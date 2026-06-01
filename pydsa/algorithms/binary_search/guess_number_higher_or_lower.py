METADATA = {
    "id": 374,
    "name": "Guess Number Higher or Lower",
    "slug": "guess_number_higher_or_lower",
    "category": "Binary Search",
    "aliases": ["Guess Number Higher or Lower"],
    "tags": ["binary_search", "interactive"],
    "difficulty": "easy",
    "time_complexity": "O(log n)",
    "space_complexity": "O(1)",
    "description": "Guess the number using binary search based on the guess API feedback.",
}

def solve(n: int, pick: int) -> int:
    """Guess the number using binary search based on the guess API feedback.

    Args:
        n (int): The upper bound of the range [1, n].
        pick (int): The number to be guessed.

    Returns:
        int: The guessed number.

    Examples:
        >>> solve(10, 6)
        6
        >>> solve(1, 1)
        1
        >>> solve(2, 1)
        1
    """
    def guess(num: int) -> int:
        if num > pick:
            return -1
        elif num < pick:
            return 1
        else:
            return 0

    low = 1
    high = n
    while low <= high:
        mid = (low + high) // 2
        result = guess(mid)
        if result == 0:
            return mid
        elif result == -1:
            high = mid - 1
        else:
            low = mid + 1
    return -1