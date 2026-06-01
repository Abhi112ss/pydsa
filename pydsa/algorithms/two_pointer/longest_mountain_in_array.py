METADATA = {
    "id": 845,
    "name": "Longest Mountain in Array",
    "slug": "longest-mountain-in-array",
    "category": "Array",
    "aliases": [],
    "tags": ["array", "two-pointers", "dynamic-programming"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the length of the longest subarray that forms a mountain shape.",
}

def solve(arr: list[int]) -> int:
    """
    Finds the length of the longest mountain in the given array.
    
    A mountain is defined as a subarray with length >= 3 that strictly increases 
    to a peak and then strictly decreases.

    Args:
        arr: A list of integers.

    Returns:
        The length of the longest mountain subarray. Returns 0 if no mountain exists.

    Examples:
        >>> solve([2, 1, 4, 7, 3, 2, 5])
        5
        >>> solve([2, 2, 2])
        0
        >>> solve([0, 1, 2, 3, 4, 5, 4, 3, 2, 1, 0])
        11
    """
    n = len(arr)
    max_mountain_length = 0
    
    # A mountain must have at least 3 elements.
    # We iterate from index 1 to n-2 because a peak cannot be at the boundaries.
    for i in range(1, n - 1):
        # Check if the current index is a peak
        if arr[i - 1] < arr[i] > arr[i + 1]:
            left = i - 1
            right = i + 1
            
            # Expand to the left as long as it is strictly decreasing towards the left
            while left > 0 and arr[left - 1] < arr[left]:
                left -= 1
                
            # Expand to the right as long as it is strictly decreasing towards the right
            while right < n - 1 and arr[right + 1] < arr[right]:
                right += 1
            
            # Calculate the current mountain length
            current_mountain_length = right - left + 1
            max_mountain_length = max(max_mountain_length, current_mountain_length)
            
    return max_mountain_length
