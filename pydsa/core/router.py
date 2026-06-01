"""
pydsa.core.router
~~~~~~~~~~~~~~~~~
Semantic search layer that maps a free-text query to one or more Problems.

SEARCH STRATEGY (layered, fastest-first)
-----------------------------------------
1. Exact id match          (query is a plain integer)
2. Exact slug match        (query == slug)
3. Exact name match        (case-insensitive)
4. Alias exact match       (query in any problem's alias list)
5. Tag match               (query matches one or more tags)
6. Fuzzy match via rapidfuzz  (token_set_ratio on search_corpus)

Each layer is tried in order; we return as soon as we have high-confidence
results.  If confidence across all layers is too low we raise
AmbiguousQueryError or ProblemNotFoundError with suggestions.

FUTURE LAYERS (not implemented yet — stubs are in search/embeddings.py)
------------------------------------------------------------------------
7. Vector embedding search  (pre-computed numpy array, cosine similarity)
8. LLM intent classification (optional cloud API call)
"""

from __future__ import annotations

import logging
from typing import Optional
from pydsa.search import embeddings
from pydsa.core.models import Problem
from pydsa.core import registry as _reg
from pydsa.core.exceptions import ProblemNotFoundError, AmbiguousQueryError

_HAS_PROMPTED_AI = False

log = logging.getLogger(__name__)

# Thresholds (tune without touching callers)
_EXACT_SCORE        = 1.0
_HIGH_CONFIDENCE    = 0.72   # auto-pick if best score ≥ this
_AMBIGUOUS_CUTOFF   = 0.50   # surface as a candidate if score ≥ this
_TOP_K              = 5      # max candidates to return / show in errors


# ── Internal helpers ──────────────────────────────────────────────────────────

def _fuzzy_scores(query: str) -> list[tuple[Problem, float]]:
    """
    Score every problem against the query using rapidfuzz.
    Returns list of (Problem, 0.0–1.0) sorted descending.
    Falls back to simple substring matching if rapidfuzz is not installed.
    """
    q = query.lower().strip()
    problems = _reg.all_problems()

    try:
        from rapidfuzz import fuzz
        scored = [
            (p, fuzz.token_set_ratio(q, p.search_corpus()) / 100.0)
            for p in problems
        ]
    except ImportError:
        log.debug("rapidfuzz not installed — using substring fallback")
        scored = []
        for p in problems:
            corpus = p.search_corpus()
            if q in corpus:
                score = len(q) / len(corpus)        # crude but functional
            else:
                # count matching words
                q_words = set(q.split())
                c_words = set(corpus.split())
                score   = len(q_words & c_words) / max(len(q_words), 1) * 0.6
            scored.append((p, score))

    scored.sort(key=lambda x: x[1], reverse=True)
    return scored


def _tag_search(query: str) -> list[Problem]:
    """Return problems whose tags contain any word from the query."""
    words = set(query.lower().replace("-", "_").split())
    results = []
    for p in _reg.all_problems():
        if words & set(p.tags):
            results.append(p)
    return results


# ── Public API ────────────────────────────────────────────────────────────────

def find(query: str | int, top_k: int = _TOP_K) -> Problem:
    """
    Resolve a free-text query (or integer id) to a single Problem.

    Parameters
    ----------
    query:
        A natural-language description, problem name, alias, tag, slug,
        or integer LeetCode id.
    top_k:
        How many candidates to surface in AmbiguousQueryError.

    Returns
    -------
    Problem
        The best-matching problem.

    Raises
    ------
    ProblemNotFoundError
        No match found above the minimum confidence threshold.
    AmbiguousQueryError
        Multiple matches exist with similar scores and it is unsafe
        to auto-pick one.
    """
    _reg._ensure_loaded()

    # ── Layer 1: integer id ───────────────────────────────────────────────────
    if isinstance(query, int) or (isinstance(query, str) and query.strip().isdigit()):
        return _reg.get_by_id(int(query))

    q = str(query).strip()

    # ── Layer 2: exact slug ───────────────────────────────────────────────────
    slug_q = q.lower().replace(" ", "-").replace("_", "-")
    try:
        return _reg.get_by_slug(slug_q)
    except ProblemNotFoundError:
        pass
    slug_q2 = q.lower().replace(" ", "_").replace("-", "_")
    try:
        return _reg.get_by_slug(slug_q2)
    except ProblemNotFoundError:
        pass

    # ── Layer 3: exact name ───────────────────────────────────────────────────
    try:
        return _reg.get_by_name(q)
    except ProblemNotFoundError:
        pass

    # ── Layer 4: alias exact match ────────────────────────────────────────────
    q_lower = q.lower()
    for p in _reg.all_problems():
        if q_lower in p.aliases:
            log.debug("Alias match: %r → %s", q, p.name)
            return p

    # ── Layer 5: tag match (single unambiguous hit) ───────────────────────────
    tag_hits = _tag_search(q)
    if len(tag_hits) == 1:
        return tag_hits[0]
    
    # ── Layer 5.5: Semantic Vector Search ─────────────────────────────────────
    if embeddings.is_available():
        vector_scored = embeddings.search(q, top_k=top_k)
        if vector_scored:
            best_problem, best_score = vector_scored[0]
            
            # Cosine similarity scales differently than fuzzy text matching.
            # A score of 0.45+ is generally a highly accurate semantic match.
            if best_score >= 0.45:
                log.debug("Vector match: %r → %s (score=%.2f)", q, best_problem.name, best_score)
                return best_problem
                
            # If the query is vague, surface the best guesses
            candidates = [(p.name, score) for p, score in vector_scored if score >= 0.30]
            if candidates:
                if len(candidates) == 1:
                    return vector_scored[0][0]
                raise AmbiguousQueryError(q, candidates)
                
            raise ProblemNotFoundError(q)
    else:
        global _HAS_PROMPTED_AI
        if not _HAS_PROMPTED_AI:
            print("\n💡 Tip: Your query was routed using text-matching.")
            print("   For intelligent, semantic AI routing, enable the vector engine:")
            print("   Run: pip install \"pydsa[search]\"\n")
            _HAS_PROMPTED_AI = True

    # ── Layer 6: fuzzy scoring ────────────────────────────────────────────────
    scored = _fuzzy_scores(q)

    if not scored:
        raise ProblemNotFoundError(q)

    best_problem, best_score = scored[0]

    # High confidence → auto-pick
    if best_score >= _HIGH_CONFIDENCE:
        log.debug("Fuzzy match: %r → %s (score=%.2f)", q, best_problem.name, best_score)
        return best_problem

    # Collect candidates above ambiguous cutoff
    candidates = [
        (p.name, score)
        for p, score in scored[:top_k]
        if score >= _AMBIGUOUS_CUTOFF
    ]

    if not candidates:
        raise ProblemNotFoundError(q)

    if len(candidates) == 1:
        return scored[0][0]

    raise AmbiguousQueryError(q, candidates)


def search(query: str, limit: int = 10) -> list[Problem]:
    """
    Return up to `limit` problems matching the query, sorted by relevance.
    Never raises — returns an empty list if nothing matches.

    Use this for browse / autocomplete UIs.
    """
    _reg._ensure_loaded()
    scored = _fuzzy_scores(query)
    return [
        p for p, score in scored[:limit]
        if score >= _AMBIGUOUS_CUTOFF
    ]
