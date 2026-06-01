METADATA = {
    "id": 525,
    "name": "Contiguous Array",
    "slug": "contiguous-array",
    "category": "Array",
    "aliases": [],
    "tags": ["hash_map", "prefix_sum"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Find the maximum length of a contiguous subarray with an equal number of 0 and 1.",
}

def solve(nums: list[int]) -> int:
    """
    Finds the maximum length of a contiguous subarray with an equal number of 0s and 1s.

    The algorithm transforms the problem by treating 0 as -1. An equal number of 0s and 1s
    then corresponds to a subarray whose sum is 0. We use a prefix sum approach combined
    with a hash map to track the first occurrence of each prefix sum.

    Args:
        nums: A list of integers containing only 0s and 1s.

    Returns:
        The maximum length of a contiguous subarray with an equal number of 0s and 1s.

    Examples:
        >>> solve([0, 1])
        2
        >>> solve([0, 1, 0])
        2
        >>> solve([0, 0, 1, 1, 0])
        4
    """
    # Map to store the first occurrence of a prefix sum: {prefix_sum: index}
    # Initialize with {0: -1} to handle cases where the subarray starts from index 0
    prefix_sum_map: dict[int, int] = {0: -1}
    
    current_sum = 0
    max_length = 0
    
    for index, num in enumerate(nums):
        # Treat 0 as -1 so that an equal number of 0s and 1s results in a sum of 0
        current_sum += 1 if num == 1 else -1
        
        if current_sum in prefix_sum_map:
            # If this sum has been seen before, the subarray between the previous 
            # occurrence and the current index has a net sum of 0.
            subarray_length = index - prefix_sum_map[current_sum]
            if subarray_length > max_length:
                max_length = subarray_length
        else:
            # Store only the first occurrence to ensure we find the longest possible subarray
            prefix_sum_map[current_sum] = index
            
    return max_length
