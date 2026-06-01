METADATA = {
    "id": 3797,
    "name": "Count Routes to Climb a Rectangular Grid",
    "slug": "count-routes-to-climb-a-rectangular-grid",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dp", "math", "grid"],
    "difficulty": "medium",
    "time_complexity": "O(m * n)",
    "space_complexity": "O(n)",
    "description": "Calculate the number of unique paths from the top-left to the bottom-right of a grid using dynamic programming.",
}

def solve(rows: int, cols: int, mod: int) -> int:
    """
    Calculates the number of unique paths from (0, 0) to (rows-1, cols-1) 
    in a rectangular grid, moving only right or down.

    Args:
        rows: The number of rows in the grid.
        cols: The number of columns in the grid.
        mod: The modulo value to prevent integer overflow.

    Returns:
        The total number of unique routes modulo the given mod.

    Examples:
        >>> solve(3, 3, 10**9 + 7)
        6
        >>> solve(2, 2, 10**9 + 7)
        2
    """
    if rows == 0 or cols == 0:
        return 0

    # We use a 1D array to optimize space from O(m*n) to O(n).
    # dp[j] represents the number of ways to reach the current cell in column j.
    dp = [0] * cols
    
    # Base case: There is exactly 1 way to reach any cell in the first row (moving only right).
    for j in range(cols):
        dp[j] = 1

    # Iterate through each row starting from the second row.
    for i in range(1, rows):
        # For the first column of every row, there is only 1 way (moving only down).
        # dp[0] remains 1 from the previous row's logic or is explicitly set.
        # However, since we update dp in place, dp[0] is already the value from the cell above.
        
        for j in range(1, cols):
            # The number of ways to reach cell (i, j) is:
            # ways(i-1, j) [value currently in dp[j]] + ways(i, j-1) [value in dp[j-1]]
            dp[j] = (dp[j] + dp[j - 1]) % mod

    return dp[cols - 1]
