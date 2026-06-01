METADATA = {
    "id": 1559,
    "name": "Detect Cycles in 2D Grid",
    "slug": "detect-cycles-in-2d-grid",
    "category": "Graphs",
    "aliases": [],
    "tags": ["graphs", "dfs", "matrix"],
    "difficulty": "medium",
    "time_complexity": "O(m * n)",
    "space_complexity": "O(m * n)",
    "description": "Determine if there is a cycle of length 4 or more in a 2D grid where all cells in the cycle contain the same character.",
}

def solve(grid: list[list[str]]) -> bool:
    """
    Detects if there is a cycle in a 2D grid of characters.
    A cycle is defined as a path of length 4 or more consisting of the same character,
    where each cell is adjacent (up, down, left, right) to the next.

    Args:
        grid: A 2D list of strings representing the grid.

    Returns:
        True if a cycle exists, False otherwise.

    Examples:
        >>> solve([["a","a","a","a"],["a","b","b","a"],["a","b","b","a"],["a","a","a","a"]])
        True
        >>> solve([["a","b","c"],["d","e","f"],["g","h","i"]])
        False
    """
    if not grid or not grid[0]:
        return False

    rows_count = len(grid)
    cols_count = len(grid[0])
    visited = [[False for _ in range(cols_count)] for _ in range(rows_count)]

    def has_cycle_dfs(row: int, col: int, parent_row: int, parent_col: int, char: str) -> bool:
        """
        Helper function using DFS to find a cycle.
        
        Args:
            row: Current row index.
            col: Current column index.
            parent_row: Row index of the cell we just came from.
            parent_col: Column index of the cell we just came from.
            char: The character we are currently tracking for the cycle.
            
        Returns:
            True if a cycle is detected, False otherwise.
        """
        visited[row][col] = True

        # Explore 4-directional neighbors
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            neighbor_row, neighbor_col = row + dr, col + dc

            # Check boundaries and character match
            if 0 <= neighbor_row < rows_count and 0 <= neighbor_col < cols_count:
                if grid[neighbor_row][neighbor_col] == char:
                    # If the neighbor is visited and is NOT the parent, we found a cycle
                    if visited[neighbor_row][neighbor_col]:
                        if neighbor_row != parent_row or neighbor_col != parent_col:
                            return True
                    else:
                        # Continue DFS traversal
                        if has_cycle_dfs(neighbor_row, neighbor_col, row, col, char):
                            return True
        return False

    # Iterate through every cell in the grid
    for r in range(rows_count):
        for c in range(cols_count):
            # If the cell hasn't been visited, start a new DFS
            if not visited[r][c]:
                if has_cycle_dfs(r, c, -1, -1, grid[r][c]):
                    return True

    return False
