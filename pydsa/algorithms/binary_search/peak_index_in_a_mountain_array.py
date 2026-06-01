METADATA = {
    "id": 852,
    "name": "Peak Index in a Mountain Array",
    "slug": "peak_index_in_a_mountain_array",
    "category": "array",
    "aliases": [],
    "tags": ["binary search", "array"],
    "difficulty": "easy",
    "time_complexity": "O(log n)",
    "space_complexity": "O(1)",
    "description": "Find the index of the peak element in a mountain array.",
}


def solve(arr: list[int]) -> int:
    """Find the peak index in a mountain array using binary search.

    Args:
        arr: A list of integers that first strictly increases then strictly decreases.
            It is guaranteed to have a peak (length >= 3).

    Returns:
        The index of the peak element.

    Examples:
        >>> solve([0, 1, 0])
        1
        >>> solve([0, 2, 1, 0])
        1
    """
    left = 0
    right = len(arr) - 1

    # Binary search: move left bound up when slope is positive,
    # otherwise move right bound down.
    while left < right:
        mid = (left + right) // 2
        if arr[mid] < arr[mid + 1]:
            left = mid + 1  # peak is to the right
        else:
            right = mid      # peak is at mid or to the left

    return left