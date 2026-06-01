METADATA = {
    "id": 2257,
    "name": "Count Unguarded Cells in the Grid",
    "slug": "count-unguarded-cells-in-the-grid",
    "category": "Breadth-First Search",
    "aliases": [],
    "tags": ["bfs", "grid", "matrix"],
    "difficulty": "medium",
    "time_complexity": "O(m * n)",
    "space_complexity": "O(m * n)",
    "description": "Count the number of empty cells in a grid that cannot be reached by any guard via horizontal or vertical movement.",
}

from collections import deque

def solve(grid: list[list[int]]) -> int:
    """
    Counts the number of unguarded cells in a grid using multi-source BFS.

    A cell is unguarded if it is empty (0) and cannot be reached by any guard (2)
    moving only horizontally or vertically. Obstacles (1) block movement.

    Args:
        grid: A 2D list of integers where 0 is empty, 1 is obstacle, and 2 is guard.

    Returns:
        The total count of unguarded empty cells.

    Examples:
        >>> solve([[2,1,0],[0,0,1],[1,0,0]])
        3
        >>> solve([[0,0,0],[0,0,0],[0,0,0]])
        9
    """
    if not grid or not grid[0]:
        return 0

    rows = len(grid)
    cols = len(grid[0])
    
    # visited will track cells that are either guards or reachable by guards
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    queue = deque()
    
    empty_cells_count = 0

    # Step 1: Initialize BFS queue with all guard positions and count empty cells
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 2:
                queue.append((r, c))
                visited[r][c] = True
            elif grid[r][c] == 0:
                empty_cells_count += 1

    # Step 2: Multi-source BFS to mark all reachable cells
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    
    while queue:
        curr_r, curr_c = queue.popleft()
        
        for dr, dc in directions:
            nr, nc = curr_r + dr, curr_c + dc
            
            # Check bounds, ensure it's not an obstacle, and not already visited
            if 0 <= nr < rows and 0 <= nc < cols:
                if not visited[nr][nc] and grid[nr][nc] == 0:
                    visited[nr][nc] = True
                    queue.append((nr, nc))
                    # Since this empty cell is now reachable, it is no longer unguarded
                    empty_cells_count -= 1

    return empty_cells_count
