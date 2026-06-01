METADATA = {
    "id": 1150,
    "name": "Check If a Number Is Majority Element in a Sorted Array",
    "slug": "check-if-a-number-is-majority-element-in-a-sorted-array",
    "category": "Binary Search",
    "aliases": [],
    "tags": ["binary_search", "arrays", "sorted_array"],
    "difficulty": "easy",
    "time_complexity": "O(log n)",
    "space_complexity": "O(1)",
    "description": "Determine if a target number appears more than n/2 times in a sorted array using binary search.",
}

def solve(nums: list[int], target: int) -> bool:
    """
    Checks if the target element is the majority element in a sorted array.
    A majority element is defined as an element that appears more than n/2 times.

    Args:
        nums: A sorted list of integers.
        target: The integer to check for majority status.

    Returns:
        True if target is the majority element, False otherwise.

    Examples:
        >>> solve([1, 2, 3, 3, 3, 3, 10], 3)
        True
        >>> solve([1, 2, 3, 3, 3, 10], 3)
        False
        >>> solve([1, 1, 1, 2, 2], 1)
        True
    """
    n = len(nums)
    
    # Find the first occurrence of the target using binary search
    first_index = find_first_occurrence(nums, target)
    
    # If target is not in the array, it cannot be the majority element
    if first_index == -1:
        return False
    
    # If target is the majority element, it must exist at the index 
    # (first_index + n // 2) because the array is sorted.
    # Example: n=7, n//2=3. If first_index=2, target must be at index 2+3=5.
    # Indices: [2, 3, 4, 5] -> 4 elements, which is > 7/2.
    check_index = first_index + n // 2
    
    return check_index < n and nums[check_index] == target

def find_first_occurrence(nums: list[int], target: int) -> int:
    """
    Helper function to find the leftmost index of the target in a sorted array.

    Args:
        nums: A sorted list of integers.
        target: The integer to search for.

    Returns:
        The smallest index i such that nums[i] == target, or -1 if not found.
    """
    low = 0
    high = len(nums) - 1
    result = -1
    
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == target:
            result = mid
            # Continue searching to the left to find the very first occurrence
            high = mid - 1
        elif nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
            
    return result
