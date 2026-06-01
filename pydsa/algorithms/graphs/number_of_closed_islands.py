METADATA = {
    "id": 1254,
    "name": "Number of Closed Islands",
    "slug": "number-of-closed-islands",
    "category": "Matrix",
    "aliases": [],
    "tags": ["dfs", "bfs", "matrix", "flood-fill"],
    "difficulty": "medium",
    "time_complexity": "O(m * n)",
    "space_complexity": "O(m * n)",
    "description": "Count the number of islands completely surrounded by water, meaning they do not touch the boundary of the grid.",
}

def solve(grid: list[list[int]]) -> int:
    """
    Counts the number of closed islands in a 2D grid.
    
    An island is a group of 0s connected 4-directionally. A closed island 
    is an island that is completely surrounded by 1s and does not touch 
    the edges of the grid.

    Args:
        grid: A 2D list of integers where 0 represents land and 1 represents water.

    Returns:
        The total number of closed islands.

    Examples:
        >>> solve([[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]])
        2
    """
    if not grid or not grid[0]:
        return 0

    rows = len(grid)
    cols = len(grid[0])

    def flood_fill(r: int, c: int) -> None:
        """
        Standard DFS to sink an island (turn 0s into 1s).
        """
        if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 1:
            return
        
        grid[r][c] = 1  # Mark as visited by turning land to water
        
        # Explore 4-directional neighbors
        flood_fill(r + 1, c)
        flood_fill(r - 1, c)
        flood_fill(r, c + 1)
        flood_fill(r, c - 1)

    # Step 1: Eliminate all islands connected to the boundaries.
    # Any land (0) on the edge or connected to the edge cannot be a closed island.
    for r in range(rows):
        for c in range(cols):
            # Check if the cell is on the boundary and is land
            is_boundary = (r == 0 or r == rows - 1 or c == 0 or c == cols - 1)
            if is_boundary and grid[r][c] == 0:
                flood_fill(r, c)

    # Step 2: Count the remaining islands.
    # Since boundary-connected islands are gone, every remaining 0 belongs to a closed island.
    closed_island_count = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 0:
                closed_island_count += 1
                flood_fill(r, c)

    return closed_island_count
