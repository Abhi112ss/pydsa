METADATA = {
    "id": 1765,
    "name": "Map of Highest Peak",
    "slug": "map-of-highest-peak",
    "category": "Breadth-First Search",
    "aliases": [],
    "tags": ["bfs", "grid", "matrix"],
    "difficulty": "medium",
    "time_complexity": "O(m * n)",
    "space_complexity": "O(m * n)",
    "description": "Given a grid where 0 represents water and 1 represents land, return a grid of the same size where each cell contains the height of the highest peak.",
}

from collections import deque

def solve(grid: list[list[int]]) -> list[list[int]]:
    """
    Computes the height of the highest peak for each cell in a grid using multi-source BFS.

    Args:
        grid: A 2D list of integers where 0 represents water and 1 represents land.

    Returns:
        A 2D list of integers representing the height of the highest peak for each cell.

    Examples:
        >>> solve([[0, 0, 1], [0, 0, 0], [0, 1, 0]])
        [[1, 1, 0], [2, 1, 1], [1, 0, 1]]
    """
    rows = len(grid)
    cols = len(grid[0])
    
    # Initialize heights with -1 to represent unvisited cells
    heights = [[-1 for _ in range(cols)] for _ in range(rows)]
    queue = deque()

    # Multi-source BFS initialization:
    # All water cells (0) are the starting points with height 0.
    # All land cells (1) are treated as potential peaks, but we start BFS from water.
    # Actually, the problem defines water as height 0. We find distances from water.
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 0:
                heights[r][c] = 0
                queue.append((r, c))

    # Directions for 4-connectivity (up, down, left, right)
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    while queue:
        curr_r, curr_c = queue.popleft()
        
        for dr, dc in directions:
            nr, nc = curr_r + dr, curr_c + dc
            
            # If the neighbor is within bounds and hasn't been visited yet
            if 0 <= nr < rows and 0 <= nc < cols and heights[nr][nc] == -1:
                # The height of the neighbor is the current cell's height + 1
                heights[nr][nc] = heights[curr_r][curr_c] + 1
                queue.append((nr, nc))
                
    return heights
