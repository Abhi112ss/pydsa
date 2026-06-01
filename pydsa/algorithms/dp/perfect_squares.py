METADATA = {
    "id": 279,
    "name": "Perfect Squares",
    "slug": "perfect-squares",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dynamic_programming", "math", "bfs"],
    "difficulty": "medium",
    "time_complexity": "O(n * sqrt(n))",
    "space_complexity": "O(n)",
    "description": "Find the least number of perfect square numbers that sum to a given integer n.",
}

def solve(n: int) -> int:
    """
    Finds the minimum number of perfect square numbers that sum up to n.

    This implementation uses Dynamic Programming. We define dp[i] as the 
    minimum number of perfect squares that sum to i. For each i, we iterate 
    through all perfect squares j*j <= i and update dp[i] = min(dp[i], dp[i - j*j] + 1).

    Args:
        n: The target integer.

    Returns:
        The least number of perfect square numbers that sum to n.

    Examples:
        >>> solve(12)
        3
        >>> solve(13)
        2
    """
    if n <= 0:
        return 0

    # Initialize DP table with infinity, dp[0] is 0 because 0 requires 0 squares.
    # dp[i] stores the minimum number of perfect squares that sum to i.
    dp = [float('inf')] * (n + 1)
    dp[0] = 0

    # Pre-calculate possible perfect squares to avoid repeated multiplication
    # in the inner loop, though j*j is also efficient.
    for i in range(1, n + 1):
        j = 1
        while j * j <= i:
            # The recurrence relation:
            # To reach sum 'i', we can take a perfect square 'j*j' 
            # and add it to the optimal solution for 'i - j*j'.
            if dp[i - j * j] + 1 < dp[i]:
                dp[i] = dp[i - j * j] + 1
            j += 1

    return int(dp[n])
