METADATA = {
    "id": 2639,
    "name": "Find the Width of Columns of a Grid",
    "slug": "find_the_width_of_columns_of_a_grid",
    "category": "array",
    "aliases": [],
    "tags": ["arrays", "simulation"],
    "difficulty": "easy",
    "time_complexity": "O(m * n)",
    "space_complexity": "O(n)",
    "description": "Compute the width of each column in a grid based on the positions of characters.",
}


def solve(grid: list[str]) -> list[int]:
    """Calculate the width of each column in a grid.

    For each column, the width is defined as the difference between the
    maximum and minimum row indices that contain a non‑dot character.
    If a column contains fewer than two such characters, its width is -1.

    Args:
        grid: A list of equal‑length strings representing the grid. Empty cells
            are denoted by '.'; any other character is considered occupied.

    Returns:
        A list of integers where the i‑th element is the width of the i‑th column.

    Examples:
        >>> solve(["..a","b..","..c"])
        [1, -1, 2]
        >>> solve(["a"])
        [-1]
    """
    row_count: int = len(grid)
    column_count: int = len(grid[0]) if row_count > 0 else 0
    column_widths: list[int] = []

    for column_index in range(column_count):
        min_row: int = row_count          # initialise to out‑of‑range high value
        max_row: int = -1                 # initialise to out‑of‑range low value

        # Scan each row in the current column to find occupied cells.
        for row_index in range(row_count):
            if grid[row_index][column_index] != '.':
                if row_index < min_row:
                    min_row = row_index
                if row_index > max_row:
                    max_row = row_index

        # Determine width based on the discovered extremes.
        if max_row == -1 or max_row == min_row:
            column_widths.append(-1)
        else:
            column_widths.append(max_row - min_row)

    return column_widths