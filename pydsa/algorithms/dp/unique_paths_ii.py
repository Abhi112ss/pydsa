METADATA = {
    "id": 63,
    "name": "Unique Paths II",
    "slug": "unique-paths-ii",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dynamic_programming", "matrix", "grid"],
    "difficulty": "medium",
    "time_complexity": "O(m*n)",
    "space_complexity": "O(n)",
    "description": "Find the number of unique paths from the top-left to the bottom-right of a grid with obstacles.",
}

def solve(obstacle_grid: list[list[int]]) -> int:
    """
    Calculates the number of unique paths in a grid with obstacles using dynamic programming.

    Args:
        obstacle_grid: A 2D list of integers where 0 represents an empty space 
                       and 1 represents an obstacle.

    Returns:
        The total number of unique paths from the top-left corner to the 
        bottom-right corner.

    Examples:
        >>> solve([[0,0,0],[0,1,0],[0,0,0]])
        2
        >>> solve([[0,1],[0,0]])
        1
    """
    if not obstacle_grid or not obstacle_grid[0]:
        return 0

    rows = len(obstacle_grid)
    cols = len(obstacle_grid[0])

    # If the starting point or ending point is an obstacle, no paths are possible
    if obstacle_grid[0][0] == 1 or obstacle_grid[rows - 1][cols - 1] == 1:
        return 0

    # Use a 1D array to optimize space complexity to O(n)
    # dp[j] represents the number of ways to reach the current cell in column j
    dp = [0] * cols
    dp[0] = 1

    for r in range(rows):
        for c in range(cols):
            if obstacle_grid[r][c] == 1:
                # If there is an obstacle, the number of ways to reach this cell is 0
                dp[c] = 0
            elif c > 0:
                # The number of ways to reach cell (r, c) is the sum of ways 
                # from the cell above (already in dp[c]) and the cell to the left (dp[c-1])
                dp[c] += dp[c - 1]
            # Note: if c == 0 and obstacle_grid[r][0] == 0, dp[0] remains 
            # its previous value (ways from the cell above), which is correct.

    return dp[cols - 1]
