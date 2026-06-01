METADATA = {
    "id": 463,
    "name": "Island Perimeter",
    "slug": "island_perimeter",
    "category": "Array",
    "aliases": [],
    "tags": ["matrix", "dfs"],
    "difficulty": "easy",
    "time_complexity": "O(rows * cols)",
    "space_complexity": "O(1)",
    "description": "Calculate the perimeter of an island represented by a grid of 1s (land) and 0s (water).",
}

def solve(grid: list[list[int]]) -> int:
    """Calculate the perimeter of the island in the given grid.

    Each land cell contributes 4 to the perimeter, minus 2 for every adjacent pair of land cells.

    Args:
        grid: A 2D list of integers where 1 represents land and 0 represents water.

    Returns:
        The perimeter of the island.

    Examples:
        >>> solve([[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]])
        16
        >>> solve([[1]])
        4
        >>> solve([[1,0]])
        4
    """
    if not grid or not grid[0]:
        return 0

    rows = len(grid)
    cols = len(grid[0])
    perimeter = 0

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 1:
                # Each land cell contributes 4 to the perimeter
                perimeter += 4

                # Subtract 2 for every adjacent pair of land cells
                # Check the cell above
                if row > 0 and grid[row - 1][col] == 1:
                    perimeter -= 2
                # Check the cell to the left
                if col > 0 and grid[row][col - 1] == 1:
                    perimeter -= 2

    return perimeter