from typing import List

METADATA = {
    "id": 3077,
    "name": "Maximum Strength of K Disjoint Subarrays",
    "slug": "maximum_strength_of_k_disjoint_subarrays",
    "category": "Dynamic Programming",
    "aliases": ["Maximum Strength"],
    "tags": ["dp", "arrays", "prefix-sum"],
    "difficulty": "hard",
    "time_complexity": "O(k * n)",
    "space_complexity": "O(n)",
    "description": "Find the maximum strength of k disjoint subarrays where strength is calculated with alternating signs and decreasing weights.",
}

def solve(nums: list[int], k: int) -> int:
    """
    Calculates the maximum strength of k disjoint subarrays using dynamic programming.
    
    The strength is defined as:
    strength = x_1 * w_1 - x_2 * w_2 + x_3 * w_3 - ... + (-1)^{k-1} * x_k * w_k
    where x_i is the sum of the i-th subarray and w_i = k - i + 1.
    
    Args:
        nums: A list of integers.
        k: The number of disjoint subarrays to select.
        
    Returns:
        The maximum possible strength.
        
    Examples:
        >>> solve([1, 2, 3, -1, 2], 3)
        22
        >>> solve([-1, -2, -3], 1)
        -1
    """
    n = len(nums)
    
    # Precompute prefix sums for O(1) subarray sum calculation
    prefix_sums = [0] * (n + 1)
    for i in range(n):
        prefix_sums[i + 1] = prefix_sums[i] + nums[i]
        
    # dp[j] stores the maximum strength using i subarrays from the first j elements.
    # We use O(n) space by updating the dp array for each i from 1 to k.
    dp = [0] * (n + 1)
    
    # Large negative constant for initialization
    INF = float('inf')
    
    for i in range(1, k + 1):
        # Weight for the current subarray: (-1)^(i-1) * (k - i + 1)
        weight = (k - i + 1) if i % 2 == 1 else -(k - i + 1)
        
        # next_dp will store values for the current i
        next_dp = [-INF] * (n + 1)
        
        # best_prev tracks max(dp[p] - prefix_sums[p] * weight) for p < j
        # This allows us to find the best starting point for the i-th subarray in O(1)
        best_prev = -INF
        
        # The i-th subarray must end at least at index i and leave room for k-i subarrays
        for j in range(i, n - (k - i) + 1):
            # Update best_prev using the result from (i-1) subarrays ending before j
            # dp[j-1] is the max strength using i-1 subarrays from first j-1 elements
            best_prev = max(best_prev, dp[j - 1] - prefix_sums[j - 1] * weight)
            
            # next_dp[j] is either:
            # 1. The max strength using i subarrays from first j-1 elements (skip nums[j-1])
            # 2. The max strength where the i-th subarray ends at index j
            next_dp[j] = max(next_dp[j - 1], prefix_sums[j] * weight + best_prev)
            
        dp = next_dp
        
    return dp[n]