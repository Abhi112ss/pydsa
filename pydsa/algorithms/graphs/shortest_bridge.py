METADATA = {
    "id": 934,
    "name": "Shortest Bridge",
    "slug": "shortest-bridge",
    "category": "Graph",
    "aliases": [],
    "tags": ["bfs", "dfs", "matrix"],
    "difficulty": "medium",
    "time_complexity": "O(n^2)",
    "space_complexity": "O(n^2)",
    "description": "Find the minimum number of 0s that must be flipped to 1s to connect two islands in a binary matrix.",
}

from collections import deque

def solve(grid: list[list[int]]) -> int:
    """
    Finds the shortest bridge between two islands in a binary matrix.

    Args:
        grid: A 2D list of integers where 1 represents land and 0 represents water.

    Returns:
        The minimum number of 0s to flip to connect the two islands.

    Examples:
        >>> solve([[0,1],[1,0]])
        1
        >>> solve([[0,1,0],[0,0,0],[0,0,1]])
        2
    """
    rows = len(grid)
    cols = len(grid[0])
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    
    island_one_cells = deque()
    found_first_island = False

    def dfs_find_island(r: int, c: int):
        """Traverses the first island using DFS and marks cells as visited."""
        nonlocal found_first_island
        stack = [(r, c)]
        grid[r][c] = 2  # Mark as visited/part of island 1
        
        while stack:
            curr_r, curr_c = stack.pop()
            island_one_cells.append((curr_r, curr_c, 0))
            
            for dr, dc in directions:
                nr, nc = curr_r + dr, curr_c + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    stack.append((nr, nc))

    # 1. Find the first island and mark all its cells
    for r in range(rows):
        if found_first_island:
            break
        for c in range(cols):
            if grid[r][c] == 1:
                dfs_find_island(r, c)
                found_first_island = True
                break

    # 2. Multi-source BFS to find the shortest path to the second island
    # island_one_cells contains (row, col, distance)
    while island_one_cells:
        r, c, dist = island_one_cells.popleft()
        
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            
            if 0 <= nr < rows and 0 <= nc < cols:
                if grid[nr][nc] == 1:
                    # Found the second island
                    return dist
                elif grid[nr][nc] == 0:
                    # Expand into water
                    grid[nr][nc] = 2  # Mark as visited to avoid cycles
                    island_one_cells.append((nr, nc, dist + 1))
                    
    return -1
