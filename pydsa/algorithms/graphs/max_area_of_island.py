METADATA = {
    "id": 695,
    "name": "Max Area of Island",
    "slug": "max-area-of-island",
    "category": "Matrix",
    "aliases": [],
    "tags": ["dfs", "bfs", "matrix", "graph"],
    "difficulty": "medium",
    "time_complexity": "O(R * C)",
    "space_complexity": "O(R * C)",
    "description": "Find the maximum area of an island in a 2D binary grid, where an island is a group of 1s connected 4-directionally.",
}

def solve(grid: list[list[int]]) -> int:
    """
    Calculates the maximum area of an island in a given 2D grid.

    Args:
        grid: A 2D list of integers where 1 represents land and 0 represents water.

    Returns:
        The area of the largest island found in the grid. Returns 0 if no island exists.

    Examples:
        >>> solve([[0,0,1,0,0,0,0,1,0,0,0,0,0], [0,0,0,0,0,0,0,1,1,1,0,0,0], [0,1,0,0,0,1,0,1,1,0,0,0,0], [0,1,0,0,0,0,0,0,0,0,0,0,0], [0,1,0,0,0,1,1,1,0,0,0,0,0], [0,0,0,0,0,1,1,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0,0,0,0,0]])
        5
    """
    if not grid or not grid[0]:
        return 0

    rows = len(grid)
    cols = len(grid[0])
    max_area = 0

    def get_island_area(row: int, col: int) -> int:
        """
        Performs a Depth First Search to calculate the area of an island.
        
        Args:
            row: Current row index.
            col: Current column index.
            
        Returns:
            The total number of land cells connected to the starting cell.
        """
        # Base case: check boundaries and if the cell is water (0)
        if row < 0 or row >= rows or col < 0 or col >= cols or grid[row][col] == 0:
            return 0

        # Mark the current cell as visited by setting it to 0 to avoid infinite loops
        grid[row][col] = 0
        
        # Recursively sum the area of the current cell + all 4 neighbors
        area = 1
        area += get_island_area(row + 1, col)
        area += get_island_area(row - 1, col)
        area += get_island_area(row, col + 1)
        area += get_island_area(row, col - 1)
        
        return area

    # Iterate through every cell in the grid
    for r in range(rows):
        for c in range(cols):
            # If we find land, it's the start of a new island
            if grid[r][c] == 1:
                current_island_area = get_island_area(r, c)
                max_area = max(max_area, current_island_area)

    return max_area
