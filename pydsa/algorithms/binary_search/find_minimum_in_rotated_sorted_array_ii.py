METADATA = {
    "id": 154,
    "name": "Find Minimum in Rotated Sorted Array II",
    "slug": "find-minimum-in-rotated-sorted-array-ii",
    "category": "Binary Search",
    "aliases": [],
    "tags": ["binary_search", "arrays"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the minimum element in a rotated sorted array that may contain duplicates.",
}

def solve(nums: list[int]) -> int:
    """
    Finds the minimum element in a rotated sorted array that may contain duplicates.

    Args:
        nums: A list of integers representing a rotated sorted array.

    Returns:
        The minimum integer in the array.

    Examples:
        >>> solve([2, 5, 6, 0, 0, 1, 2])
        0
        >>> solve([2, 2, 2, 0, 1])
        0
        >>> solve([1])
        1
    """
    left_index = 0
    right_index = len(nums) - 1

    while left_index < right_index:
        mid_index = left_index + (right_index - left_index) // 2

        if nums[mid_index] < nums[right_index]:
            # The minimum is in the left half (including mid)
            right_index = mid_index
        elif nums[mid_index] > nums[right_index]:
            # The minimum is in the right half (excluding mid)
            left_index = mid_index + 1
        else:
            # When nums[mid] == nums[right], we cannot determine which side the 
            # minimum is on due to duplicates. Shrink the search space by 1.
            right_index -= 1

    return nums[left_index]
