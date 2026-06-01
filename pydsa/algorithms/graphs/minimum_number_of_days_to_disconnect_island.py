METADATA = {
    "id": 1568,
    "name": "Minimum Number of Days to Disconnect Island",
    "slug": "minimum-number-of-days-to-disconnect-island",
    "category": "Graph",
    "aliases": [],
    "tags": ["dfs", "bfs", "graph", "grid"],
    "difficulty": "medium",
    "time_complexity": "O(n * m)",
    "space_complexity": "O(n * m)",
    "description": "Find the minimum number of days (cells to remove) to make an island disconnected.",
}

def solve(grid: list[list[int]]) -> int:
    """
    Finds the minimum number of cells to remove to disconnect the island.

    The island is disconnected if there are no paths between any two land cells,
    or if there are no land cells left at all.

    Args:
        grid: A 2D grid of 0s (water) and 1s (land).

    Returns:
        The minimum number of cells to remove (0, 1, or 2).

    Examples:
        >>> solve([[0,1,1,0],[0,1,1,0],[0,0,0,0]])
        1
        >>> solve([[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1]])
        2
    """
    rows = len(grid)
    cols = len(grid[0])

    def count_islands(current_grid: list[list[int]]) -> int:
        """Counts the number of connected components of 1s."""
        visited = set()
        island_count = 0

        for r in range(rows):
            for c in range(cols):
                if current_grid[r][c] == 1 and (r, c) not in visited:
                    island_count += 1
                    # Standard BFS to mark all cells in the current island
                    queue = [(r, c)]
                    visited.add((r, c))
                    idx = 0
                    while idx < len(queue):
                        curr_r, curr_c = queue[idx]
                        idx += 1
                        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                            nr, nc = curr_r + dr, curr_c + dc
                            if (0 <= nr < rows and 0 <= nc < cols and 
                                    current_grid[nr][nc] == 1 and (nr, nc) not in visited):
                                visited.add((nr, nc))
                                queue.append((nr, nc))
        return island_count

    # Step 1: Check if the island is already disconnected (0 days)
    if count_islands(grid) != 1:
        return 0

    # Step 2: Try removing one cell (1 day)
    # We only need to check land cells (1s)
    land_cells = []
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                land_cells.append((r, c))

    for r, c in land_cells:
        grid[r][c] = 0  # Temporarily remove land
        if count_islands(grid) != 1:
            return 1
        grid[r][c] = 1  # Backtrack

    # Step 3: If removing one cell didn't work, the answer is at most 2.
    # In a 2D grid, any connected component can be disconnected by removing 
    # at most 2 cells (the neighbors of a corner cell).
    return 2
