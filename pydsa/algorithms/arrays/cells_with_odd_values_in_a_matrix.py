METADATA = {
    "id": 1252,
    "name": "Cells with Odd Values in a Matrix",
    "slug": "cells-with-odd-values-in-a-matrix",
    "category": "Simulation",
    "aliases": [],
    "tags": ["simulation", "math", "counting"],
    "difficulty": "easy",
    "time_complexity": "O(R * C)",
    "space_complexity": "O(R + C)",
    "description": "Count the number of cells in a matrix that have an odd value after performing row and column increment operations.",
}

def solve(grid: list[list[int]]) -> int:
    """
    Calculates the number of cells with odd values after row and column increments.

    The algorithm avoids full matrix updates by tracking the parity of increments 
    applied to each row and each column. A cell (r, c) is odd if the sum of 
    increments applied to row 'r' and column 'c' is odd.

    Args:
        grid: A 2D list of integers representing the initial matrix.

    Returns:
        The total count of cells containing an odd value.

    Examples:
        >>> solve([[0, 1, 0], [1, 1, 1], [0, 1, 0]])
        5
        >>> solve([[0]])
        1
    """
    rows = len(grid)
    cols = len(grid[0])

    # Track how many times each row and column is incremented
    row_increments = [0] * rows
    col_increments = [0] * cols

    # First pass: Count increments per row and column based on the input grid
    # Note: The problem states we increment based on the initial grid values
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                row_increments[r] += 1
                col_increments[c] += 1

    odd_count = 0
    # Second pass: Determine parity of each cell without updating the whole matrix
    for r in range(rows):
        for c in range(cols):
            # A cell is odd if (initial_value + row_inc + col_inc) % 2 != 0
            # Since initial values are 0 or 1, we check the parity of the sum
            if (grid[r][c] + row_increments[r] + col_increments[c]) % 2 != 0:
                odd_count += 1

    return odd_count
