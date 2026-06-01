"""
pydsa
~~~~~
A semantic DSA execution engine.

Quickstart
----------
>>> from pydsa import solve, search, info
>>>
>>> # Solve by natural description
>>> result = solve("find maximum water between vertical lines", [1,8,6,2,5,4,8,3,7])
>>> print(result.answer)           # 49
>>> print(result.time_complexity)  # O(n)
>>>
>>> # Solve by exact problem id
>>> result = solve(11, [1,8,6,2,5,4,8,3,7])
>>>
>>> # Browse problems
>>> problems = search("sliding window")
>>> for p in problems:
...     print(p.id, p.name)
>>>
>>> # Get metadata for a problem
>>> p = info("two sum")
>>> print(p.difficulty, p.tags)
"""

from __future__ import annotations

from typing import Any

from pydsa.core.models   import Problem, Result
from pydsa.core.router   import find, search as _search
from pydsa.core.engine   import execute
from pydsa.core          import registry as _registry
from pydsa.core.exceptions import (
    PyDSAError,
    ProblemNotFoundError,
    AmbiguousQueryError,
    InvalidInputError,
    SolverError,
)

__version__ = "0.1.0"
__all__ = [
    "solve",
    "search",
    "info",
    "list_problems",
    "stats",
    # models
    "Problem",
    "Result",
    # exceptions
    "PyDSAError",
    "ProblemNotFoundError",
    "AmbiguousQueryError",
    "InvalidInputError",
    "SolverError",
]


# ── Core API ──────────────────────────────────────────────────────────────────

def solve(query: str | int, /, *args: Any, **kwargs: Any) -> Result:
    """
    Find and execute the best-matching algorithm for the given query.

    Parameters
    ----------
    query : str | int
        A natural-language description, problem name, alias, tag, slug,
        or integer LeetCode problem id.
    *args :
        Input arguments forwarded directly to the solver function.
    **kwargs :
        Keyword arguments forwarded directly to the solver function.

    Returns
    -------
    Result
        Structured output with .answer, .time_complexity, .space_complexity,
        .difficulty, .tags, .description.

    Raises
    ------
    ProblemNotFoundError
        Query matched no known problem.
    AmbiguousQueryError
        Query matched multiple problems at similar confidence.
    InvalidInputError
        Input arguments are wrong for the matched solver.
    SolverError
        The solver raised an unexpected internal exception.

    Examples
    --------
    >>> solve("two sum", [2, 7, 11, 15], 9)
    Result(problem='Two Sum', answer=[0, 1], ...)

    >>> solve(11, [1,8,6,2,5,4,8,3,7])
    Result(problem='Container With Most Water', answer=49, ...)

    >>> solve("rearrange array by sign", [3, 1, -2, -5, 2, -4])
    Result(problem='Rearrange Array Elements by Sign', answer=[3,-2,1,-5,2,-4], ...)
    """
    trace_flag = kwargs.pop("trace", False)
    problem = find(query)
    result  = execute(problem, args, kwargs, trace=trace_flag)
    result.match_score = 1.0  # exact or high-confidence fuzzy
    return result


def search(query: str, limit: int = 10) -> list[Problem]:
    """
    Return up to `limit` problems matching the query, sorted by relevance.

    Unlike ``solve()``, this never raises — returns [] if nothing matches.
    Useful for autocomplete, exploration, and building UIs on top of pydsa.

    Examples
    --------
    >>> results = search("sliding window")
    >>> for p in results:
    ...     print(p.id, p.name, p.difficulty)
    """
    return _search(query, limit=limit)


def info(query: str | int) -> Problem:
    """
    Return the Problem metadata for a query without executing the solver.

    Examples
    --------
    >>> p = info("two sum")
    >>> print(p.time_complexity)  # O(n)
    >>> print(p.tags)             # ['hash_map', 'array']
    """
    return find(query)


def list_problems(
    category:   str | None = None,
    difficulty: str | None = None,
    tag:        str | None = None,
) -> list[Problem]:
    """
    List all registered problems with optional filters.

    Parameters
    ----------
    category :   filter by category  (e.g. "arrays", "dp")
    difficulty : filter by difficulty ("easy", "medium", "hard")
    tag :        filter by tag        (e.g. "two_pointer", "bfs")

    Examples
    --------
    >>> easy_dp = list_problems(category="dp", difficulty="easy")
    """
    problems = _registry.all_problems()
    if category:
        problems = [p for p in problems if p.category == category.lower()]
    if difficulty:
        problems = [p for p in problems if p.difficulty == difficulty.lower()]
    if tag:
        t = tag.lower()
        problems = [p for p in problems if t in p.tags]
    return problems


def stats() -> dict:
    """
    Return a summary of the registry.

    Examples
    --------
    >>> import pydsa
    >>> pydsa.stats()
    {'total': 3944, 'categories': {'arrays': 812, ...}, 'difficulty': {...}}
    """
    return _registry.stats()