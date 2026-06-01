METADATA = {
    "id": 2371,
    "name": "Minimize Maximum Value in a Grid",
    "slug": "minimize-maximum-value-in-a-grid",
    "category": "Medium",
    "aliases": [],
    "tags": ["binary_search", "bfs", "priority_queue", "graph", "dijkstra"],
    "difficulty": "medium",
    "time_complexity": "O(n^2 log(max_val))",
    "space_complexity": "O(n^2)",
    "description": "Find the minimum possible maximum value in a grid such that there is a path from (0,0) to (n-1, n-1) following specific movement rules.",
}

import heapq

def solve(grid: list[list[int]]) -> int:
    """
    Finds the minimum possible maximum value in a path from (0,0) to (n-1, n-1).

    The problem asks to minimize the maximum value encountered on a path. 
    This is a classic application of Dijkstra's algorithm or a modified BFS 
    where we track the 'bottleneck' value of the path.

    Args:
        grid: A 2D list of integers representing the grid values.

    Returns:
        The minimum possible maximum value on a path from the top-left to the bottom-right.

    Examples:
        >>> solve([[1,2,3],[4,5,6],[7,8,9]])
        9
        >>> solve([[1,1,1],[1,1,1],[1,1,1]])
        1
    """
    rows = len(grid)
    cols = len(grid[0])
    
    # min_max_val[r][c] stores the minimum possible 'maximum value' seen on a path to (r, c)
    # Initialize with infinity to represent unvisited cells
    min_max_val = [[float('inf')] * cols for _ in range(rows)]
    
    # Priority Queue stores (current_max_on_path, r, c)
    # We use a min-heap to always expand the path with the smallest "maximum value"
    priority_queue = [(grid[0][0], 0, 0)]
    min_max_val[0][0] = grid[0][0]
    
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    
    while priority_queue:
        current_max, r, c = heapq.heappop(priority_queue)
        
        # If we reached the destination, this is the optimal answer due to Dijkstra's property
        if r == rows - 1 and c == cols - 1:
            return current_max
            
        # If we found a better path to this cell already, skip
        if current_max > min_max_val[r][c]:
            continue
            
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            
            if 0 <= nr < rows and 0 <= nc < cols:
                # The maximum value on the path to the neighbor is the max of 
                # the current path's max and the neighbor's own value
                new_max = max(current_max, grid[nr][nc])
                
                # If this new path offers a smaller 'maximum value' for the neighbor, update it
                if new_max < min_max_val[nr][nc]:
                    min_max_val[nr][nc] = new_max
                    heapq.heappush(priority_queue, (new_max, nr, nc))
                    
    return -1  # Should not be reached given problem constraints