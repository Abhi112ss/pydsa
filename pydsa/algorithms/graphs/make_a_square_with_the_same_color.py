METADATA = {
    "id": 3127,
    "name": "Make a Square with the Same Color",
    "slug": "make-a-square-with-the-same-color",
    "category": "Grid",
    "aliases": [],
    "tags": ["dfs", "bfs", "grid"],
    "difficulty": "medium",
    "time_complexity": "O(n^2)",
    "space_complexity": "O(n^2)",
    "description": "Determine if it is possible to make a 2x2 square of the same color by changing at most one cell in a grid.",
}

def solve(grid: list[list[int]]) -> bool:
    """
    Determines if a 2x2 square of the same color can be formed by changing at most one cell.

    Args:
        grid: A 2D list of integers representing the colors of cells in an n x n grid.

    Returns:
        True if a 2x2 square of the same color can be formed by changing at most one cell, 
        False otherwise.

    Examples:
        >>> solve([[1, 2, 1], [2, 1, 1], [1, 1, 2]])
        True
        >>> solve([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        False
    """
    rows = len(grid)
    cols = len(grid[0])

    # Iterate through every possible top-left corner of a 2x2 square
    for r in range(rows - 1):
        for c in range(cols - 1):
            # Extract the four cells forming the current 2x2 square
            cells = [
                grid[r][c],
                grid[r][c + 1],
                grid[r + 1][c],
                grid[r + 1][c + 1]
            ]
            
            # Count occurrences of each color in the 2x2 block
            color_counts: dict[int, int] = {}
            for color in cells:
                color_counts[color] = color_counts.get(color, 0) + 1
            
            # A 2x2 square can be made if:
            # 1. All 4 cells are already the same color (count == 4)
            # 2. 3 cells are the same color and 1 is different (count == 3)
            # This is equivalent to checking if any color appears at least 3 times.
            if any(count >= 3 for count in color_counts.values()):
                return True

    return False
