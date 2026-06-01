METADATA = {
    "id": 3381,
    "name": "Maximum Subarray Sum With Length Divisible by K",
    "slug": "maximum-subarray-sum-with-length-divisible-by-k",
    "category": "Array",
    "aliases": [],
    "tags": ["prefix_sum", "sliding_window", "modulo"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(k)",
    "description": "Find the maximum sum of a subarray whose length is a multiple of k.",
}

def solve(nums: list[int], k: int) -> int:
    """
    Calculates the maximum sum of a subarray whose length is divisible by k.

    Args:
        nums: A list of integers.
        k: The divisor for the subarray length.

    Returns:
        The maximum sum found.

    Examples:
        >>> solve([1, -2, 3, 4, -5, 6], 2)
        7
        >>> solve([-1, -2, -3, -4], 2)
        -3
    """
    n = len(nums)
    # prefix_sum[i] stores the sum of nums[0...i-1]
    prefix_sum = [0] * (n + 1)
    for i in range(n):
        prefix_sum[i + 1] = prefix_sum[i] + nums[i]

    # To ensure length (j - i) is divisible by k, we need i % k == j % k.
    # We want to maximize (prefix_sum[j] - prefix_sum[i]) where j % k == i % k.
    # This is equivalent to maximizing prefix_sum[j] - min(prefix_sum[i]) 
    # for all i < j such that i % k == j % k.
    
    # min_prefix_at_mod[r] stores the minimum prefix_sum[i] encountered 
    # so far where i % k == r.
    min_prefix_at_mod = [float('inf')] * k
    max_sum = float('-inf')

    for j in range(n + 1):
        remainder = j % k
        
        # If we have seen a prefix sum with the same remainder before,
        # the subarray from that index to j has a length divisible by k.
        if min_prefix_at_mod[remainder] != float('inf'):
            current_sum = prefix_sum[j] - min_prefix_at_mod[remainder]
            if current_sum > max_sum:
                max_sum = current_sum
        
        # Update the minimum prefix sum for this remainder to be used for future j's.
        # Note: We update after checking max_sum to ensure length > 0 if k > 0,
        # though for length divisible by k, length 0 is technically divisible by k.
        # However, standard subarray problems usually imply length >= k.
        # Since j-i must be a multiple of k, and we want max sum, 
        # if k=2, j=2, i=0 is valid.
        if prefix_sum[j] < min_prefix_at_mod[remainder]:
            min_prefix_at_mod[remainder] = prefix_sum[j]

    return int(max_sum)
