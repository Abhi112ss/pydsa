METADATA = {
    "id": 2017,
    "name": "Grid Game",
    "slug": "grid-game",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dp", "graphs", "matrix"],
    "difficulty": "medium",
    "time_complexity": "O(m * n)",
    "space_complexity": "O(m * n)",
    "description": "Find the maximum score Alice can get by choosing a path from top-left to bottom-right in a grid, where she can only move right or down.",
}

def solve(grid: list[list[int]]) -> int:
    """
    Calculates the maximum score Alice can achieve in the Grid Game.

    Alice starts at (0, 0) and wants to reach (m-1, n-1). She can only move 
    right or down. The score is the sum of the values in the cells she visits.

    Args:
        grid: A 2D list of integers representing the grid values.

    Returns:
        The maximum possible sum of values along a path from top-left to bottom-right.

    Examples:
        >>> solve([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        21
        >>> solve([[1, 1], [1, 1]])
        3
    """
    if not grid or not grid[0]:
        return 0

    rows = len(grid)
    cols = len(grid[0])

    # dp[i][j] represents the maximum score to reach cell (i, j)
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
            # The max score to reach (i, j) is the current cell value 
            # plus the maximum of the score from the cell above or the cell to the left
            dp[i][j] = grid[i][j] + max(dp[i - 1][j], dp[i][j - 1])

    return dp[rows - 1][cols - 1]
