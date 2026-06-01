METADATA = {
    "id": 2723,
    "name": "Add Two Promises",
    "slug": "add_two_promises",
    "category": "async_programming",
    "aliases": [],
    "tags": ["async_programming"],
    "difficulty": "easy",
    "time_complexity": "O(1)",
    "space_complexity": "O(1)",
    "description": "Awaits two promises and returns their sum.",
}

from typing import Awaitable

async def solve(promise1: Awaitable[int], promise2: Awaitable[int]) -> int:
    """Awaits two integer promises and returns their sum.

    Args:
        promise1: An awaitable that resolves to an integer.
        promise2: An awaitable that resolves to an integer.

    Returns:
        The sum of the two resolved integer values.

    Examples:
        >>> import asyncio
        >>> async def main():
        ...     async def p1(): return 3
        ...     async def p2(): return 5
        ...     result = await solve(p1(), p2())
        ...     print(result)  # prints 8
        >>> asyncio.run(main())
    """
    # Await each promise to retrieve its integer value.
    value1 = await promise1
    value2 = await promise2
    # Return the sum of the two values.
    return value1 + value2