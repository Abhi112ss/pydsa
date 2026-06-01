METADATA = {
    "id": 81,
    "name": "Search in Rotated Sorted Array II",
    "slug": "search-in-rotated-sorted-array-ii",
    "category": "Binary Search",
    "aliases": [],
    "tags": ["binary_search", "two_pointers"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Search for a target value in a rotated sorted array that may contain duplicates.",
}

def solve(nums: list[int], target: int) -> bool:
    """
    Searches for a target value in a rotated sorted array that may contain duplicates.

    Args:
        nums: A list of integers representing a rotated sorted array.
        target: The integer value to search for.

    Returns:
        True if the target is found in the array, False otherwise.

    Examples:
        >>> solve([2, 5, 6, 0, 0, 1, 2], 0)
        True
        >>> solve([2, 5, 6, 0, 0, 1, 2], 3)
        False
        >>> solve([1, 0, 1, 1, 1], 0)
        True
    """
    left_index = 0
    right_index = len(nums) - 1

    while left_index <= right_index:
        mid_index = (left_index + right_index) // 2

        if nums[mid_index] == target:
            return True

        # Handle the case where duplicates make it impossible to determine 
        # which side is sorted (e.g., [1, 0, 1, 1, 1])
        if nums[left_index] == nums[mid_index] == nums[right_index]:
            left_index += 1
            right_index -= 1
            continue

        # Determine if the left half is sorted
        if nums[left_index] <= nums[mid_index]:
            # Check if target lies within the sorted left half
            if nums[left_index] <= target < nums[mid_index]:
                right_index = mid_index - 1
            else:
                left_index = mid_index + 1
        # Otherwise, the right half must be sorted
        else:
            # Check if target lies within the sorted right half
            if nums[mid_index] < target <= nums[right_index]:
                left_index = mid_index + 1
            else:
                right_index = mid_index - 1

    return False
