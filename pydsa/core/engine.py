"""
pydsa.core.engine
~~~~~~~~~~~~~~~~~
Solver execution engine.

Responsibilities
----------------
* Receive a resolved Problem + raw user args/kwargs
* Execute the solver safely (catching internal errors)
* Wrap the return value in a structured Result
* Never leak raw solver exceptions to the user
"""

from __future__ import annotations

import logging
import sys

from pydsa.core.models import Problem, Result
from pydsa.core.exceptions import InvalidInputError, SolverError

log = logging.getLogger(__name__)


def execute(problem: Problem, args: tuple, kwargs: dict, trace: bool = False) -> Result:
    if problem.solver is None:
        raise InvalidInputError(problem.name, "this problem has no solver implementation yet.")

    if not args and not kwargs:
        raise InvalidInputError(problem.name, "no input provided.")

    log.debug("Executing solver for %r", problem.name)

    trace_history = []
    
    try:
        if trace:
            from pydsa.core.tracer import AlgorithmTracer
            
            # Start the spy
            tracer = AlgorithmTracer("solve")
            sys.settrace(tracer.trace_calls)
            
            # Run the code
            answer = problem.solver(*args, **kwargs)
            
            # Turn off the spy
            sys.settrace(None)
            trace_history = tracer.history
        else:
            answer = problem.solver(*args, **kwargs)
            
    except TypeError as exc:
        sys.settrace(None) # Always turn off trace on crash
        raise InvalidInputError(problem.name, f"argument mismatch — {exc}") from exc
    except Exception as exc:
        sys.settrace(None)
        raise SolverError(problem.name, exc) from exc

    return Result(
        problem          = problem.name,
        answer           = answer,
        time_complexity  = problem.time_complexity,
        space_complexity = problem.space_complexity,
        category         = problem.category,
        difficulty       = problem.difficulty,
        tags             = problem.tags,
        description      = problem.description,
        trace_history    = trace_history, # Add it to the result!
    )
