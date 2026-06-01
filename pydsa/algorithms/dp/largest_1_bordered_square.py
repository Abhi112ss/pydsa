METADATA = {
    "id": 1139,
    "name": "Largest 1-Bordered Square",
    "slug": "largest-1-bordered-square",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dynamic_programming", "matrix"],
    "difficulty": "medium",
    "time_complexity": "O(n * m * min(n, m))",
    "space_complexity": "O(n * m)",
    "description": "Find the side length of the largest square that has all its border elements equal to 1.",
}

def solve(grid: list[list[int]]) -> int:
    """
    Finds the side length of the largest square whose border consists entirely of 1s.

    Args:
        grid: A 2D list of integers where grid[i][j] is either 0 or 1.

    Returns:
        The side length of the largest 1-bordered square.

    Examples:
        >>> solve([[0,1,1,1,0],[1,1,1,1,1],[0,1,1,1,0],[0,0,0,0,0]])
        3
        >>> solve([[1,0,1],[1,1,1],[1,0,1]])
        1
    """
    if not grid or not grid[0]:
        return 0

    rows = len(grid)
    cols = len(grid[0])

    # left[r][c] stores the number of consecutive 1s to the left of (r, c), including itself.
    # up[r][c] stores the number of consecutive 1s above (r, c), including itself.
    left = [[0] * cols for _ in range(rows)]
    up = [[0] * cols for _ in range(rows)]

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                left[r][c] = (left[r][c - 1] + 1) if c > 0 else 1
                up[r][c] = (up[r - 1][c] + 1) if r > 0 else 1

    max_side = 0

    # Iterate through every cell as the bottom-right corner of a potential square.
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                # The maximum possible side length for a square ending at (r, c)
                # is limited by the continuous 1s ending at this cell.
                possible_side = min(left[r][c], up[r][c])
                
                # Check squares from largest possible down to current max_side + 1
                for side in range(possible_side, max_side, -1):
                    # To validate a square of 'side', we check the top and left borders.
                    # The bottom and right borders are already guaranteed by 'possible_side'.
                    top_row = r - side + 1
                    left_col = c - side + 1
                    
                    # Check if the top border (from left_col to c at top_row) is all 1s.
                    # We use the 'left' precomputed table: left[top_row][c] must be >= side.
                    # Check if the left border (from top_row to r at left_col) is all 1s.
                    # We use the 'up' precomputed table: up[r][left_col] must be >= side.
                    if left[top_row][c] >= side and up[r][left_col] >= side:
                        max_side = max(max_side, side)
                        break # Found the largest square for this bottom-right corner

    return max_side
