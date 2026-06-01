METADATA = {
    "id": 764,
    "name": "Largest Plus Sign",
    "slug": "largest-plus-sign",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dp", "arrays", "matrix"],
    "difficulty": "hard",
    "time_complexity": "O(n^2)",
    "space_complexity": "O(n^2)",
    "description": "Find the largest plus sign in a binary grid by calculating the maximum possible arm length for each cell.",
}

def solve(grid: list[list[int]]) -> int:
    """
    Finds the largest plus sign in a binary grid.
    
    A plus sign is defined by its center and four arms of equal length.
    The size of the plus sign is the length of one arm (including the center).

    Args:
        grid: A 2D list of integers where 1 represents a part of a plus sign 
              and 0 represents an empty space.

    Returns:
        The size of the largest plus sign found in the grid.

    Examples:
        >>> solve([[0,0,1,0,0],[0,0,1,0,0],[1,11,1,1,1],[0,0,1,0,0],[0,0,1,0,0]])
        3
        >>> solve([[0,0,0],[0,0,0]])
        0
    """
    if not grid or not grid[0]:
        return 0

    rows = len(grid)
    cols = len(grid[0])
    
    # dp[r][c] will store the minimum length of the four arms 
    # (up, down, left, right) extending from cell (r, c).
    dp = [[float('inf')] * cols for _ in range(rows)]

    # Left to Right pass
    for r in range(rows):
        count = 0
        for c in range(cols):
            count = (count + 1) if grid[r][c] == 1 else 0
            dp[r][c] = min(dp[r][c], count)

    # Right to Left pass
    for r in range(rows):
        count = 0
        for c in range(cols - 1, -1, -1):
            count = (count + 1) if grid[r][c] == 1 else 0
            dp[r][c] = min(dp[r][c], count)

    # Top to Bottom pass
    for c in range(cols):
        count = 0
        for r in range(rows):
            count = (count + 1) if grid[r][c] == 1 else 0
            dp[r][c] = min(dp[r][c], count)

    # Bottom to Top pass
    max_plus_size = 0
    for c in range(cols):
        count = 0
        for r in range(rows - 1, -1, -1):
            count = (count + 1) if grid[r][c] == 1 else 0
            # The final value at dp[r][c] is the minimum of all 4 directions
            dp[r][c] = min(dp[r][c], count)
            # Update the global maximum
            if dp[r][c] != float('inf'):
                max_plus_size = max(max_plus_size, int(dp[r][c]))

    return max_plus_size
