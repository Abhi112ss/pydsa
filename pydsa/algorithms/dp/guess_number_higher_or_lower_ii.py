METADATA = {
    "id": 375,
    "name": "Guess Number Higher or Lower II",
    "slug": "guess-number-higher-or-lower-ii",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dynamic_programming", "minimax", "interval_dp"],
    "difficulty": "hard",
    "time_complexity": "O(n^3)",
    "space_complexity": "O(n^2)",
    "description": "Find the minimum amount of money you need to guarantee a win when guessing a number in a given range.",
}

def solve(n: int) -> int:
    """
    Calculates the minimum cost to guarantee a correct guess using minimax strategy.

    Args:
        n: The upper bound of the range [1, n].

    Returns:
        The minimum amount of money required to guarantee a win.

    Examples:
        >>> solve(10)
        16
        >>> solve(1)
        0
    """
    if n <= 1:
        return 0

    # dp[i][j] represents the minimum cost to guarantee a win for the range [i, j]
    # We use a size (n+2) x (n+2) to avoid index out of bounds for range boundaries
    dp = [[0] * (n + 2) for _ in range(n + 2)]

    # length is the size of the current range we are considering
    for length in range(2, n + 1):
        # left is the starting number of the range
        for left in range(1, n - length + 2):
            right = left + length - 1
            
            # Initialize with a very large value to find the minimum
            min_max_cost = float('inf')

            # Try every possible guess 'k' within the current range [left, right]
            for k in range(left, right + 1):
                # If we guess 'k', the worst case is the maximum of the costs 
                # of the two resulting sub-problems: [left, k-1] and [k+1, right]
                # We add 'k' because that is the cost of the current guess.
                current_cost = k + max(dp[left][k - 1], dp[k + 1][right])
                
                # We want to choose 'k' such that this worst-case cost is minimized
                if current_cost < min_max_cost:
                    min_max_cost = current_cost
            
            dp[left][right] = int(min_max_cost)

    return dp[1][n]
