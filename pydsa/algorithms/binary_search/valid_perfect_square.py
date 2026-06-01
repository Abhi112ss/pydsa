METADATA = {
    "id": 367,
    "name": "Valid Perfect Square",
    "slug": "valid_perfect_square",
    "category": "Math",
    "aliases": ["Valid Perfect Square"],
    "tags": ["math", "binary_search"],
    "difficulty": "easy",
    "time_complexity": "O(log n)",
    "space_complexity": "O(1)",
    "description": "Determine if a given integer is a perfect square without using built‑in sqrt.",
}


def solve(num: int) -> bool:
    """Determine whether ``num`` is a perfect square using binary search.

    Args:
        num: A positive integer (1 ≤ num ≤ 2**31 - 1).

    Returns:
        True if ``num`` is a perfect square, otherwise False.

    Examples:
        >>> solve(16)
        True
        >>> solve(14)
        False
        >>> solve(1)
        True
    """
    if num < 1:
        return False

    left = 1
    right = num

    while left <= right:
        mid = (left + right) // 2
        square = mid * mid

        if square == num:
            return True
        if square < num:
            left = mid + 1  # discard left half
        else:
            right = mid - 1  # discard right half

    return False