METADATA = {
    "id": 629,
    "name": "K Inverse Pairs Array",
    "slug": "k-inverse-pairs-array",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dynamic_programming", "prefix_sum", "math"],
    "difficulty": "hard",
    "time_complexity": "O(n * k)",
    "space_complexity": "O(k)",
    "description": "Calculate the number of permutations of n elements that have exactly k inverse pairs.",
}

def solve(n: int, k: int) -> int:
    """
    Calculates the number of permutations of n elements that have exactly k inverse pairs.
    
    The recurrence relation used is:
    dp[i][j] = sum(dp[i-1][j-m] for m in range(min(j, i-1) + 1))
    
    This can be optimized using a sliding window/prefix sum approach:
    dp[i][j] = dp[i][j-1] + dp[i-1][j] - dp[i-1][j-i]
    
    Args:
        n: The number of elements in the permutation.
        k: The target number of inverse pairs.
        
    Returns:
        The number of permutations with exactly k inverse pairs.
        
    Examples:
        >>> solve(3, 1)
        2
        >>> solve(3, 2)
        2
        >>> solve(4, 3)
        6
    """
    MOD = 10**9 + 7

    # dp[j] will store the number of permutations of 'i' elements with 'j' inverse pairs.
    # We use a 1D array to optimize space from O(n*k) to O(k).
    dp = [0] * (k + 1)
    dp[0] = 1

    for i in range(1, n + 1):
        new_dp = [0] * (k + 1)
        current_sum = 0
        
        # We use a sliding window sum to calculate the new DP values in O(k)
        # for each 'i', instead of O(k * i).
        for j in range(k + 1):
            # Add the current dp[i-1][j] to the sliding window sum
            current_sum += dp[j]
            
            # If the window size exceeds the number of possible inversions 
            # the i-th element can contribute (which is i-1), subtract the oldest element.
            if j >= i:
                current_sum -= dp[j - i]
            
            # Ensure the sum stays within modulo bounds
            new_dp[j] = current_sum % MOD
            
        dp = new_dp

    return dp[k]
