METADATA = {
    "id": 885,
    "name": "Spiral Matrix III",
    "slug": "spiral-matrix-iii",
    "category": "Simulation",
    "aliases": [],
    "tags": ["matrix", "simulation"],
    "difficulty": "medium",
    "time_complexity": "O(max(R, C)^2)",
    "space_complexity": "O(1)",
    "description": "Return the order in which cells are visited in a spiral pattern starting from a given position.",
}

def solve(rows: int, cols: int, start_row: int, start_col: int) -> list[int]:
    """
    Simulates a spiral traversal starting from a specific cell in an infinite grid,
    returning the order of cells that fall within the bounds of a given matrix.

    Args:
        rows: The number of rows in the matrix.
        cols: The number of columns in the matrix.
        start_row: The starting row index.
        start_col: The starting column index.

    Returns:
        A list of integers representing the order of cells visited within the matrix.

    Examples:
        >>> solve(3, 3, 0, 0)
        [0, 1, 2, 3, 4, 5, 6, 7, 8]
        >>> solve(5, 3, 3, 0)
        [12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36]
    """
    # Directions: Right, Down, Left, Up
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    result = []
    current_row, current_col = start_row, start_col
    direction_idx = 0
    steps_to_move = 1
    cells_found = 0
    total_cells = rows * cols

    # Add the starting cell if it is within bounds
    if 0 <= current_row < rows and 0 <= current_col < cols:
        result.append(current_row * cols + current_col)
        cells_found += 1

    while cells_found < total_cells:
        # We move in the current direction for 'steps_to_move' steps
        # The step length increases by 1 every two direction changes
        for _ in range(2):
            dr, dc = directions[direction_idx]
            
            for _ in range(steps_to_move):
                current_row += dr
                current_col += dc
                
                # Check if the new position is within the matrix boundaries
                if 0 <= current_row < rows and 0 <= current_col < cols:
                    result.append(current_row * cols + current_col)
                    cells_found += 1
                    if cells_found == total_cells:
                        return result
            
            # Rotate direction clockwise
            direction_idx = (direction_idx + 1) % 4
            
        # Increase step length after completing two directions (e.g., Right then Down)
        steps_to_move += 1

    return result
