METADATA = {
    "id": 694,
    "name": "Number of Distinct Islands",
    "slug": "number-of-distinct-islands",
    "category": "Medium",
    "aliases": [],
    "tags": ["dfs", "hash_set", "matrix", "traversal"],
    "difficulty": "medium",
    "time_complexity": "O(r * c)",
    "space_complexity": "O(r * c)",
    "description": "Count the number of unique island shapes in a 2D grid using relative coordinate paths.",
}

def solve(grid: list[list[int]]) -> int:
    """
    Counts the number of distinct island shapes in a 2D grid.

    Two islands are considered the same if one can be translated (not rotated or reflected)
    to equal the other.

    Args:
        grid: A 2D list of integers where 1 represents land and 0 represents water.

    Returns:
        The number of unique island shapes.

    Examples:
        >>> grid = [[1,1,0,0,0],[1,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]]
        >>> solve(grid)
        1
        >>> grid2 = [[1,1,0,1,1],[1,0,0,0,0],[0,0,0,0,1],[1,1,0,1,1]]
        >>> solve(grid2)
        3
    """
    if not grid or not grid[0]:
        return 0

    rows = len(grid)
    cols = len(grid[0])
    visited = set[tuple[int, int]]()
    unique_islands = set[tuple[tuple[int, int], ...]]()

    def dfs(r: int, c: int, base_r: int, base_c: int, shape: list[tuple[int, int]]):
        """
        Performs DFS to explore an island and records relative coordinates.
        """
        # Boundary and validity checks
        if (r < 0 or r >= rows or 
            c < 0 or c >= cols or 
            grid[r][c] == 0 or 
            (r, c) in visited):
            return

        visited.add((r, c))
        # Store the coordinate relative to the starting cell of this island
        shape.append((r - base_r, c - base_c))

        # Explore all 4 directions
        dfs(r + 1, c, base_r, base_c, shape)
        dfs(r - 1, c, base_r, base_c, shape)
        dfs(r, c + 1, base_r, base_c, shape)
        dfs(r, c - 1, base_r, base_c, shape)

    for r in range(rows):
        for c in range(cols):
            # If we find unvisited land, it's a new island
            if grid[r][c] == 1 and (r, c) not in visited:
                island_shape = []
                # Use the current (r, c) as the origin for this island's shape
                dfs(r, c, r, c, island_shape)
                # Convert list of tuples to a tuple of tuples to make it hashable
                unique_islands.add(tuple(island_shape))

    return len(unique_islands)
