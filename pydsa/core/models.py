"""
pydsa.core.models
~~~~~~~~~~~~~~~~~
Canonical dataclasses for the problem registry and execution results.
All other modules import from here — never import in the other direction.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from typing import Any, Callable, Optional


@dataclass
class Problem:
    """
    A single registered algorithm problem.

    Every solver file exposes a METADATA dict that gets loaded into this
    dataclass by the registry at startup.  All fields except `solver` are
    plain data so they can be serialised to JSON or searched easily.
    """

    id:               int
    name:             str
    slug:             str
    category:         str
    difficulty:       str                        # "easy" | "medium" | "hard"
    time_complexity:  str                        # e.g. "O(n)"
    space_complexity: str                        # e.g. "O(1)"
    description:      str
    aliases:          list[str]  = field(default_factory=list)
    tags:             list[str]  = field(default_factory=list)
    solver:           Optional[Callable] = field(default=None, repr=False)

    # ── convenience ──────────────────────────────────────────────────────────

    def search_corpus(self) -> str:
        """
        Single string used by the fuzzy / semantic search engine.
        Combines every human-readable field so one query can match any of them.
        """
        parts = [self.name] + self.aliases + self.tags + [self.category, self.description]
        return " ".join(parts).lower()

    def to_dict(self) -> dict[str, Any]:
        """Serialisable representation (no solver callable)."""
        return {
            "id":               self.id,
            "name":             self.name,
            "slug":             self.slug,
            "category":         self.category,
            "difficulty":       self.difficulty,
            "time_complexity":  self.time_complexity,
            "space_complexity": self.space_complexity,
            "description":      self.description,
            "aliases":          self.aliases,
            "tags":             self.tags,
        }


@dataclass
class Result:
    """
    Structured output returned by the execution engine after solving a problem.
    """

    problem:          str          # canonical problem name
    answer:           Any          # the actual computed answer
    time_complexity:  str
    space_complexity: str
    category:         str   = ""
    difficulty:       str   = ""
    tags:             list[str] = field(default_factory=list)
    description:      str   = ""
    match_score:      float = 1.0  # 0.0–1.0 confidence of the search match
    trace_history:    list  = field(default_factory=list) # ADD THIS LINE

    def __repr__(self) -> str:
        return (
            f"Result(\n"
            f"  problem         = {self.problem!r}\n"
            f"  answer          = {self.answer!r}\n"
            f"  time_complexity = {self.time_complexity!r}\n"
            f"  space_complexity= {self.space_complexity!r}\n"
            f"  difficulty      = {self.difficulty!r}\n"
            f")"
        )
