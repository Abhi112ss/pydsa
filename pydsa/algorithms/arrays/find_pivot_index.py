METADATA = {
    "id": 724,
    "name": "Find Pivot Index",
    "slug": "find_pivot_index",
    "category": "Array",
    "aliases": ["pivot_index", "equilibrium_index"],
    "tags": ["prefix_sum"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the pivot index where the sum of elements to the left equals the sum of elements to the right.",
}

from typing import Optional

def solve(nums: list[int]) -> int:
    """Find the pivot index where the sum of elements to the left equals the sum of elements to the right.

    Args:
        nums: A list of integers.

    Returns:
        The pivot index if found, otherwise -1.

    Examples:
        >>> solve([1, 7, 3, 6, 5, 6])
        3
        >>> solve([1, 2, 3])
        -1
        >>> solve([2, 1, -1])
        0
    """
    total_sum = sum(nums)
    left_sum = 0

    for index, num in enumerate(nums):
        # Check if left sum equals right sum (total_sum - left_sum - num)
        if left_sum == total_sum - left_sum - num:
            return index
        left_sum += num

    return -1