METADATA = {
    "id": 2872,
    "name": "Maximum Number of K-Divisible Components",
    "slug": "maximum-number-of-k-divisible-components",
    "category": "Arrays",
    "aliases": [],
    "tags": ["arrays", "greedy", "prefix sum"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the maximum number of non-empty contiguous subarrays such that the sum of each subarray is divisible by k.",
}

def solve(nums: list[int], k: int) -> int:
    """
    Calculates the maximum number of non-empty contiguous subarrays whose sums are divisible by k.

    The algorithm uses a greedy approach with prefix sums. A subarray sum from index i to j 
    is divisible by k if (prefix_sum[j] - prefix_sum[i-1]) % k == 0, which implies 
    prefix_sum[j] % k == prefix_sum[i-1] % k. By greedily cutting the array as soon 
    as we encounter a prefix sum modulo k that we have seen before (or is 0), 
    we maximize the number of components.

    Args:
        nums: A list of integers.
        k: The divisor.

    Returns:
        The maximum number of k-divisible components.

    Examples:
        >>> solve([4, 3, 2, 6], 3)
        3
        >>> solve([1, 2, 3, 4, 5], 2)
        2
    """
    count = 0
    current_prefix_sum_mod = 0
    
    # We use a set to track the prefix sum remainders encountered in the current segment.
    # When we find a remainder that has already appeared in the current segment,
    # it means the sum of the elements between these two points is divisible by k.
    # We then 'cut' the segment and reset.
    seen_remainders = {0}

    for num in nums:
        # Update the running prefix sum modulo k
        current_prefix_sum_mod = (current_prefix_sum_mod + num) % k
        
        # If this remainder has been seen before in the current segment,
        # we have found a k-divisible component.
        if current_prefix_sum_mod in seen_remainders:
            count += 1
            # Reset for the next potential component
            seen_remainders = {0}
            current_prefix_sum_mod = 0
        else:
            # Otherwise, add the current remainder to the set of seen remainders
            seen_remainders.add(current_prefix_sum_mod)

    return count
