METADATA = {
    "id": 560,
    "name": "Subarray Sum Equals K",
    "slug": "subarray-sum-equals-k",
    "category": "Array",
    "aliases": [],
    "tags": ["hash_map", "prefix_sum"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Find the total number of continuous subarrays whose sum equals a given integer k.",
}

def solve(nums: list[int], k: int) -> int:
    """
    Calculates the total number of continuous subarrays that sum up to k.

    Args:
        nums: A list of integers.
        k: The target sum.

    Returns:
        The total count of subarrays that sum to k.

    Examples:
        >>> solve([1, 1, 1], 2)
        2
        >>> solve([1, 2, 3], 3)
        2
    """
    # prefix_sum_counts stores how many times a specific prefix sum has occurred.
    # We initialize it with {0: 1} to account for subarrays starting from index 0.
    prefix_sum_counts: dict[int, int] = {0: 1}
    
    current_running_sum: int = 0
    total_subarrays_found: int = 0

    for num in nums:
        current_running_sum += num
        
        # If (current_running_sum - k) exists in our map, it means there is a 
        # prefix that, when removed from the current prefix, results in a sum of k.
        target_difference = current_running_sum - k
        if target_difference in prefix_sum_counts:
            total_subarrays_found += prefix_sum_counts[target_difference]
            
        # Update the frequency of the current prefix sum in the hash map.
        prefix_sum_counts[current_running_sum] = prefix_sum_counts.get(current_running_sum, 0) + 1

    return total_subarrays_found
