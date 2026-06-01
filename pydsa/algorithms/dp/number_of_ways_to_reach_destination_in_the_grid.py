METADATA = {
    "id": 2912,
    "name": "Number of Ways to Reach Destination in the Grid",
    "slug": "number-of-ways-to-reach-destination-in-the-grid",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dynamic_programming", "grid", "math"],
    "difficulty": "medium",
    "time_complexity": "O(m * n)",
    "space_complexity": "O(m * n)",
    "description": "Calculate the number of unique paths from the top-left to the bottom-right of a grid with obstacles using dynamic programming.",
}

def solve(grid: list[list[int]], target_x: int, target_y: int, mod: int) -> int:
    """
    Calculates the number of ways to reach a specific destination in a grid.

    Args:
        grid: A 2D list where 0 represents an empty cell and 1 represents an obstacle.
        target_x: The target row index.
        target_y: The target column index.
        mod: The modulo value for the result.

    Returns:
        The number of unique paths to (target_x, target_y) modulo mod.

    Examples:
        >>> grid = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
        >>> solve(grid, 2, 2, 10**9 + 7)
        2
    """
    rows = len(grid)
    cols = len(grid[0])

    # If the starting point or target point is an obstacle, no paths exist.
    if grid[0][0] == 1 or grid[target_x][target_y] == 1:
        return 0

    # dp[i][j] stores the number of ways to reach cell (i, j)
    dp = [[0] * cols for _ in range(rows)]
    
    # Base case: starting point
    dp[0][0] = 1

    for r in range(rows):
        for c in range(cols):
            # Skip if current cell is an obstacle or it's the starting cell
            if grid[r][c] == 1 or (r == 0 and c == 0):
                continue
            
            # Ways to reach current cell is the sum of ways from the top and left cells
            ways_from_top = dp[r - 1][c] if r > 0 else 0
            ways_from_left = dp[r][c - 1] if c > 0 else 0
            
            dp[r][c] = (ways_from_top + ways_from_left) % mod

    return dp[target_x][target_y]
