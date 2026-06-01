METADATA = {
    "id": 2057,
    "name": "Smallest Index With Equal Value",
    "slug": "smallest_index_with_equal_value",
    "category": "Array",
    "aliases": [],
    "tags": ["arrays", "hash_map"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the smallest index where the element equals the sum of all other elements.",
}


def solve(nums: list[int]) -> int:
    """Return the smallest index i such that nums[i] equals the sum of all other elements.

    Args:
        nums: List of integers.

    Returns:
        The smallest index satisfying the condition, or -1 if none exists.

    Examples:
        >>> solve([2, 0, 2, 0])
        0
        >>> solve([1, 2, 3, 6])
        3
        >>> solve([1, 2, 3])
        -1
    """
    total_sum: int = sum(nums)  # total sum of the array
    for index, value in enumerate(nums):
        # If the sum of the remaining elements equals the current value
        if total_sum - value == value:
            return index
    return -1