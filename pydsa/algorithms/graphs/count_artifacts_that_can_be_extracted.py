METADATA = {
    "id": 2201,
    "name": "Count Artifacts That Can Be Extracted",
    "slug": "count-artifacts-that-can-be-extracted",
    "category": "Graph",
    "aliases": [],
    "tags": ["dfs", "grid", "graph_traversal"],
    "difficulty": "hard",
    "time_complexity": "O(m * n)",
    "space_complexity": "O(m * n)",
    "description": "Count the number of artifacts that can be extracted from a grid by removing connected components of empty cells that touch the boundary.",
}

def solve(grid: list[list[int]]) -> int:
    """
    Counts the number of artifacts that can be extracted from a grid.
    An artifact is extractable if it is adjacent to a connected component of 
    empty cells (0s) that reaches the boundary of the grid.

    Args:
        grid: A 2D list of integers where 1 represents an artifact and 0 represents empty space.

    Returns:
        The total number of artifacts that can be extracted.

    Examples:
        >>> solve([[1, 0, 1], [1, 1, 1], [0, 0, 1]])
        2
        >>> solve([[1, 1, 1], [1, 1, 1], [1, 1, 1]])
        0
    """
    rows = len(grid)
    cols = len(grid[0])
    
    # visited keeps track of empty cells (0s) that have been processed
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    
    # reachable_empty[r][c] is True if the empty cell (r, c) is part of a 
    # connected component of 0s that touches the grid boundary.
    reachable_empty = [[False for _ in range(cols)] for _ in range(rows)]

    def bfs_boundary_empty(start_r: int, start_c: int):
        """Performs BFS to mark all empty cells in a component that touches the boundary."""
        queue = [(start_r, start_c)]
        visited[start_r][start_c] = True
        component = [(start_r, start_c)]
        touches_boundary = False
        
        idx = 0
        while idx < len(queue):
            r, c = queue[idx]
            idx += 1
            
            # Check if this cell is on the boundary
            if r == 0 or r == rows - 1 or c == 0 or c == cols - 1:
                touches_boundary = True
            
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and \
                   grid[nr][nc] == 0 and not visited[nr][nc]:
                    visited[nr][nc] = True
                    queue.append((nr, nc))
                    component.append((nr, nc))
        
        # If the component touches the boundary, all its cells are 'extractable' paths
        if touches_boundary:
            for r, c in component:
                reachable_empty[r][c] = True

    # Step 1: Identify all connected components of 0s and check if they touch the boundary
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 0 and not visited[r][c]:
                bfs_boundary_empty(r, c)

    # Step 2: Count artifacts (1s) that are adjacent to a reachable empty cell
    extractable_count = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                is_extractable = False
                for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and reachable_empty[nr][nc]:
                        is_extractable = True
                        break
                if is_extractable:
                    extractable_count += 1
                    
    return extractable_count
