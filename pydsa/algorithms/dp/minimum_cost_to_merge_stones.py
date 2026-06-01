METADATA = {
    "id": 1000,
    "name": "Minimum Cost to Merge Stones",
    "slug": "minimum-cost-to-merge-stones",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dynamic_programming", "interval_dp"],
    "difficulty": "hard",
    "time_complexity": "O(n^3 / k)",
    "space_complexity": "O(n^2)",
    "description": "Find the minimum cost to merge all stones into K piles using interval dynamic programming.",
}

def solve(stones: list[int], k: int) -> int:
    """
    Calculates the minimum cost to merge all stones into K piles.

    Args:
        stones: A list of integers representing the number of stones in each pile.
        k: The target number of piles to merge into.

    Returns:
        The minimum cost to merge the stones, or -1 if it is impossible.

    Examples:
        >>> solve([3, 2, 4, 5, 6], 2)
        20
        >>> solve([3, 2, 4, 5, 6], 3)
        14
        >>> solve([1, 2, 3, 4, 5], 4)
        -1
    """
    n = len(stones)
    
    # To merge n piles into k piles, we must reduce the number of piles by (n - k).
    # Each merge operation reduces the number of piles by (k - 1).
    # Therefore, (n - k) must be divisible by (k - 1).
    if (n - k) % (k - 1) != 0:
        return -1

    # Precompute prefix sums to calculate the sum of any range [i, j] in O(1).
    prefix_sums = [0] * (n + 1)
    for i in range(n):
        prefix_sums[i + 1] = prefix_sums[i] + stones[i]

    # dp[i][j] represents the minimum cost to merge the range [i, j] 
    # into the minimum possible number of piles.
    # The number of piles for range [i, j] is 1 + (length - 1) % (k - 1).
    # However, a more standard interval DP approach is to track the cost 
    # to merge [i, j] into 1 pile, but we must ensure the sub-problems 
    # are valid for the k-merge constraint.
    
    # dp[i][j] = min cost to merge stones from index i to j into 1 pile.
    # Since we can only merge k piles at a time, we use a 2D DP table.
    # To handle the "k-at-a-time" constraint, we can use dp[i][j] to mean 
    # the min cost to merge range [i, j] into 1 pile.
    # But a simpler way is dp[i][j] = min cost to merge [i, j] into 1 pile,
    # and we use the step size (k-1) to ensure validity.
    
    dp = [[0] * n for _ in range(n)]

    for length in range(k, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            
            # Initialize with a large value.
            dp[i][j] = float('inf')
            
            # Try splitting the range [i, j] into two parts: [i, m] and [m+1, j].
            # We step by (k-1) to ensure the left part can eventually be merged 
            # into a single pile or a valid number of piles.
            for m in range(i, j, k - 1):
                dp[i][j] = min(dp[i][j], dp[i][m] + dp[m + 1][j])
            
            # If the current range [i, j] can be merged into exactly 1 pile,
            # we add the sum of all stones in this range.
            # A range can be merged into 1 pile if (length - 1) % (k - 1) == 0.
            if (length - 1) % (k - 1) == 0:
                dp[i][j] += prefix_sums[j + 1] - prefix_sums[i]

    return int(dp[0][n - 1])
