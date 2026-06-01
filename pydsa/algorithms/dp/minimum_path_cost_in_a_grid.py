METADATA = {
    "id": 2304,
    "name": "Minimum Path Cost in a Grid",
    "slug": "minimum-path-cost-in-a-grid",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dynamic_programming", "grid", "matrix"],
    "difficulty": "medium",
    "time_complexity": "O(m * n)",
    "space_complexity": "O(m * n)",
    "description": "Find the minimum cost to reach the bottom-right cell from the top-left cell in a grid, where movement is restricted to right and down.",
}

def solve(grid: list[list[int]]) -> int:
    """
    Calculates the minimum cost to travel from the top-left corner to the 
    bottom-right corner of a grid.

    Args:
        grid: A 2D list of integers representing the cost of each cell.

    Returns:
        The minimum path cost to reach the bottom-right cell.

    Examples:
        >>> solve([[1, 3, 1], [1, 5, 1], [4, 2, 1]])
        7
        >>> solve([[1, 1], [1, 1]])
        2
    """
    if not grid or not grid[0]:
        return 0

    rows = len(grid)
    cols = len(grid[0])

    # dp[i][j] represents the minimum cost to reach cell (i, j)
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
            # The minimum cost to reach (i, j) is the current cell's cost 
            # plus the minimum of the costs from the cell above or the cell to the left
            dp[i][j] = grid[i][j] + min(dp[i - 1][j], dp[i][j - 1])

    return dp[rows - 1][cols - 1]
