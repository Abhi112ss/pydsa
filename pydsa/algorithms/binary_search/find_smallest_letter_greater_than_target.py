METADATA = {
    "id": 744,
    "name": "Find Smallest Letter Greater Than Target",
    "slug": "find_smallest_letter_greater_than_target",
    "category": "Binary Search",
    "aliases": [],
    "tags": ["binary_search"],
    "difficulty": "easy",
    "time_complexity": "O(log n)",
    "space_complexity": "O(1)",
    "description": "Given a sorted array of characters and a target character, find the smallest character in the array that is strictly greater than the target, wrapping around if necessary.",
}


def solve(letters: list[str], target: str) -> str:
    """Find the smallest letter in a sorted list that is strictly greater than target.

    Uses binary search to find the upper bound of target in the sorted array.
    If no such letter exists (target >= last element), wraps around to the first element.

    Args:
        letters: A sorted list of lowercase English letters (non-decreasing order).
        target: A single lowercase English letter to compare against.

    Returns:
        The smallest letter in letters that is strictly greater than target,
        or the first letter if no such letter exists (wrap-around).

    Examples:
        >>> solve(["c", "f", "j"], "a")
        'c'
        >>> solve(["c", "f", "j"], "c")
        'f'
        >>> solve(["c", "f", "j"], "j")
        'c'
        >>> solve(["c", "f", "j"], "k")
        'c'
    """
    left = 0
    right = len(letters) - 1

    # Binary search for the first letter strictly greater than target
    while left <= right:
        mid = (left + right) // 2
        if letters[mid] <= target:
            # Current letter is not greater, search the right half
            left = mid + 1
        else:
            # Current letter is greater, but there might be a smaller one on the left
            right = mid - 1

    # left is the index of the smallest letter > target, or len(letters) if none found
    # Use modulo to wrap around to the first element when left goes past the end
    return letters[left % len(letters)]