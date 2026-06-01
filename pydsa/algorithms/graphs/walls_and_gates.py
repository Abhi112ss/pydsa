METADATA = {
    "id": 286,
    "name": "Walls and Gates",
    "slug": "walls-and-gates",
    "category": "Matrix",
    "aliases": [],
    "tags": ["bfs", "matrix", "shortest_path"],
    "difficulty": "medium",
    "time_complexity": "O(m*n)",
    "space_complexity": "O(m*n)",
    "description": "Fill each empty room in a grid with the distance to its nearest gate.",
}

from collections import deque

def solve(grid: list[list[int]]) -> None:
    """
    Fills each empty room in a grid with the distance to its nearest gate using multi-source BFS.

    Args:
        grid: A 2D list of integers where:
            - -1 represents a wall.
            - 0 represents a gate.
            - 2147483647 represents an empty room.

    Returns:
        None. The grid is modified in-place.

    Examples:
        >>> grid = [[2147483647, -1, 0], [2147483647, 2147483647, 2147483647], [2147483647, -1, 2147483647]]
        >>> solve(grid)
        >>> grid
        [[3, -1, 0], [2, 3, 1], [1, -1, 2]]
    """
    if not grid or not grid[0]:
        return

    rows = len(grid)
    cols = len(grid[0])
    queue = deque()
    EMPTY_ROOM = 2147483647
    GATE = 0

    # Step 1: Find all gates and add them to the queue as starting points for BFS
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == GATE:
                queue.append((r, c))

    # Step 2: Perform multi-source BFS
    # This ensures that when we reach an empty room, it's via the shortest path
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    
    while queue:
        curr_r, curr_c = queue.popleft()
        
        for dr, dc in directions:
            nr, nc = curr_r + dr, curr_c + dc
            
            # Check boundaries and if the cell is an unvisited empty room
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == EMPTY_ROOM:
                # Update distance and add to queue to explore its neighbors
                grid[nr][nc] = grid[curr_r][curr_c] + 1
                queue.append((nr, nc))
