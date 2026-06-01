METADATA = {
    "id": 2235,
    "name": "Add Two Integers",
    "slug": "add_two_integers",
    "category": "math",
    "aliases": [],
    "tags": ["math"],
    "difficulty": "easy",
    "time_complexity": "O(1)",
    "space_complexity": "O(1)",
    "description": "Returns the sum of two integers.",
}

def solve(num1: int, num2: int) -> int:
    """Add two integers.

    Args:
        num1: First integer.
        num2: Second integer.

    Returns:
        The sum of ``num1`` and ``num2``.

    Examples:
        >>> solve(1, 2)
        3
        >>> solve(-5, 10)
        5
    """
    # Directly compute the sum; this operation is O(1) time and O(1) space.
    result = num1 + num2
    return result