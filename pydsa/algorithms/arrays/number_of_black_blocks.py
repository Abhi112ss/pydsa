METADATA = {
    "id": 2768,
    "name": "Number of Black Blocks",
    "slug": "number_of_black_blocks",
    "category": "Math",
    "aliases": [],
    "tags": ["arrays", "math"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Calculate the total number of black blocks in a grid based on row and column constraints.",
}

def solve(rows: int, cols: int, black_rows: list[int], black_cols: list[int]) -> int:
    """
    Calculates the total number of black blocks in a grid where a cell (r, c) 
    is black if either row r is in black_rows or column c is in black_cols.

    Args:
        rows: The total number of rows in the grid.
        cols: The total number of columns in the grid.
        black_rows: A list of indices representing rows that are entirely black.
        black_cols: A list of indices representing columns that are entirely black.

    Returns:
        The total count of black cells in the grid.

    Examples:
        >>> solve(3, 3, [0], [0])
        5
        >>> solve(3, 3, [0, 1], [0, 1])
        8
    """
    # The number of black cells is the union of cells in black rows and black columns.
    # Using the Principle of Inclusion-Exclusion:
    # Total = (cells in black rows) + (cells in black columns) - (intersection)
    
    num_black_rows = len(black_rows)
    num_black_cols = len(black_cols)

    # Cells covered by black rows: each black row has 'cols' cells.
    cells_from_rows = num_black_rows * cols

    # Cells covered by black columns: each black column has 'rows' cells.
    cells_from_cols = num_black_cols * rows

    # The intersection: cells that are in both a black row and a black column.
    # These cells are counted twice in the sum above, so we subtract them once.
    intersection = num_black_rows * num_black_cols

    return cells_from_rows + cells_from_cols - intersection
