METADATA = {
    "id": 807,
    "name": "Max Increase to Keep City Skyline",
    "slug": "max-increase-to-keep-city-skyline",
    "category": "Matrix",
    "aliases": [],
    "tags": ["greedy", "matrix"],
    "difficulty": "medium",
    "time_complexity": "O(n^2)",
    "space_complexity": "O(n)",
    "description": "Calculate the maximum total height increase possible for buildings in a grid such that the skyline from both directions remains unchanged.",
}

def solve(grid: list[list[int]]) -> int:
    """
    Calculates the maximum total height increase possible for buildings in a grid.

    The skyline from the side (rows) and from the top (columns) must remain the same.
    To maximize the increase, each building at (r, c) can be raised to the 
    minimum of the maximum height in its row and the maximum height in its column.

    Args:
        grid: A 2D list of integers representing building heights.

    Returns:
        The maximum total increase in height.

    Examples:
        >>> solve([[3, 0, 8, 4], [2, 4, 5, 7], [9, 2, 6, 3], [0, 3, 1, 0]])
        13
        >>> solve([[1, 1], [1, 1]])
        0
    """
    if not grid or not grid[0]:
        return 0

    rows = len(grid)
    cols = len(grid[0])

    # Precompute the maximum height for each row and each column
    row_maxima = [0] * rows
    col_maxima = [0] * cols

    for r in range(rows):
        for c in range(cols):
            height = grid[r][c]
            if height > row_maxima[r]:
                row_maxima[r] = height
            if height > col_maxima[c]:
                col_maxima[c] = height

    total_increase = 0

    # For each cell, the maximum allowed height is min(row_max, col_max)
    # The increase is this maximum allowed height minus the current height
    for r in range(rows):
        for c in range(cols):
            allowed_height = min(row_maxima[r], col_maxima[c])
            total_increase += allowed_height - grid[r][c]

    return total_increase
