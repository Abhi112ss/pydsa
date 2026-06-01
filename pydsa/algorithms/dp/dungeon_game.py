METADATA = {
    "id": 174,
    "name": "Dungeon Game",
    "slug": "dungeon-game",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dynamic_programming", "matrix", "greedy"],
    "difficulty": "hard",
    "time_complexity": "O(m * n)",
    "space_complexity": "O(m * n)",
    "description": "Find the minimum initial health required to reach the bottom-right corner of a grid without health dropping to zero or below.",
}

def solve(dungeon: list[list[int]]) -> int:
    """
    Calculates the minimum initial health required to traverse the dungeon.

    The strategy uses bottom-up dynamic programming starting from the princess (bottom-right)
    to the knight (top-left). We calculate the minimum health needed *before* entering 
    each cell to ensure the knight survives the path ahead.

    Args:
        dungeon: A 2D list of integers representing health changes (positive or negative).

    Returns:
        The minimum initial health required to reach the destination.

    Examples:
        >>> solve([[-2, -3, 3], [-5, -10, 1], [10, 30, -5]])
        7
        >>> solve([[0, -2, -7], [[-4, -3, 4], [2, 1, -1]]]) # Note: Example structure simplified
    """
    rows = len(dungeon)
    cols = len(dungeon[0])

    # dp[i][j] represents the minimum health needed BEFORE entering cell (i, j)
    dp = [[0] * cols for _ in range(rows)]

    # Base case: The destination cell (bottom-right)
    # If dungeon[r][c] is positive, we only need 1 health to survive.
    # If dungeon[r][c] is negative, we need 1 + abs(dungeon[r][c]) health.
    dp[rows - 1][cols - 1] = max(1, 1 - dungeon[rows - 1][cols - 1])

    # Fill the last column (can only move down)
    for r in range(rows - 2, -1, -1):
        dp[r][cols - 1] = max(1, dp[r + 1][cols - 1] - dungeon[r][cols - 1])

    # Fill the last row (can only move right)
    for c in range(cols - 2, -1, -1):
        dp[rows - 1][c] = max(1, dp[rows - 1][c + 1] - dungeon[rows - 1][c])

    # Fill the rest of the DP table
    for r in range(rows - 2, -1, -1):
        for c in range(cols - 2, -1, -1):
            # To survive from (r, c), we must choose the path (down or right) 
            # that requires the minimum health to proceed.
            min_health_needed_after_this_cell = min(dp[r + 1][c], dp[r][c + 1])
            
            # The health needed before entering (r, c) must account for the current cell's value.
            # We must also ensure health never drops below 1.
            dp[r][c] = max(1, min_health_needed_after_this_cell - dungeon[r][c])

    return dp[0][0]
