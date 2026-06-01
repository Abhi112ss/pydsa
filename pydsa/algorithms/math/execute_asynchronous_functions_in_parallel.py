METADATA = {
    "id": 2721,
    "name": "Execute Asynchronous Functions in Parallel",
    "slug": "execute_asynchronous_functions_in_parallel",
    "category": "Concurrency",
    "aliases": [],
    "tags": ["async_programming", "concurrency"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Runs a list of asynchronous functions concurrently and returns their results in order.",
}

import asyncio
from typing import Callable, Awaitable, Any


def solve(async_functions: list[Callable[[], Awaitable[Any]]]) -> list[Any]:
    """Execute a collection of asynchronous functions in parallel.

    Args:
        async_functions: A list where each element is a callable that returns an
            awaitable (e.g., a coroutine). The callable takes no arguments.

    Returns:
        A list containing the results of each asynchronous function, ordered
        identically to the input list.

    Examples:
        >>> import asyncio
        >>> async def f1(): await asyncio.sleep(0.1); return 1
        >>> async def f2(): await asyncio.sleep(0.2); return 2
        >>> results = solve([lambda: f1(), lambda: f2()])
        >>> results
        [1, 2]
    """
    async def _run_all() -> list[Any]:
        # Create coroutine objects for all functions; this does not start execution yet.
        coroutines = [func() for func in async_functions]
        # asyncio.gather schedules all coroutines concurrently and preserves order.
        return await asyncio.gather(*coroutines)

    # Run the asynchronous helper in a new event loop and return the gathered results.
    return asyncio.run(_run_all())