METADATA = {
    "id": 1463,
    "name": "Cherry Pickup II",
    "slug": "cherry-pickup-ii",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dynamic_programming", "grid_dp"],
    "difficulty": "hard",
    "time_complexity": "O(m * n^2)",
    "space_complexity": "O(m * n^2)",
    "description": "Two robots start at the top corners of a grid and move downwards to collect the maximum number of cherries.",
}

def solve(grid: list[list[int]]) -> int:
    """
    Calculates the maximum number of cherries collected by two robots moving down the grid.

    The robots start at (0, 0) and (0, cols-1). In each step, they move to the 
    next row and can choose to move to the column directly below, or one column 
    to the left or right. If both robots land on the same cell, the cherries 
    are only counted once.

    Args:
        grid: A 2D list of integers representing the number of cherries in each cell.

    Returns:
        The maximum total cherries collected by both robots.

    Examples:
        >>> grid = [[0,1,1],[1,0,1],[1,1,1]]
        >>> solve(grid)
        5
        >>> grid = [[0,0,0],[0,0,0]]
        >>> solve(grid)
        0
    """
    rows = len(grid)
    cols = len(grid[0])

    # dp[r][c1][c2] represents the max cherries collected when robots are at 
    # row 'r', robot 1 is at column 'c1', and robot 2 is at column 'c2'.
    # We use a 3D DP table.
    dp = [[[ -1 for _ in range(cols)] for _ in range(cols)] for _ in range(rows)]

    # Initial state: robots start at (0, 0) and (0, cols-1)
    dp[0][0][cols - 1] = grid[0][0] + grid[0][cols - 1]

    # Iterate through each row
    for r in range(rows - 1):
        for c1 in range(cols):
            for c2 in range(cols):
                # If this state is unreachable, skip it
                if dp[r][c1][c2] == -1:
                    continue

                # Each robot can move to c-1, c, or c+1 in the next row
                for dc1 in [-1, 0, 1]:
                    for dc2 in [-1, 0, 1]:
                        nc1 = c1 + dc1
                        nc2 = c2 + dc2

                        # Check if the new columns are within grid boundaries
                        if 0 <= nc1 < cols and 0 <= nc2 < cols:
                            # Calculate cherries in the next cells
                            # If both robots land on the same cell, count it once
                            cherries = grid[r + 1][nc1]
                            if nc1 != nc2:
                                cherries += grid[r + 1][nc2]

                            # Update the DP table with the maximum cherries found so far
                            new_val = dp[r][c1][c2] + cherries
                            if new_val > dp[r + 1][nc1][nc2]:
                                dp[r + 1][nc1][nc2] = new_val

    # The answer is the maximum value in the last row of the DP table
    max_cherries = 0
    for c1 in range(cols):
        for c2 in range(cols):
            max_cherries = max(max_cherries, dp[rows - 1][c1][c2])

    return max_cherries
