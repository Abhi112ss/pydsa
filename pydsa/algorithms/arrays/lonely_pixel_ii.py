METADATA = {
    "id": 533,
    "name": "Lonely Pixel II",
    "slug": "lonely-pixel-ii",
    "category": "Matrix",
    "aliases": [],
    "tags": ["hash_map", "matrix", "counting"],
    "difficulty": "medium",
    "time_complexity": "O(m * n)",
    "space_complexity": "O(m * n)",
    "description": "Find the number of pixels that are the only ones in their row and their column.",
}

def solve(grid: list[list[int]]) -> int:
    """
    Finds the number of pixels that are the only ones in their row and their column.

    Args:
        grid: A 2D list of integers representing the pixel grid.

    Returns:
        The total count of lonely pixels.

    Examples:
        >>> solve([[1,0,0],[0,0,0],[1,0,1]])
        1
        >>> solve([[1,0,0],[0,0,0],[0,0,0]])
        1
    """
    if not grid or not grid[0]:
        return 0

    rows = len(grid)
    cols = len(grid[0])

    # row_counts[i] stores the number of 1s in row i
    # col_counts[j] stores the number of 1s in column j
    row_counts = [0] * rows
    col_counts = [0] * cols

    # First pass: Populate the counts for each row and column
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                row_counts[r] += 1
                col_counts[c] += 1

    lonely_pixel_count = 0

    # Second pass: A pixel is lonely if it is 1 AND its row count is 1 AND its col count is 1
    for r in range(rows):
        # Optimization: if the row doesn't have exactly one '1', skip the whole row
        if row_counts[r] == 1:
            for c in range(cols):
                if grid[r][c] == 1:
                    # Check if this specific column also has exactly one '1'
                    if col_counts[c] == 1:
                        lonely_pixel_count += 1
                    # Since row_counts[r] is 1, we can break the inner loop once found
                    break

    return lonely_pixel_count
