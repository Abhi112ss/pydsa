METADATA = {
    "id": 1546,
    "name": "Maximum Number of Non-Overlapping Subarrays With Sum Equals Target",
    "slug": "maximum-number-of-non-overlapping-subarrays-with-sum-equals-target",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["prefix_sum", "greedy", "hash_map"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Find the maximum number of non-overlapping subarrays that sum up to a given target using a greedy approach with prefix sums.",
}

def solve(nums: list[int], target: int) -> int:
    """
    Calculates the maximum number of non-overlapping subarrays that sum to target.

    The algorithm uses a greedy approach: as soon as we find a subarray that 
    sums to the target, we count it and "reset" our search to ensure 
    non-overlapping property. We use a hash set to track prefix sums 
    encountered since the last valid subarray was found.

    Args:
        nums: A list of integers.
        target: The target sum for each subarray.

    Returns:
        The maximum number of non-overlapping subarrays.

    Examples:
        >>> solve([1, 1, 1, 1, 1], 2)
        2
        >>> solve([-1, 3, 5, 1, 4, 2, -9], 6)
        2
    """
    count = 0
    current_prefix_sum = 0
    
    # seen_prefix_sums stores prefix sums encountered since the last 
    # successful subarray was identified. We initialize with 0 to 
    # handle cases where a subarray starting from the current 'start' 
    # index sums exactly to target.
    seen_prefix_sums = {0}

    for num in nums:
        current_prefix_sum += num
        
        # If (current_prefix_sum - target) exists in our set, it means 
        # there is a subarray ending at the current index that sums to target.
        if (current_prefix_sum - target) in seen_prefix_sums:
            count += 1
            # Greedy step: Reset the search to ensure non-overlapping.
            # We clear the set and start fresh from the next index.
            seen_prefix_sums = {0}
            current_prefix_sum = 0
        else:
            # Otherwise, record the current prefix sum to check for 
            # future subarrays.
            seen_prefix_sums.add(current_prefix_sum)

    return count
