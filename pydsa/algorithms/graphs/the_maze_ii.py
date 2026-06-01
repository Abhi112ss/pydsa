METADATA = {
    "id": 505,
    "name": "The Maze II",
    "slug": "the-maze-ii",
    "category": "Graph",
    "aliases": [],
    "tags": ["dijkstra", "bfs", "shortest_path"],
    "difficulty": "hard",
    "time_complexity": "O(m * n * max(m, n))",
    "space_complexity": "O(m * n)",
    "description": "Find the shortest distance from a starting point to a destination in a maze where a ball rolls until it hits a wall.",
}

import heapq

def solve(maze: list[list[int]], start: list[int], destination: list[int]) -> int:
    """
    Finds the shortest distance for a ball to roll from start to destination.
    The ball rolls in a direction until it hits a wall.

    Args:
        maze: A 2D grid where 0 is empty space and 1 is a wall.
        start: The starting coordinates [row, col].
        destination: The destination coordinates [row, col].

    Returns:
        The shortest distance to the destination, or -1 if unreachable.

    Examples:
        >>> solve([[0,0,0,0,0],[1,1,0,1,1],[0,0,0,0,0],[0,1,1,1,0],[0,0,0,0,0]], [4,0], [0,0])
        12
    """
    rows = len(maze)
    cols = len(maze[0])
    
    # min_distances[r][c] stores the shortest distance found so far to reach cell (r, c)
    min_distances = [[float('inf')] * cols for _ in range(rows)]
    start_row, start_col = start[0], start[1]
    min_distances[start_row][start_col] = 0
    
    # Priority queue for Dijkstra: (distance, current_row, current_col)
    priority_queue = [(0, start_row, start_col)]
    
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    
    while priority_queue:
        current_dist, r, c = heapq.heappop(priority_queue)
        
        # If we found a longer path than already recorded, skip it
        if current_dist > min_distances[r][c]:
            continue
            
        # If we reached the destination, since we use Dijkstra, this is the shortest path
        if [r, c] == destination:
            return current_dist
            
        for dr, dc in directions:
            new_r, new_c = r, c
            step_count = 0
            
            # Simulate the ball rolling until it hits a wall or boundary
            while 0 <= new_r + dr < rows and 0 <= new_c + dc < cols and maze[new_r + dr][new_c + dc] == 0:
                new_r += dr
                new_c += dc
                step_count += 1
            
            # Calculate the total distance to the new stopping position
            total_dist = current_dist + step_count
            
            # If this path to the new stopping position is shorter, update and push to queue
            if total_dist < min_distances[new_r][new_c]:
                min_distances[new_r][new_c] = total_dist
                heapq.heappush(priority_queue, (total_dist, new_r, new_c))
                
    dest_r, dest_c = destination[0], destination[1]
    result = min_distances[dest_r][dest_c]
    return int(result) if result != float('inf') else -1
