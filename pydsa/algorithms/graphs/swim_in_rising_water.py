METADATA = {
    "id": 778,
    "name": "Swim in Rising Water",
    "slug": "swim-in-rising-water",
    "category": "Graph",
    "aliases": [],
    "tags": ["heap", "dijkstra", "bfs", "union_find"],
    "difficulty": "hard",
    "time_complexity": "O(n^2 log n)",
    "space_complexity": "O(n^2)",
    "description": "Find the minimum time required to reach the bottom-right corner from the top-left corner in a grid where each cell has an elevation.",
}

import heapq

def solve(grid: list[list[int]]) -> int:
    """
    Finds the minimum time required to swim from (0, 0) to (n-1, n-1).
    
    The problem is modeled as finding a path where the maximum value on the path 
    is minimized. This is a classic application of Dijkstra's algorithm 
    (or a modified Prim's algorithm) where the 'distance' to a cell is the 
    maximum elevation encountered on the path to it.

    Args:
        grid: A 2D list of integers representing the elevation of each cell.

    Returns:
        The minimum time (maximum elevation) required to reach the destination.

    Examples:
        >>> solve([[0,1],[2,3]])
        3
        >>> solve([[0,1,2],[2,2,2],[3,3,0]])
        3
    """
    n = len(grid)
    # Min-heap stores (max_elevation_so_far, row, col)
    # We use a heap to always expand the path with the smallest "bottleneck" elevation.
    min_heap = [(grid[0][0], 0, 0)]
    
    # visited keeps track of cells we have already processed to avoid cycles
    visited = [[False for _ in range(n)] for _ in range(n)]
    visited[0][0] = True
    
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    
    while min_heap:
        current_max_elevation, r, c = heapq.heappop(min_heap)
        
        # If we reached the destination, this is the minimum possible max elevation
        if r == n - 1 and c == n - 1:
            return current_max_elevation
        
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            
            if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc]:
                visited[nr][nc] = True
                # The max elevation for the neighbor is the max of the current path's 
                # max elevation and the neighbor's own elevation.
                new_max = max(current_max_elevation, grid[nr][nc])
                heapq.heappush(min_heap, (new_max, nr, nc))
                
    return -1  # Should not be reached given problem constraints