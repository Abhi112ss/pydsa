METADATA = {
    "id": 2943,
    "name": "Maximize Area of Square Hole in Grid",
    "slug": "maximize-area-of-square-hole-in-grid",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["prefix_sum", "matrix", "dynamic_programming"],
    "difficulty": "medium",
    "time_complexity": "O(n * m)",
    "space_complexity": "O(n * m)",
    "description": "Find the area of the largest square consisting entirely of 0s in a given grid.",
}

def solve(grid: list[list[int]]) -> int:
    """
    Finds the area of the largest square consisting entirely of 0s in a grid.

    Args:
        grid: A 2D list of integers where 0 represents a hole and 1 represents a wall.

    Returns:
        The area of the largest square of 0s.

    Examples:
        >>> solve([[0, 0, 1], [0, 0, 1], [1, 1, 1]])
        4
        >>> solve([[1, 1], [1, 1]])
        0
    """
    if not grid or not grid[0]:
        return 0

    rows = len(grid)
    cols = len(grid[0])
    
    # dp[i][j] will store the side length of the largest square of 0s 
    # whose bottom-right corner is at (i, j).
    dp = [[0] * cols for _ in range(rows)]
    max_side = 0

    for r in range(rows):
        for c in range(cols):
            # We are looking for squares of 0s (holes).
            if grid[r][c] == 0:
                if r == 0 or c == 0:
                    # Base case: cells in the first row or first column
                    dp[r][c] = 1
                else:
                    # The side length of the square ending at (r, c) is determined by 
                    # the minimum of the squares ending at its top, left, and top-left neighbors, plus 1.
                    # This ensures that all cells within the new square are also 0s.
                    dp[r][c] = min(dp[r - 1][c], dp[r][c - 1], dp[r - 1][c - 1]) + 1
                
                # Track the maximum side length found so far
                if dp[r][c] > max_side:
                    max_side = dp[r][c]

    return max_side * max_side
