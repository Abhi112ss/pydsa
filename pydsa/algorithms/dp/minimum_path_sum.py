METADATA = {
    "id": 64,
    "name": "Minimum Path Sum",
    "slug": "minimum-path-sum",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dynamic_programming", "matrix", "grid"],
    "difficulty": "medium",
    "time_complexity": "O(m*n)",
    "space_complexity": "O(n)",
    "description": "Find a path from top left to bottom right of a grid which minimizes the sum of all numbers along its path.",
}

def solve(grid: list[list[int]]) -> int:
    """
    Calculates the minimum path sum from the top-left corner to the bottom-right corner.

    The algorithm uses dynamic programming with space optimization. Instead of a 
    full 2D table, we maintain a 1D array representing the current row being processed.

    Args:
        grid: A 2D list of integers representing the cost of each cell.

    Returns:
        The minimum sum of a path from top-left to bottom-right.

    Examples:
        >>> solve([[1,3,1],[1,5,1],[4,2,1]])
        7
        >>> solve([[1,2,3],[4,5,6]])
        12
    """
    if not grid or not grid[0]:
        return 0

    rows = len(grid)
    cols = len(grid[0])

    # dp array stores the minimum path sum to reach each column in the current row.
    # We initialize it with a size equal to the number of columns.
    dp = [0] * cols

    for r in range(rows):
        for c in range(cols):
            if r == 0 and c == 0:
                # Base case: starting cell
                dp[c] = grid[r][c]
            elif r == 0:
                # Top row: can only come from the left
                dp[c] = dp[c - 1] + grid[r][c]
            elif c == 0:
                # Leftmost column: can only come from above
                # dp[c] currently holds the value from the previous row (above)
                dp[c] = dp[c] + grid[r][c]
            else:
                # General case: minimum of coming from above (dp[c]) or left (dp[c-1])
                dp[c] = min(dp[c], dp[c - 1]) + grid[r][c]

    return dp[cols - 1]
