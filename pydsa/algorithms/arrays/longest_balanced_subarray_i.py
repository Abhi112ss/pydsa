METADATA = {
    "id": 3719,
    "name": "Longest Balanced Subarray I",
    "slug": "longest_balanced_subarray_i",
    "category": "Array",
    "aliases": [],
    "tags": ["prefix_sum", "hash_map"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Find the length of the longest subarray where the number of 0s and 1s are equal.",
}

def solve(nums: list[int]) -> int:
    """
    Finds the length of the longest subarray containing an equal number of 0s and 1s.

    Args:
        nums: A list of integers containing only 0s and 1s.

    Returns:
        The length of the longest balanced subarray.

    Examples:
        >>> solve([0, 1])
        2
        >>> solve([0, 1, 0])
        2
        >>> solve([0, 0, 0, 1, 1])
        4
    """
    # To treat 0s and 1s equally, we transform 0s into -1s.
    # A balanced subarray will then have a sum of 0.
    
    # Map to store the first occurrence of a prefix sum.
    # Key: prefix_sum, Value: index
    # Initialize with {0: -1} to handle subarrays starting from index 0.
    first_occurrence: dict[int, int] = {0: -1}
    
    current_sum = 0
    max_length = 0
    
    for index, value in enumerate(nums):
        # Treat 0 as -1 so that equal counts of 0 and 1 sum to 0
        current_sum += 1 if value == 1 else -1
        
        if current_sum in first_occurrence:
            # If this sum has been seen before, the subarray between 
            # the previous index and current index has a sum of 0.
            subarray_length = index - first_occurrence[current_sum]
            if subarray_length > max_length:
                max_length = subarray_length
        else:
            # Store the first time we encounter this specific prefix sum
            first_occurrence[current_sum] = index
            
    return max_length
