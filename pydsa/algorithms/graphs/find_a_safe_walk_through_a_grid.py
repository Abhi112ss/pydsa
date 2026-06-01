METADATA = {
    "id": 3286,
    "name": "Find a Safe Walk Through a Grid",
    "slug": "find-a-safe-walk-through-a-grid",
    "category": "Graph",
    "aliases": [],
    "tags": ["bfs", "dfs", "dynamic_programming", "shortest_path"],
    "difficulty": "hard",
    "time_complexity": "O(m * n)",
    "space_complexity": "O(m * n)",
    "description": "Find the shortest path from the top-left to the bottom-right cell such that every cell in the path is at least 'distance' away from any obstacle.",
}

from collections import deque

def solve(grid: list[list[int]], distance: int) -> int:
    """
    Finds the shortest path from (0, 0) to (m-1, n-1) where every cell in the path 
    is at least 'distance' away from any obstacle (cell with value 1).

    Args:
        grid: A 2D integer grid where 1 represents an obstacle and 0 represents empty space.
        distance: The minimum required distance from any obstacle for a cell to be safe.

    Returns:
        The length of the shortest path (number of cells) if a safe path exists, 
        otherwise -1.

    Examples:
        >>> solve([[0,0,0],[0,1,0],[0,0,0]], 1)
        5
        >>> solve([[0,0,0],[0,1,0],[0,0,0]], 2)
        -1
    """
    rows = len(grid)
    cols = len(grid[0])
    
    # 1. Multi-source BFS to calculate distance to nearest obstacle for every cell
    # Initialize distances with -1 (unvisited)
    dist_to_obstacle = [[-1 for _ in range(cols)] for _ in range(rows)]
    queue = deque()

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                dist_to_obstacle[r][c] = 0
                queue.append((r, c))

    # If no obstacles exist, all cells are effectively at infinite distance.
    # We use a large number to represent this for the comparison logic.
    if not queue:
        # We can treat all cells as having distance >= distance
        # But for the BFS to work correctly, we can just initialize with a large value
        dist_to_obstacle = [[float('inf')] * cols for _ in range(rows)]
    else:
        # Standard BFS to propagate distances from obstacles
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        while queue:
            r, c = queue.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and dist_to_obstacle[nr][nc] == -1:
                    dist_to_obstacle[nr][nc] = dist_to_obstacle[r][c] + 1
                    queue.append((nr, nc))

    # 2. Check if start or end cells are invalid immediately
    if dist_to_obstacle[0][0] < distance or dist_to_obstacle[rows - 1][cols - 1] < distance:
        return -1

    # 3. BFS to find the shortest path using only "safe" cells
    # A cell is safe if dist_to_obstacle[r][c] >= distance
    path_queue = deque([(0, 0, 1)])  # (row, col, current_path_length)
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    visited[0][0] = True

    while path_queue:
        r, c, length = path_queue.popleft()

        if r == rows - 1 and c == cols - 1:
            return length

        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nr, nc = r + dr, c + dc
            if (0 <= nr < rows and 0 <= nc < cols and 
                not visited[nr][nc] and 
                dist_to_obstacle[nr][nc] >= distance):
                
                visited[nr][nc] = True
                path_queue.append((nr, nc, length + 1))

    return -1
