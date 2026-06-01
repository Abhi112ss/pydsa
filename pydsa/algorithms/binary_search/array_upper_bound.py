METADATA = {
    "id": 2774,
    "name": "Array Upper Bound",
    "slug": "array-upper-bound",
    "category": "Binary Search",
    "aliases": [],
    "tags": ["binary_search", "array"],
    "difficulty": "easy",
    "time_complexity": "O(log n)",
    "space_complexity": "O(1)",
    "description": "Find the smallest index i such that nums[i] is greater than or equal to a given target value using binary search.",
}

def solve(nums: list[int], target: int) -> int:
    """
    Finds the smallest index i such that nums[i] >= target in a sorted array.

    Args:
        nums: A sorted list of integers.
        target: The value to compare against.

    Returns:
        The smallest index i where nums[i] >= target. 
        If no such element exists, returns the length of the array.

    Examples:
        >>> solve([1, 2, 4, 4, 5, 6], 4)
        2
        >>> solve([1, 2, 4, 4, 5, 6], 7)
        6
        >>> solve([1, 2, 4, 4, 5, 6], 0)
        0
    """
    left_index = 0
    right_index = len(nums) - 1
    result_index = len(nums)

    while left_index <= right_index:
        mid_index = left_index + (right_index - left_index) // 2

        # If current element meets the condition, it's a potential candidate.
        # We record it and try to find a smaller index to the left.
        if nums[mid_index] >= target:
            result_index = mid_index
            right_index = mid_index - 1
        else:
            # If current element is too small, the target must be to the right.
            left_index = mid_index + 1

    return result_index
