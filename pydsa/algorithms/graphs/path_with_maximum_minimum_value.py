METADATA = {
    "id": 1102,
    "name": "Path With Maximum Minimum Value",
    "slug": "path-with-maximum-minimum-value",
    "category": "Graph",
    "aliases": [],
    "tags": ["priority_queue", "bfs", "greedy", "graph"],
    "difficulty": "medium",
    "time_complexity": "O(mn log(mn))",
    "space_complexity": "O(mn)",
    "description": "Find a path from the top-left to the bottom-right cell such that the minimum value encountered on the path is maximized.",
}

import heapq

def solve(grid: list[list[int]]) -> int:
    """
    Finds a path from (0, 0) to (R-1, C-1) that maximizes the minimum value on the path.

    Args:
        grid: A 2D list of integers representing the values in the grid.

    Returns:
        The maximum possible minimum value along any path from the start to the end.

    Examples:
        >>> solve([[5, 4, 5], [1, 2, 6]])
        4
        >>> solve([[0, 0], [0, 0]])
        0
    """
    if not grid or not grid[0]:
        return 0

    rows = len(grid)
    cols = len(grid[0])
    
    # Max-priority queue to store (-value, r, c). 
    # We use negative values because Python's heapq is a min-heap.
    # This allows us to always expand the cell with the highest value first (Greedy).
    max_heap = [(-grid[0][0], 0, 0)]
    
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    visited[0][0] = True
    
    # The answer is the minimum value encountered so far on the current path.
    # Since we always pick the largest available neighbor, the first time we 
    # reach the destination, the bottleneck (minimum) will be maximized.
    min_val_on_path = grid[0][0]
    
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    while max_heap:
        current_val_neg, r, c = heapq.heappop(max_heap)
        current_val = -current_val_neg
        
        # Update the bottleneck value for the path we are building
        min_val_on_path = min(min_val_on_path, current_val)
        
        # If we reached the bottom-right corner, return the bottleneck
        if r == rows - 1 and c == cols - 1:
            return min_val_on_path
        
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            
            if 0 <= nr < rows and 0 <= nc < cols and not visited[nr][nc]:
                visited[nr][nc] = True
                # Push neighbor into heap to explore the highest available values next
                heapq.heappush(max_heap, (-grid[nr][nc], nr, nc))
                
    return 0
