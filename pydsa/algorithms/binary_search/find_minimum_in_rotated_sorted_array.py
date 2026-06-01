METADATA = {
    "id": 153,
    "name": "Find Minimum in Rotated Sorted Array",
    "slug": "find-minimum-in-rotated-sorted-array",
    "category": "Binary Search",
    "aliases": [],
    "tags": ["binary_search", "arrays", "sorted_array"],
    "difficulty": "medium",
    "time_complexity": "O(log n)",
    "space_complexity": "O(1)",
    "description": "Find the minimum element in a sorted array that has been rotated between 1 and n times.",
}

def solve(nums: list[int]) -> int:
    """
    Finds the minimum element in a rotated sorted array using binary search.

    Args:
        nums: A list of integers representing a rotated sorted array.

    Returns:
        The minimum integer in the array.

    Examples:
        >>> solve([3, 4, 5, 1, 2])
        1
        >>> solve([4, 5, 6, 7, 0, 1, 2])
        0
        >>> solve([11, 13, 15, 17])
        11
    """
    left_index = 0
    right_index = len(nums) - 1

    # If the array is not rotated (or rotated n times), the first element is the minimum
    if nums[left_index] <= nums[right_index]:
        return nums[left_index]

    while left_index <= right_index:
        mid_index = left_index + (right_index - left_index) // 2

        # If the middle element is greater than its next element, 
        # the next element is the minimum (the inflection point)
        if mid_index < len(nums) - 1 and nums[mid_index] > nums[mid_index + 1]:
            return nums[mid_index + 1]

        # If the middle element is less than its previous element,
        # the middle element is the minimum
        if mid_index > 0 and nums[mid_index] < nums[mid_index - 1]:
            return nums[mid_index]

        # Decide which half to search:
        # If the middle element is greater than the leftmost element,
        # the inflection point (minimum) must be in the right half.
        if nums[mid_index] > nums[left_index]:
            left_index = mid_index + 1
        else:
            # Otherwise, the inflection point is in the left half.
            right_index = mid_index - 1

    return nums[0]
