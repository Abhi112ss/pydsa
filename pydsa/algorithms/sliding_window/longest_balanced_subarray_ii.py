METADATA = {
    "id": 3721,
    "name": "Longest Balanced Subarray II",
    "slug": "longest_balanced_subarray_ii",
    "category": "Array",
    "aliases": [],
    "tags": ["sliding_window", "prefix_sum", "hash_map"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Find the length of the longest subarray containing an equal number of two specific elements.",
}

def solve(nums: list[int], target_a: int, target_b: int) -> int:
    """
    Finds the length of the longest subarray that contains an equal number 
    of target_a and target_b.

    Args:
        nums: A list of integers.
        target_a: The first integer to balance.
        target_b: The second integer to balance.

    Returns:
        The length of the longest balanced subarray.

    Examples:
        >>> solve([1, 0, 1, 1, 0, 0, 1], 1, 0)
        6
        >>> solve([1, 1, 1], 1, 0)
        0
        >>> solve([0, 0, 1, 1, 0], 0, 1)
        4
    """
    # Map to store the first occurrence of a specific (count_a - count_b) difference.
    # Key: difference (count_a - count_b), Value: index where this difference first occurred.
    # Initialize with difference 0 at index -1 to handle subarrays starting from index 0.
    diff_map: dict[int, int] = {0: -1}
    
    max_length = 0
    count_a = 0
    count_b = 0
    
    for index, num in enumerate(nums):
        if num == target_a:
            count_a += 1
        elif num == target_b:
            count_b += 1
        
        # The core idea: if (count_a - count_b) is the same at two different indices,
        # the subarray between those indices has an equal number of target_a and target_b.
        current_diff = count_a - count_b
        
        if current_diff in diff_map:
            # Calculate the length of the subarray ending at the current index.
            subarray_length = index - diff_map[current_diff]
            if subarray_length > max_length:
                max_length = subarray_length
        else:
            # Store the first time we encounter this specific difference.
            diff_map[current_diff] = index
            
    return max_length
