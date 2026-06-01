METADATA = {
    "id": 3865,
    "name": "Reverse K Subarrays",
    "slug": "reverse_k_subarrays",
    "category": "Array",
    "aliases": [],
    "tags": ["array", "sliding_window"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Reverse every contiguous subarray of size k within the given array.",
}

def solve(nums: list[int], k: int) -> list[int]:
    """
    Reverses every contiguous subarray of size k in the input list.
    
    If the length of the array is not a multiple of k, the remaining 
    elements at the end (the last partial subarray) are also reversed.

    Args:
        nums: A list of integers to be processed.
        k: The size of the subarrays to reverse.

    Returns:
        A new list containing the elements after reversing each k-sized subarray.

    Examples:
        >>> solve([1, 2, 3, 4, 5, 6], 3)
        [3, 2, 1, 6, 5, 4]
        >>> solve([1, 2, 3, 4, 5], 2)
        [2, 1, 4, 3, 5]
        >>> solve([1, 2, 3, 4, 5], 3)
        [3, 2, 1, 5, 4]
    """
    if not nums:
        return []
    
    n = len(nums)
    # Create a copy to avoid mutating the original input if required by caller
    result = list(nums)
    
    # Iterate through the array in steps of k
    for start_index in range(0, n, k):
        # Determine the end of the current window
        # The window might be smaller than k if we are at the end of the array
        end_index = min(start_index + k, n)
        
        # Perform an in-place reversal of the current window [start_index, end_index)
        left = start_index
        right = end_index - 1
        
        while left < right:
            result[left], result[right] = result[right], result[left]
            left += 1
            right -= 1
            
    return result
