METADATA = {
    "id": 200,
    "name": "Number of Islands",
    "slug": "number_of_islands",
    "category": "Graph",
    "aliases": [],
    "tags": ["dfs", "bfs", "union_find"],
    "difficulty": "medium",
    "time_complexity": "O(m * n)",
    "space_complexity": "O(m * n)",
    "description": "Count the number of islands in a 2D grid where '1' represents land and '0' represents water.",
}

def solve(grid: list[list[str]]) -> int:
    """Count the number of islands in a 2D grid.

    An island is formed by connecting adjacent lands horizontally or vertically.

    Args:
        grid: A 2D list of strings where '1' is land and '0' is water.

    Returns:
        The number of islands.

    Examples:
        >>> solve([["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]])
        1
        >>> solve([["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]])
        3
    """
    if not grid or not grid[0]:
        return 0

    rows = len(grid)
    cols = len(grid[0])
    island_count = 0

    def dfs(row: int, col: int) -> None:
        """Mark all connected land cells as visited by setting them to '0'."""
        # Use iterative DFS with a stack to avoid recursion depth issues
        stack = [(row, col)]
        while stack:
            current_row, current_col = stack.pop()
            # Check bounds and ensure the cell is land
            if (current_row < 0 or current_row >= rows or
                    current_col < 0 or current_col >= cols or
                    grid[current_row][current_col] == '0'):
                continue
            # Mark as visited by setting to '0'
            grid[current_row][current_col] = '0'
            # Explore all four directions
            stack.append((current_row + 1, current_col))
            stack.append((current_row - 1, current_col))
            stack.append((current_row, current_col + 1))
            stack.append((current_row, current_col - 1))

    for row in range(rows):
        for col in range(cols):
            # When we find an unvisited land cell, it's a new island
            if grid[row][col] == '1':
                island_count += 1
                # Flood fill to mark the entire island as visited
                dfs(row, col)

    return island_count