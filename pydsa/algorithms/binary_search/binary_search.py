METADATA = {
    "id": 704,
    "name": "Binary Search",
    "slug": "binary_search",
    "category": "Search",
    "aliases": [],
    "tags": ["binary_search", "divide_and_conquer"],
    "difficulty": "easy",
    "time_complexity": "O(log n)",
    "space_complexity": "O(1)",
    "description": "Find the index of a target value in a sorted array using binary search.",
}


def solve(nums: list[int], target: int) -> int:
    """Searches for ``target`` in a sorted list ``nums`` using binary search.

    Args:
        nums: A list of integers sorted in non‑decreasing order.
        target: The integer value to locate within ``nums``.

    Returns:
        The index of ``target`` if it exists in ``nums``; otherwise ``-1``.

    Examples:
        >>> solve([1, 2, 3, 4, 5], 3)
        2
        >>> solve([1, 2, 3, 4, 5], 6)
        -1
    """
    left: int = 0
    right: int = len(nums) - 1

    while left <= right:
        middle: int = left + (right - left) // 2  # avoid overflow
        middle_value: int = nums[middle]

        if middle_value == target:
            return middle  # target found
        if middle_value < target:
            left = middle + 1  # discard left half
        else:
            right = middle - 1  # discard right half

    return -1  # target not present