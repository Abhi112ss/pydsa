METADATA = {
    "id": 3148,
    "name": "Maximum Difference Score in a Grid",
    "slug": "maximum-difference-score-in-a-grid",
    "category": "Arrays",
    "aliases": [],
    "tags": ["arrays", "simulation"],
    "difficulty": "easy",
    "time_complexity": "O(m * n)",
    "space_complexity": "O(1)",
    "description": "Find the maximum difference between any two elements in a 2D grid.",
}

def solve(grid: list[list[int]]) -> int:
    """
    Calculates the maximum difference score in a 2D grid.
    
    The maximum difference score is defined as the difference between the 
    maximum element and the minimum element present in the grid.

    Args:
        grid: A 2D list of integers representing the grid.

    Returns:
        The maximum difference (max_val - min_val) found in the grid.

    Examples:
        >>> solve([[1, 2], [3, 4]])
        3
        >>> solve([[10, 5], [2, 8]])
        8
        >>> solve([[7]])
        0
    """
    if not grid or not grid[0]:
        return 0

    # Initialize min and max with the first element of the grid
    min_val = grid[0][0]
    max_val = grid[0][0]

    # Iterate through every cell in the 2D grid
    for row in grid:
        for value in row:
            # Update the global minimum and maximum encountered so far
            if value < min_val:
                min_val = value
            if value > max_val:
                max_val = value

    # The maximum difference is the spread between the extremes
    return max_val - min_val
