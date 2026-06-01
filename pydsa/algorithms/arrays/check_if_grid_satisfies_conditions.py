METADATA = {
    "id": 3142,
    "name": "Check if Grid Satisfies Conditions",
    "slug": "check-if-grid-satisfies-conditions",
    "category": "Array",
    "aliases": [],
    "tags": ["arrays", "simulation"],
    "difficulty": "easy",
    "time_complexity": "O(m * n)",
    "space_complexity": "O(1)",
    "description": "Check if all adjacent cells in a grid (right and bottom) have a difference of at most 1.",
}

def solve(grid: list[list[int]]) -> bool:
    """
    Checks if the given grid satisfies the condition that the absolute difference 
    between any two adjacent cells (horizontally or vertically) is at most 1.

    Args:
        grid: A 2D list of integers representing the grid.

    Returns:
        True if the grid satisfies the condition, False otherwise.

    Examples:
        >>> solve([[1, 2, 3], [2, 3, 4], [3, 4, 5]])
        True
        >>> solve([[1, 5], [2, 3]])
        False
    """
    rows = len(grid)
    cols = len(grid[0])

    for r in range(rows):
        for c in range(cols):
            current_val = grid[r][c]

            # Check the neighbor to the right
            if c + 1 < cols:
                if abs(current_val - grid[r][c + 1]) > 1:
                    return False

            # Check the neighbor below
            if r + 1 < rows:
                if abs(current_val - grid[r + 1][c]) > 1:
                    return False

    # If no violations were found after checking all adjacent pairs
    return True
