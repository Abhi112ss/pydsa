METADATA = {
    "id": 1260,
    "name": "Shift 2D Grid",
    "slug": "shift_2d_grid",
    "category": "array",
    "aliases": [],
    "tags": ["matrix", "simulation", "math"],
    "difficulty": "medium",
    "time_complexity": "O(m * n)",
    "space_complexity": "O(m * n)",
    "description": "Shift all elements of a 2D grid to the right by k positions with wrap‑around.",
}


def solve(grid: list[list[int]], k: int) -> list[list[int]]:
    """Shift the elements of a 2D grid to the right by *k* positions.

    Args:
        grid: A list of *m* rows, each containing *n* integers.
        k: Number of rightward shifts; may be larger than *m × n*.

    Returns:
        A new grid of the same dimensions where each element has been shifted
        right by *k* positions with wrap‑around.

    Examples:
        >>> solve([[1,2,3],[4,5,6],[7,8,9]], 1)
        [[9, 1, 2], [3, 4, 5], [6, 7, 8]]
        >>> solve([[1,2,3],[4,5,6]], 2)
        [[5, 6, 1], [2, 3, 4]]
    """
    row_count = len(grid)
    if row_count == 0:
        return []
    col_count = len(grid[0])
    total_elements = row_count * col_count

    # Effective shifts needed after removing full cycles.
    effective_shifts = k % total_elements

    # Prepare an empty grid to hold shifted values.
    shifted_grid = [[0 for _ in range(col_count)] for _ in range(row_count)]

    for i in range(row_count):
        for j in range(col_count):
            # Linear index of the current element in the flattened view.
            original_index = i * col_count + j
            # Compute the new linear index after shifting.
            new_index = (original_index + effective_shifts) % total_elements
            # Convert linear index back to 2‑D coordinates.
            new_row = new_index // col_count
            new_col = new_index % col_count
            shifted_grid[new_row][new_col] = grid[i][j]

    return shifted_grid