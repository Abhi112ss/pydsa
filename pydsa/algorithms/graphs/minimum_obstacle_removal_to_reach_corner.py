METADATA = {
    "id": 2290,
    "name": "Minimum Obstacle Removal to Reach Corner",
    "slug": "minimum-obstacle-removal-to-reach-corner",
    "category": "Graph",
    "aliases": [],
    "tags": ["bfs", "01_bfs", "shortest_path", "deque"],
    "difficulty": "medium",
    "time_complexity": "O(m * n)",
    "space_complexity": "O(m * n)",
    "description": "Find the minimum number of obstacles to remove to reach the bottom-right corner from the top-left corner of a grid.",
}

from collections import deque

def solve(grid: list[list[int]]) -> int:
    """
    Finds the minimum number of obstacles to remove to reach the bottom-right corner.

    This implementation uses a 0-1 Breadth-First Search (BFS) algorithm. 
    Since the edge weights are only 0 (empty cell) or 1 (obstacle), a deque 
    allows us to maintain the shortest path property by adding 0-weight 
    edges to the front and 1-weight edges to the back.

    Args:
        grid: A 2D list of integers where 0 represents an empty cell and 1 represents an obstacle.

    Returns:
        The minimum number of obstacles to remove to reach (rows-1, cols-1) from (0, 0).

    Examples:
        >>> solve([[0,1,0],[1,1,0],[0,0,0]])
        1
        >>> solve([[0,1],[1,1]])
        1
    """
    rows = len(grid)
    cols = len(grid[0])
    
    # distance[r][c] stores the minimum obstacles removed to reach cell (r, c)
    # Initialize with infinity
    distances = [[float('inf')] * cols for _ in range(rows)]
    distances[0][0] = 0
    
    # Deque for 0-1 BFS
    queue = deque([(0, 0)])
    
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    while queue:
        r, c = queue.popleft()
        
        # If we reached the target, we can return early because 0-1 BFS 
        # guarantees the first time we pop a node, it's the shortest path.
        if r == rows - 1 and c == cols - 1:
            return int(distances[r][c])
            
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            
            if 0 <= nr < rows and 0 <= nc < cols:
                # Weight is 0 if the cell is empty, 1 if it's an obstacle
                weight = grid[nr][nc]
                new_dist = distances[r][c] + weight
                
                # If we found a shorter path to the neighbor
                if new_dist < distances[nr][nc]:
                    distances[nr][nc] = new_dist
                    
                    # 0-1 BFS logic: 
                    # If weight is 0, add to front to process immediately (higher priority)
                    # If weight is 1, add to back (lower priority)
                    if weight == 0:
                        queue.appendleft((nr, nc))
                    else:
                        queue.append((nr, nc))
                        
    return int(distances[rows - 1][cols - 1])
