METADATA = {
    "id": 903,
    "name": "Valid Permutations for DI Sequence",
    "slug": "valid-permutations-for-di-sequence",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dynamic_programming", "math"],
    "difficulty": "hard",
    "time_complexity": "O(n^2)",
    "space_complexity": "O(n)",
    "description": "Count the number of permutations of length n that satisfy a given DI sequence.",
}

def solve(s: str) -> int:
    """
    Calculates the number of permutations of length n that satisfy the DI sequence.
    
    The problem is solved using dynamic programming. We maintain a DP table where 
    dp[j] represents the number of valid permutations of the current length 
    ending with the j-th smallest available element.

    Args:
        s: A string consisting of 'I' (increase) and 'D' (decrease).

    Returns:
        The total number of valid permutations modulo 10^9 + 7.

    Examples:
        >>> solve("IDID")
        16
        >>> solve("III")
        1
        >>> solve("DDD")
        1
    """
    MOD = 10**9 + 7
    n = len(s) + 1
    
    # dp[j] stores the number of valid permutations of length 'i' 
    # where the last element added was the j-th smallest among available elements.
    # Base case: for length 1, there is 1 way to have a permutation ending in rank 0.
    dp = [0] * n
    dp[0] = 1
    
    for i in range(n - 1):
        new_dp = [0] * n
        # Precompute prefix sums to optimize the transition from O(n^3) to O(n^2)
        prefix_sum = [0] * (n + 1)
        for k in range(n):
            prefix_sum[k + 1] = (prefix_sum[k] + dp[k]) % MOD
            
        char = s[i]
        if char == 'I':
            # If 'I', the current element must be greater than the previous.
            # If the previous element had rank 'prev_rank', the new element 
            # must have rank 'curr_rank' such that curr_rank > prev_rank.
            # However, because we are using relative ranks, when we insert a new 
            # element, the ranks of existing elements shift.
            # For 'I', the new element's rank j must be > previous rank k.
            # In the relative rank DP, this means: new_dp[j] = sum(dp[k] for k < j)
            for j in range(n):
                new_dp[j] = prefix_sum[j]
        else:
            # If 'D', the current element must be smaller than the previous.
            # For 'D', the new element's rank j must be <= previous rank k.
            # In the relative rank DP, this means: new_dp[j] = sum(dp[k] for k >= j)
            # We use the prefix sum to calculate the suffix sum efficiently.
            for j in range(n):
                # sum(dp[k] for k from j to i)
                new_dp[j] = (prefix_sum[n] - prefix_sum[j]) % MOD
        
        dp = new_dp

    # The answer is the sum of all valid permutations of length n
    return sum(dp) % MOD
