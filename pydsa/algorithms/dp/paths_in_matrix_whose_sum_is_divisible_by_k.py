METADATA = {
    "id": 2435,
    "name": "Paths in Matrix Whose Sum Is Divisible by K",
    "slug": "paths-in-matrix-whose-sum-is-divisible-by-k",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dp", "graphs", "matrix"],
    "difficulty": "hard",
    "time_complexity": "O(m * n * k)",
    "space_complexity": "O(m * n * k)",
    "description": "Find the number of paths from the top-left to the bottom-right of a matrix such that the sum of elements in the path is divisible by k.",
}

def solve(grid: list[list[int]], k: int) -> int:
    """
    Calculates the number of paths from (0, 0) to (m-1, n-1) such that the 
    sum of elements along the path is divisible by k.

    Args:
        grid: A 2D list of integers representing the matrix.
        k: The divisor to check for path sums.

    Returns:
        The number of valid paths modulo 10^9 + 7.

    Examples:
        >>> solve([[1, 2, 3], [4, 5, 6]], 3)
        1
    """
    MOD = 1_000_000_007
    rows = len(grid)
    cols = len(grid[0])

    # dp[r][c][rem] stores the number of paths to cell (r, c) 
    # where the path sum modulo k is equal to 'rem'.
    dp = [[[0] * k for _ in range(cols)] for _ in range(rows)]

    # Base case: starting cell
    start_val = grid[0][0] % k
    dp[0][0][start_val] = 1

    for r in range(rows):
        for c in range(cols):
            for rem in range(k):
                if dp[r][c][rem] == 0:
                    continue
                
                current_count = dp[r][c][rem]

                # Move Right
                if c + 1 < cols:
                    next_rem = (rem + grid[r][c + 1]) % k
                    dp[r][c + 1][next_rem] = (dp[r][c + 1][next_rem] + current_count) % MOD

                # Move Down
                if r + 1 < rows:
                    next_rem = (rem + grid[r + 1][c]) % k
                    dp[r + 1][c][next_rem] = (dp[r + 1][c][next_rem] + current_count) % MOD

    # The answer is the number of paths reaching the bottom-right cell 
    # with a remainder of 0.
    return dp[rows - 1][cols - 1][0]
