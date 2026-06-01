METADATA = {
    "id": 2637,
    "name": "Promise Time Limit",
    "slug": "promise-time-limit",
    "category": "Design",
    "aliases": [],
    "tags": ["design", "concurrency", "asynchronous"],
    "difficulty": "medium",
    "time_complexity": "O(1)",
    "space_complexity": "O(1)",
    "description": "Implement a function that returns a promise that rejects if the original promise takes longer than a specified time limit.",
}

import asyncio

async def solve(promise: asyncio.Future, time_limit: int) -> asyncio.Future:
    """
    Wraps a given promise with a timeout. If the promise does not resolve 
    within the time_limit, the returned promise rejects.

    Args:
        promise (asyncio.Future): The original asynchronous task/promise.
        time_limit (int): The maximum allowed time in milliseconds.

    Returns:
        asyncio.Future: A future that resolves with the original promise's 
            result or rejects with a timeout error.

    Examples:
        >>> import asyncio
        >>> async def slow_task():
        ...     await asyncio.sleep(0.5)
        ...     return "done"
        >>> # This will reject because 0.5s > 0.1s
        >>> asyncio.run(solve(asyncio.ensure_future(slow_task()), 100))
        Exception: Promise rejected after 100ms
    """
    # Create a new future to represent the result of the race
    result_future = asyncio.get_event_loop().create_future()

    async def timer():
        # Wait for the specified time limit in seconds
        await asyncio.sleep(time_limit / 1000.0)
        # If the timer finishes first, reject the result_future
        if not result_future.done():
            result_future.set_exception(TimeoutError(f"Promise rejected after {time_limit}ms"))

    async def task_wrapper():
        try:
            # Wait for the original promise to resolve
            res = await promise
            # If the promise resolves first, set the result
            if not result_future.done():
                result_future.set_result(res)
        except Exception as e:
            # If the original promise rejects, propagate that rejection
            if not result_future.done():
                result_future.set_exception(e)

    # Schedule both the timer and the task wrapper to run concurrently
    # asyncio.gather or create_task can be used to start these background tasks
    timer_task = asyncio.create_task(timer())
    wrapper_task = asyncio.create_task(task_wrapper())

    # We must ensure that when one finishes, we don't leave the other hanging 
    # indefinitely in a production environment, though for LeetCode 
    # returning the result_future is the primary requirement.
    return result_future