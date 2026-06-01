METADATA = {
    "id": 3934,
    "name": "Smallest Unique Subarray",
    "slug": "smallest_unique_subarray",
    "category": "Sliding Window",
    "aliases": [],
    "tags": ["sliding_window", "hash_map"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Find the length of the smallest subarray that contains all unique elements present in the original array.",
}

def solve(nums: list[int]) -> int:
    """
    Finds the length of the smallest subarray that contains all unique elements 
    present in the input array.

    Args:
        nums: A list of integers.

    Returns:
        The length of the smallest subarray containing all unique elements. 
        Returns 0 if the input list is empty.

    Examples:
        >>> solve([1, 2, 1, 3, 2])
        3
        >>> solve([1, 1, 1])
        1
        >>> solve([1, 2, 3, 4, 5])
        5
    """
    if not nums:
        return 0

    # Identify the total number of unique elements in the entire array
    unique_elements_count = len(set(nums))
    
    # If all elements are the same, the smallest subarray is length 1
    if unique_elements_count <= 1:
        return 1 if nums else 0

    # Frequency map to track elements within the current sliding window
    window_counts: dict[int, int] = {}
    # Number of distinct elements currently in the window
    distinct_in_window = 0
    
    min_length = float('inf')
    left = 0

    # Expand the right boundary of the window
    for right in range(len(nums)):
        current_val = nums[right]
        
        # Update frequency map and distinct count
        if window_counts.get(current_val, 0) == 0:
            distinct_in_window += 1
        window_counts[current_val] = window_counts.get(current_val, 0) + 1

        # When the window contains all unique elements, try to shrink it from the left
        while distinct_in_window == unique_elements_count:
            # Update the minimum length found so far
            current_window_size = right - left + 1
            if current_window_size < min_length:
                min_length = current_window_size
            
            # Shrink the window from the left
            left_val = nums[left]
            window_counts[left_val] -= 1
            if window_counts[left_val] == 0:
                distinct_in_window -= 1
            
            left += 1

    return int(min_length) if min_length != float('inf') else 0
