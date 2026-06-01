METADATA = {
    "id": 3850,
    "name": "Count Sequences to K",
    "slug": "count_sequences_to_k",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dp", "math", "combinatorics"],
    "difficulty": "medium",
    "time_complexity": "O(k * n)",
    "space_complexity": "O(k)",
    "description": "Find the number of sequences of length n using elements from a given set that sum up to exactly k.",
}

def solve(n: int, k: int, elements: list[int]) -> int:
    """
    Calculates the number of sequences of length n using elements from the 
    provided list that sum up to exactly k.

    The problem is solved using dynamic programming where dp[i][j] represents 
    the number of sequences of length i that sum to j. To optimize space, 
    we use a 1D array since the state for length i only depends on length i-1.

    Args:
        n: The required length of the sequence.
        k: The target sum.
        elements: A list of available integers to use in the sequence.

    Returns:
        The total number of valid sequences.

    Examples:
        >>> solve(2, 4, [1, 2, 3])
        3
        # Sequences: (1, 3), (2, 2), (3, 1)
        
        >>> solve(3, 5, [1, 2])
        3
        # Sequences: (1, 2, 2), (2, 1, 2), (2, 2, 1)
    """
    # MOD is often required in these problems to prevent overflow, 
    # though not explicitly stated in the prompt, we assume standard large integer handling.
    # If the problem specifies a modulo, it should be applied here.
    MOD = 10**9 + 7

    # dp[s] will store the number of ways to get sum 's' using 'i' elements.
    # We initialize dp[0] = 1 because there is 1 way to get sum 0 with 0 elements.
    dp = [0] * (k + 1)
    dp[0] = 1

    # We iterate through the number of elements we are adding to the sequence.
    for _ in range(n):
        # next_dp will store the counts for the current sequence length.
        next_dp = [0] * (k + 1)
        
        # For every possible sum achieved by the previous (i-1) elements...
        for current_sum in range(k + 1):
            if dp[current_sum] == 0:
                continue
            
            # ...try adding each available element to the sequence.
            for element in elements:
                new_sum = current_sum + element
                if new_sum <= k:
                    # Update the count for the new sum.
                    next_dp[new_sum] = (next_dp[new_sum] + dp[current_sum]) % MOD
        
        # Move to the next length iteration.
        dp = next_dp

    return dp[k]
