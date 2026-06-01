METADATA = {
    "id": 1533,
    "name": "Find the Index of the Large Integer",
    "slug": "find_the_index_of_the_large_integer",
    "category": "Array",
    "aliases": [],
    "tags": ["arrays"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Return the index of the maximum element if it appears exactly once, otherwise -1.",
}


def solve(nums: list[int]) -> int:
    """Find the index of the large integer.

    Args:
        nums: List of integers.

    Returns:
        The index of the maximum integer if it occurs exactly once; otherwise -1.

    Examples:
        >>> solve([1, 2, 3, 4])
        3
        >>> solve([5, 5, 1])
        -1
        >>> solve([10])
        0
    """
    if not nums:
        return -1

    max_value = nums[0]
    max_index = 0
    max_count = 1

    # Single pass to track maximum value, its first index, and occurrence count
    for current_index in range(1, len(nums)):
        current_value = nums[current_index]
        if current_value > max_value:
            max_value = current_value
            max_index = current_index
            max_count = 1
        elif current_value == max_value:
            max_count += 1

    return max_index if max_count == 1 else -1