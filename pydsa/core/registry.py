"""
pydsa.core.registry
~~~~~~~~~~~~~~~~~~~~
Central problem registry.

HOW IT WORKS
------------
At import time the registry walks every ``pydsa/algorithms/<category>/``
sub-package and imports each solver module.  Any module that exposes a
top-level ``METADATA`` dict and a ``solve`` callable is registered
automatically.

Adding a new problem requires only ONE file — no manual registry edits.

DESIGN NOTES
------------
* We use importlib so the scan works whether pydsa is installed as a wheel
  or run from source.
* The registry is a singleton (_REGISTRY) built once on first access.
* Thread safety is not a concern for the initial release (CLI / notebook use).
"""

from __future__ import annotations

import importlib
import importlib.util
import logging
import pkgutil
from pathlib import Path
from typing import Iterator

from pydsa.core.models import Problem
from pydsa.core.exceptions import ProblemNotFoundError

log = logging.getLogger(__name__)

# ── Internal store ────────────────────────────────────────────────────────────

_by_id:   dict[int,  Problem] = {}   # id  → Problem
_by_slug: dict[str,  Problem] = {}   # slug → Problem
_by_name: dict[str,  Problem] = {}   # lower(name) → Problem
_all:     list[Problem]       = []
_loaded   = False


# ── Loader ────────────────────────────────────────────────────────────────────

def _iter_solver_modules() -> Iterator[str]:
    """
    Yield fully-qualified module names for every file inside
    pydsa.algorithms.* that does NOT start with underscore.
    """
    # Bulletproof path resolution relative to registry.py itself
    # registry.py is in pydsa/core/, so algorithms/ is parent.parent / "algorithms"
    alg_path = Path(__file__).resolve().parent.parent / "algorithms"

    if not alg_path.exists():
        log.warning("Algorithms directory not found at %s", alg_path)
        return

    for category_dir in sorted(alg_path.iterdir()):
        if not category_dir.is_dir() or category_dir.name.startswith("_") or category_dir.name.endswith(".bad.py"):
            continue
        for file in sorted(category_dir.glob("*.py")):
            if file.name.startswith("_"):
                continue
            module_name = (
                f"pydsa.algorithms.{category_dir.name}.{file.stem}"
            )
            yield module_name


def _load_module(module_name: str) -> None:
    """Import one solver module and register it if it has METADATA + solve."""
    try:
        mod = importlib.import_module(module_name)
    except Exception as exc:
        log.warning("Could not import %s: %s", module_name, exc)
        return

    metadata: dict = getattr(mod, "METADATA", None)
    solver_fn      = getattr(mod, "solve", None)

    if metadata is None or solver_fn is None:
        log.debug("Skipping %s — no METADATA or solve()", module_name)
        return

    # Validate required keys
    required = {"id", "name", "slug", "category", "difficulty",
                "time_complexity", "space_complexity", "description"}
    missing = required - metadata.keys()
    if missing:
        log.warning("Skipping %s — METADATA missing keys: %s", module_name, missing)
        return

    problem = Problem(
        id               = int(metadata["id"]),
        name             = metadata["name"],
        slug             = metadata["slug"],
        category         = metadata.get("category", "").lower(),
        difficulty       = metadata.get("difficulty", "unknown").lower(),
        time_complexity  = metadata.get("time_complexity", "?"),
        space_complexity = metadata.get("space_complexity", "?"),
        description      = metadata.get("description", ""),
        aliases          = [a.lower() for a in metadata.get("aliases", [])],
        tags             = [t.lower() for t in metadata.get("tags", [])],
        solver           = solver_fn,
    )

    _by_id[problem.id]          = problem
    _by_slug[problem.slug]      = problem
    _by_name[problem.name.lower()] = problem
    _all.append(problem)


def _ensure_loaded() -> None:
    global _loaded
    if _loaded:
        return
    for module_name in _iter_solver_modules():
        _load_module(module_name)
    _all.sort(key=lambda p: p.id)
    _loaded = True
    log.debug("Registry loaded: %d problems", len(_all))


# ── Public API ────────────────────────────────────────────────────────────────

def all_problems() -> list[Problem]:
    """Return all registered problems sorted by id."""
    _ensure_loaded()
    return list(_all)


def get_by_id(problem_id: int) -> Problem:
    """Exact lookup by LeetCode problem id."""
    _ensure_loaded()
    if problem_id not in _by_id:
        raise ProblemNotFoundError(str(problem_id))
    return _by_id[problem_id]


def get_by_slug(slug: str) -> Problem:
    """Exact lookup by snake_case slug."""
    _ensure_loaded()
    if slug not in _by_slug:
        raise ProblemNotFoundError(slug)
    return _by_slug[slug]


def get_by_name(name: str) -> Problem:
    """Case-insensitive exact name lookup."""
    _ensure_loaded()
    key = name.lower()
    if key not in _by_name:
        raise ProblemNotFoundError(name)
    return _by_name[key]


def filter_by_category(category: str) -> list[Problem]:
    _ensure_loaded()
    cat = category.lower()
    return [p for p in _all if p.category == cat]


def filter_by_difficulty(difficulty: str) -> list[Problem]:
    _ensure_loaded()
    diff = difficulty.lower()
    return [p for p in _all if p.difficulty == diff]


def filter_by_tag(tag: str) -> list[Problem]:
    _ensure_loaded()
    t = tag.lower()
    return [p for p in _all if t in p.tags]


def stats() -> dict:
    """Quick summary of the registry for debugging / CLI."""
    _ensure_loaded()
    from collections import Counter
    cats  = Counter(p.category   for p in _all)
    diffs = Counter(p.difficulty for p in _all)
    return {
        "total":      len(_all),
        "categories": dict(cats),
        "difficulty": dict(diffs),
    }
