METADATA = {
    "id": 1030,
    "name": "Matrix Cells in Distance Order",
    "slug": "matrix_cells_in_distance_order",
    "category": "array",
    "aliases": [],
    "tags": ["sorting", "bfs", "geometry"],
    "difficulty": "easy",
    "time_complexity": "O(r * c log(r * c))",
    "space_complexity": "O(r * c)",
    "description": "Return all matrix coordinates sorted by their Manhattan distance from a given cell.",
}


def solve(r: int, c: int, r0: int, c0: int) -> list[list[int]]:
    """Generate all matrix cells sorted by Manhattan distance from (r0, c0).

    Args:
        r: Number of rows in the matrix.
        c: Number of columns in the matrix.
        r0: Row index of the reference cell.
        c0: Column index of the reference cell.

    Returns:
        A list of [row, column] pairs ordered by increasing Manhattan distance.

    Examples:
        >>> solve(1, 2, 0, 0)
        [[0, 0], [0, 1]]
        >>> solve(2, 2, 0, 1)
        [[0, 1], [0, 0], [1, 1], [1, 0]]
    """
    # Generate every possible cell coordinate in the matrix.
    all_cells = [[row_index, col_index] for row_index in range(r) for col_index in range(c)]

    # Sort cells by Manhattan distance to the reference cell (r0, c0).
    all_cells.sort(key=lambda cell: abs(cell[0] - r0) + abs(cell[1] - c0))

    return all_cells