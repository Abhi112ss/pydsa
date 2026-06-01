METADATA = {
    "id": 3028,
    "name": "Ant on the Boundary",
    "slug": "ant_on_the_boundary",
    "category": "Math",
    "aliases": [],
    "tags": ["math", "simulation"],
    "difficulty": "medium",
    "time_complexity": "O(1)",
    "space_complexity": "O(1)",
    "description": "Determine the final position of an ant moving along the perimeter of a grid using modular arithmetic.",
}

def solve(rows: int, cols: int, moves: int) -> list[int]:
    """
    Calculates the final (row, col) position of an ant moving along the boundary of a grid.

    The ant starts at (0, 0) and moves clockwise along the perimeter:
    1. Top edge: (0, 0) -> (0, cols-1)
    2. Right edge: (0, cols-1) -> (rows-1, cols-1)
    3. Bottom edge: (rows-1, cols-1) -> (rows-1, 0)
    4. Left edge: (rows-1, 0) -> (1, 0)

    Args:
        rows: The number of rows in the grid.
        cols: The number of columns in the grid.
        moves: The total number of steps the ant takes.

    Returns:
        A list of two integers [final_row, final_col] representing the ant's position.

    Examples:
        >>> solve(3, 3, 2)
        [0, 2]
        >>> solve(3, 3, 4)
        [1, 2]
        >>> solve(3, 3, 8)
        [0, 0]
    """
    # The perimeter length is the total number of unique cells on the boundary.
    # A grid of R x C has 2*R + 2*C - 4 boundary cells.
    # However, it's easier to think of the path as a sequence of segments.
    
    # Total perimeter length calculation:
    # Top: cols - 1 steps
    # Right: rows - 1 steps
    # Bottom: cols - 1 steps
    # Left: rows - 1 steps
    perimeter_length = 2 * (rows + cols - 2)
    
    # Use modulo to handle cases where moves exceed the perimeter length
    effective_moves = moves % perimeter_length
    
    # Segment 1: Top edge (moving from (0,0) to (0, cols-1))
    if effective_moves < cols:
        return [0, effective_moves]
    
    # Subtract steps taken on the top edge
    effective_moves -= (cols - 1)
    
    # Segment 2: Right edge (moving from (0, cols-1) to (rows-1, cols-1))
    if effective_moves < rows:
        return [effective_moves, cols - 1]
    
    # Subtract steps taken on the right edge
    effective_moves -= (rows - 1)
    
    # Segment 3: Bottom edge (moving from (rows-1, cols-1) to (rows-1, 0))
    if effective_moves < cols:
        return [rows - 1, (cols - 1) - effective_moves]
    
    # Subtract steps taken on the bottom edge
    effective_moves -= (cols - 1)
    
    # Segment 4: Left edge (moving from (rows-1, 0) to (1, 0))
    # The remaining steps must be on the left edge.
    # We are moving upwards from (rows-1, 0).
    return [rows - 1 - effective_moves, 0]
