METADATA = {
    "id": 2132,
    "name": "Stamping the Grid",
    "slug": "stamping_the_grid",
    "category": "Matrix",
    "aliases": [],
    "tags": ["matrix", "greedy", "prefix_sum"],
    "difficulty": "hard",
    "time_complexity": "O(m * n)",
    "space_complexity": "O(m * n)",
    "description": "Determine if a grid can be fully covered by applying a set of rectangular stamps.",
}

def solve(rows: int, cols: int, stamps: list[list[list[int]]]) -> bool:
    """
    Determines if a grid of size rows x cols can be completely covered by the given stamps.

    The algorithm uses a 2D difference array (2D prefix sum) to efficiently mark 
    the areas covered by each stamp. After processing all stamps, we compute 
    the 2D prefix sum to find the actual coverage count for each cell.

    Args:
        rows: The number of rows in the grid.
        cols: The number of columns in the grid.
        stamps: A list of stamps, where each stamp is [r1, c1, r2, c2] 
                representing the top-left and bottom-right coordinates.

    Returns:
        True if every cell in the grid is covered by at least one stamp, False otherwise.

    Examples:
        >>> solve(3, 3, [[0, 0, 1, 1], [1, 1, 2, 2], [0, 0, 2, 2]])
        True
        >>> solve(3, 3, [[0, 0, 1, 1], [1, 1, 2, 2]])
        False
    """
    # Initialize a 2D difference array with an extra row and column to handle boundaries
    # diff[i][j] will help us calculate the coverage using 2D prefix sums.
    diff = [[0] * (cols + 2) for _ in range(rows + 2)]

    for r1, c1, r2, c2 in stamps:
        # We use the 2D difference array technique to mark a rectangle.
        # To cover [r1, r2] and [c1, c2], we update four points.
        # Note: We use r2+1 and c2+1 because the stamp is inclusive.
        diff[r1][c1] += 1
        diff[r1][c2 + 1] -= 1
        diff[r2 + 1][c1] -= 1
        diff[r2 + 1][c2 + 1] += 1

    # Compute the 2D prefix sum to transform the difference array into the actual coverage count.
    # First pass: Row-wise prefix sum
    for r in range(rows):
        for c in range(1, cols):
            diff[r][c] += diff[r][c - 1]

    # Second pass: Column-wise prefix sum
    for c in range(cols):
        for r in range(1, rows):
            diff[r][c] += diff[r - 1][c]

    # Check if any cell in the original grid dimensions has a coverage count of 0.
    for r in range(rows):
        for c in range(cols):
            if diff[r][c] <= 0:
                return False

    return True
