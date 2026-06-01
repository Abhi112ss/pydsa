METADATA = {
    "id": 33,
    "name": "Search in Rotated Sorted Array",
    "slug": "search-in-rotated-sorted-array",
    "category": "Binary Search",
    "aliases": [],
    "tags": ["binary_search", "arrays"],
    "difficulty": "medium",
    "time_complexity": "O(log n)",
    "space_complexity": "O(1)",
    "description": "Find the index of a target value in a rotated sorted array in logarithmic time.",
}

def solve(nums: list[int], target: int) -> int:
    """
    Performs a binary search on a rotated sorted array to find the target.

    Args:
        nums: A list of integers representing a rotated sorted array.
        target: The integer value to search for.

    Returns:
        The index of the target if found, otherwise -1.

    Examples:
        >>> solve([4, 5, 6, 7, 0, 1, 2], 0)
        4
        >>> solve([4, 5, 6, 7, 0, 1, 2], 3)
        -1
        >>> solve([1], 0)
        -1
    """
    left_index = 0
    right_index = len(nums) - 1

    while left_index <= right_index:
        mid_index = (left_index + right_index) // 2

        if nums[mid_index] == target:
            return mid_index

        # Identify which half is sorted. 
        # In a rotated sorted array, at least one half (left or right) must be sorted.
        
        # Case 1: The left half [left_index...mid_index] is sorted
        if nums[left_index] <= nums[mid_index]:
            # Check if the target lies within the range of this sorted left half
            if nums[left_index] <= target < nums[mid_index]:
                right_index = mid_index - 1
            else:
                left_index = mid_index + 1
        
        # Case 2: The right half [mid_index...right_index] is sorted
        else:
            # Check if the target lies within the range of this sorted right half
            if nums[mid_index] < target <= nums[right_index]:
                left_index = mid_index + 1
            else:
                right_index = mid_index - 1

    return -1
