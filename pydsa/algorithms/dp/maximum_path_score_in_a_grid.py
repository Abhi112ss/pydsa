METADATA = {
    "id": 3742,
    "name": "Maximum Path Score in a Grid",
    "slug": "maximum-path-score-in-a-grid",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dynamic_programming", "matrix", "grid"],
    "difficulty": "medium",
    "time_complexity": "O(m * n)",
    "space_complexity": "O(m * n)",
    "description": "Find the maximum path score from the top-left to the bottom-right of a grid where you can move right or down.",
}

def solve(grid: list[list[int]]) -> int:
    """
    Calculates the maximum path score from the top-left cell to the bottom-right cell.
    Movement is restricted to only moving right or down.

    Args:
        grid: A 2D list of integers representing the scores in each cell.

    Returns:
        The maximum possible sum of scores along a path from (0, 0) to (m-1, n-1).

    Examples:
        >>> solve([[1, 3, 1], [1, 5, 1], [4, 2, 1]])
        12
        >>> solve([[1, 1], [1, 1]])
        2
    """
    if not grid or not grid[0]:
        return 0

    rows = len(grid)
    cols = len(grid[0])

    # dp[i][j] stores the maximum score to reach cell (i, j)
    dp = [[0] * cols for _ in range(rows)]

    # Initialize the starting point
    dp[0][0] = grid[0][0]

    # Initialize the first row (can only come from the left)
    for j in range(1, cols):
        dp[0][j] = dp[0][j - 1] + grid[0][j]

    # Initialize the first column (can only come from above)
    for i in range(1, rows):
        dp[i][0] = dp[i - 1][0] + grid[i][0]

    # Fill the rest of the DP table
    for i in range(1, rows):
        for j in range(1, cols):
            # The max score at current cell is the cell's value plus 
            # the maximum of the score from the cell above or the cell to the left
            dp[i][j] = grid[i][j] + max(dp[i - 1][j], dp[i][j - 1])

    return dp[rows - 1][cols - 1]
