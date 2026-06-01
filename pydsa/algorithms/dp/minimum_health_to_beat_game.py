METADATA = {
    "id": 2214,
    "name": "Minimum Health to Beat Game",
    "slug": "minimum-health-to-beat-game",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dp", "grid", "matrix"],
    "difficulty": "medium",
    "time_complexity": "O(m * n)",
    "space_complexity": "O(m * n)",
    "description": "Find the minimum initial health required to reach the bottom-right corner from the top-left corner of a grid without health dropping to zero or below.",
}

def solve(healths: list[list[int]]) -> int:
    """
    Calculates the minimum initial health required to traverse the grid.

    The strategy is to use bottom-up dynamic programming starting from the 
    destination (bottom-right) back to the source (top-left). This allows us 
    to determine the minimum health needed at any cell to survive the rest 
    of the journey.

    Args:
        healths: A 2D grid of integers representing health changes.

    Returns:
        The minimum initial health required (must be at least 1).

    Examples:
        >>> solve([[5, -3, 3], [1, -2, 3], [2, -1, 1]])
        3
        >>> solve([[1, -2, -2], [-2, -1, -2], [-2, -2, 1]])
        5
    """
    rows = len(healths)
    cols = len(healths[0])

    # dp[r][c] represents the minimum health needed *before* entering cell (r, c)
    # to ensure health remains >= 1 throughout the path to the destination.
    dp = [[0] * cols for _ in range(rows)]

    # Base case: The destination cell.
    # We need enough health to survive the cell itself. 
    # If healths[r][c] is 5, we need 1 health to enter (1 + 5 = 6, which is > 0).
    # If healths[r][c] is -5, we need 6 health to enter (6 - 5 = 1).
    # Formula: max(1, 1 - healths[r][c])
    dp[rows - 1][cols - 1] = max(1, 1 - healths[rows - 1][cols - 1])

    # Fill the last column (can only move down)
    for r in range(rows - 2, -1, -1):
        dp[r][cols - 1] = max(1, dp[r + 1][cols - 1] - healths[r][cols - 1])

    # Fill the last row (can only move right)
    for c in range(cols - 2, -1, -1):
        dp[rows - 1][c] = max(1, dp[rows - 1][c + 1] - healths[rows - 1][c])

    # Fill the rest of the DP table
    for r in range(rows - 2, -1, -1):
        for c in range(cols - 2, -1, -1):
            # To survive from (r, c), we look at the minimum health needed 
            # for the next step (either right or down) and subtract current cell's effect.
            min_health_needed_next = min(dp[r + 1][c], dp[r][c + 1])
            dp[r][c] = max(1, min_health_needed_next - healths[r][c])

    return dp[0][0]
