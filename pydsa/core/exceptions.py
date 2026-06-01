"""
pydsa.core.exceptions
~~~~~~~~~~~~~~~~~~~~~
All custom exception types for pydsa.

Design rule: every exception carries enough context for the user to
understand what went wrong and what to do next — no bare raises.
"""

from __future__ import annotations


class PyDSAError(Exception):
    """Base class for all pydsa errors."""


class ProblemNotFoundError(PyDSAError):
    """
    Raised when the search engine cannot find any problem matching the query.

    Example
    -------
    >>> solve("banana sorting algorithm", [3, 1, 2])
    ProblemNotFoundError: No problem found for query 'banana sorting algorithm'.
    Try: solve.search('sorting') to browse available problems.
    """

    def __init__(self, query: str) -> None:
        self.query = query
        super().__init__(
            f"No problem found for query {query!r}.\n"
            f"  Tip: use search({query!r}) to browse available problems."
        )


class AmbiguousQueryError(PyDSAError):
    """
    Raised when multiple problems match the query with similar confidence and
    it is unsafe to pick one automatically.

    Carries `candidates` so callers can present suggestions.
    """

    def __init__(self, query: str, candidates: list[tuple[str, float]]) -> None:
        self.query      = query
        self.candidates = candidates  # [(name, score), ...]
        options = "\n".join(
            f"  {i+1}. {name}  (score={score:.2f})"
            for i, (name, score) in enumerate(candidates)
        )
        super().__init__(
            f"Ambiguous query {query!r}. Did you mean:\n{options}\n"
            f"  Tip: be more specific or use the problem id directly."
        )


class InvalidInputError(PyDSAError):
    """
    Raised when the input provided to a solver does not match what the
    problem expects.
    """

    def __init__(self, problem: str, detail: str) -> None:
        self.problem = problem
        super().__init__(f"Invalid input for {problem!r}: {detail}")


class SolverError(PyDSAError):
    """
    Wraps unexpected exceptions raised inside a solver so the stack trace
    stays clean but the original cause is preserved.
    """

    def __init__(self, problem: str, cause: Exception) -> None:
        self.problem = problem
        self.cause   = cause
        super().__init__(f"Solver for {problem!r} raised: {type(cause).__name__}: {cause}")
