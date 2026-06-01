METADATA = {
    "id": 1574,
    "name": "Shortest Subarray to be Removed to Make Array Sorted",
    "slug": "shortest-subarray-to-be-removed-to-make-array-sorted",
    "category": "Array",
    "aliases": [],
    "tags": ["two_pointer", "binary_search"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the length of the shortest subarray to remove such that the remaining elements are in non-decreasing order.",
}

def solve(arr: list[int]) -> int:
    """
    Finds the length of the shortest subarray to remove to make the remaining array sorted.

    The strategy is to identify the longest non-decreasing prefix and the longest 
    non-decreasing suffix. Then, we attempt to bridge a part of the prefix with 
    a part of the suffix using a two-pointer approach to find the minimum removal.

    Args:
        arr: A list of integers.

    Returns:
        The length of the shortest subarray to be removed.

    Examples:
        >>> solve([1, 2, 3, 4])
        0
        >>> solve([1, 2, 3, 1, 1])
        1
        >>> solve([1, 4, 3, 2])
        2
    """
    n = len(arr)
    
    # 1. Find the longest non-decreasing prefix
    left_end = 0
    while left_end + 1 < n and arr[left_end] <= arr[left_end + 1]:
        left_end += 1
        
    # If the entire array is already sorted
    if left_end == n - 1:
        return 0
        
    # 2. Find the longest non-decreasing suffix
    right_start = n - 1
    while right_start > 0 and arr[right_start - 1] <= arr[right_start]:
        right_start -= 1
        
    # Initial answer: either remove everything after prefix or everything before suffix
    # This covers cases where we only keep a part of the prefix or a part of the suffix
    min_removal = min(n - 1 - left_end, right_start)
    
    # 3. Use two pointers to bridge prefix and suffix
    # We try to keep arr[0...i] and arr[j...n-1] such that arr[i] <= arr[j]
    i = 0
    j = right_start
    while i <= left_end and j < n:
        if arr[i] <= arr[j]:
            # If valid, the elements to remove are those between index i and j
            # The number of elements removed is j - i - 1
            min_removal = min(min_removal, j - i - 1)
            i += 1
        else:
            # If arr[i] > arr[j], we need a larger arr[j] to satisfy the condition
            j += 1
            
    return min_removal
