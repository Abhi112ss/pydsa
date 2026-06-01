METADATA = {
    "id": 540,
    "name": "Single Element in a Sorted Array",
    "slug": "single-element-in-a-sorted-array",
    "category": "Binary Search",
    "aliases": [],
    "tags": ["binary_search", "array", "sorted"],
    "difficulty": "medium",
    "time_complexity": "O(log n)",
    "space_complexity": "O(1)",
    "description": "Find the single element in a sorted array where every other element appears exactly twice.",
}

def solve(nums: list[int]) -> int:
    """
    Finds the single element in a sorted array where every other element appears twice.

    The algorithm uses binary search to find the index of the unique element. 
    In a sorted array where elements come in pairs, for any pair (nums[i], nums[i+1]), 
    the first element of the pair should be at an even index and the second at an odd index.
    If this property is violated, the single element must be at or before the current index.

    Args:
        nums: A list of integers where every element appears twice except for one.

    Returns:
        The single element that appears only once in the array.

    Examples:
        >>> solve([1, 1, 2, 3, 3, 4, 4, 8, 8])
        2
        >>> solve([3, 3, 7, 7, 10, 11, 11])
        10
    """
    low = 0
    high = len(nums) - 1

    while low < high:
        mid = low + (high - low) // 2

        # Ensure mid is even to check the pair starting at mid.
        # If mid is odd, decrement it to make it the start of a potential pair.
        if mid % 2 == 1:
            mid -= 1

        # If the element at mid and mid + 1 are the same, the single element
        # must be located in the right half of the array.
        if nums[mid] == nums[mid + 1]:
            low = mid + 2
        else:
            # Otherwise, the single element is either at mid or to the left.
            high = mid

    return nums[low]
