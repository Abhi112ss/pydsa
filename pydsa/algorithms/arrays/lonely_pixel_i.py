METADATA = {
    "id": 531,
    "name": "Lonely Pixel I",
    "slug": "lonely-pixel-i",
    "category": "Matrix",
    "aliases": [],
    "tags": ["matrix", "array"],
    "difficulty": "easy",
    "time_complexity": "O(m * n)",
    "space_complexity": "O(m + n)",
    "description": "Find the coordinates of a pixel that is the only black pixel in its row and its column.",
}

def solve(grid: list[list[int]]) -> list[int]:
    """
    Finds the coordinates of the lonely pixel in a binary matrix.
    
    A pixel is lonely if it is the only black pixel (1) in its row 
    and the only black pixel in its column.

    Args:
        grid: A 2D list of integers where 1 represents a black pixel and 0 represents white.

    Returns:
        A list of two integers [row, col] representing the coordinates of the lonely pixel.
        Returns [-1, -1] if no such pixel exists.

    Examples:
        >>> solve([[0, 1, 0], [0, 0, 0], [1, 0, 0]])
        [0, 1]
        >>> solve([[0, 0, 0], [0, 1, 0], [0, 0, 0]])
        [1, 1]
    """
    if not grid or not grid[0]:
        return [-1, -1]

    rows = len(grid)
    cols = len(grid[0])

    # Arrays to store the count of black pixels (1s) in each row and column
    row_counts = [0] * rows
    col_counts = [0] * cols

    # First pass: Populate the row and column counts
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                row_counts[r] += 1
                col_counts[c] += 1

    # Second pass: Find the pixel that is the only 1 in both its row and column
    for r in range(rows):
        # Optimization: If row doesn't have exactly one 1, skip the whole row
        if row_counts[r] == 1:
            for c in range(cols):
                if grid[r][c] == 1:
                    # Check if this specific column also has exactly one 1
                    if col_counts[c] == 1:
                        return [r, c]
                    # Since row_counts[r] is 1, we can break the inner loop 
                    # once we find the single 1 in this row
                    break

    return [-1, -1]
