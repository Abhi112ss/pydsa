METADATA = {
    "id": 326,
    "name": "Power of Three",
    "slug": "power_of_three",
    "category": "Math",
    "aliases": [],
    "tags": ["math", "recursion"],
    "difficulty": "easy",
    "time_complexity": "O(1)",
    "space_complexity": "O(1)",
    "description": "Determine whether an integer is a power of three.",
}


def solve(n: int) -> bool:
    """Return ``True`` if ``n`` is a power of three, otherwise ``False``.

    Args:
        n: The integer to evaluate.

    Returns:
        ``True`` if ``n`` is a positive power of three, ``False`` otherwise.

    Examples:
        >>> solve(27)
        True
        >>> solve(0)
        False
        >>> solve(45)
        False
    """
    if n <= 0:
        return False

    # Largest power of three that fits in a 32‑bit signed integer (3**19).
    max_power_of_three = 1162261467

    # If ``n`` divides this maximum power, it must be a power of three.
    return max_power_of_three % n == 0