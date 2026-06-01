METADATA = {
    "id": 75,
    "name": "Sort Colors",
    "slug": "sort-colors",
    "category": "Array",
    "aliases": [],
    "tags": ["two_pointer", "array", "sorting"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Sort an array with n objects colored red, white, or blue, represented by 0, 1, and 2 respectively, in-place.",
}

def solve(nums: list[int]) -> None:
    """
    Sorts the input list in-place using the Dutch National Flag algorithm.

    The algorithm uses three pointers to partition the array into three sections:
    - Elements before 'low' are all 0s.
    - Elements between 'low' and 'mid' are all 1s.
    - Elements after 'high' are all 2s.

    Args:
        nums: A list of integers containing only 0, 1, and 2.

    Returns:
        None. The list is modified in-place.

    Examples:
        >>> nums = [2, 0, 2, 1, 1, 0]
        >>> solve(nums)
        >>> nums
        [0, 0, 1, 1, 2, 2]
    """
    low = 0
    mid = 0
    high = len(nums) - 1

    while mid <= high:
        if nums[mid] == 0:
            # If we find a 0, swap it with the element at the 'low' pointer.
            # Increment both low and mid because we know the swapped element is a 1 or 0.
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1
        elif nums[mid] == 1:
            # If we find a 1, it is already in the correct relative middle section.
            # Just move the mid pointer forward.
            mid += 1
        else:
            # If we find a 2, swap it with the element at the 'high' pointer.
            # Decrement high, but do NOT increment mid yet, because the new element 
            # swapped from 'high' to 'mid' needs to be evaluated.
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1
