METADATA = {
    "id": 2045,
    "name": "Second Minimum Time to Reach Destination",
    "slug": "second-minimum-time-to-reach-destination",
    "category": "Graph",
    "aliases": [],
    "tags": ["bfs", "graphs", "matrix"],
    "difficulty": "medium",
    "time_complexity": "O(m * n)",
    "space_complexity": "O(m * n)",
    "description": "Find the second minimum time to reach the bottom-right corner of a grid where each cell has a time value.",
}

from collections import deque

def solve(time: list[list[int]], direction: str) -> int:
    """
    Finds the second minimum time to reach the bottom-right corner from the top-left.
    
    The problem requires finding the second shortest path in terms of time. 
    Since all edge weights are positive and we move in a grid, we can use a 
    modified BFS that tracks both the minimum and second minimum time to reach 
    each cell.

    Args:
        time: A 2D grid of integers representing the time required to stay in each cell.
        direction: A string '8' or '4' indicating allowed movement (8 directions or 4).

    Returns:
        The second minimum time to reach the destination.

    Examples:
        >>> time = [[1,2,3],[4,5,6],[7,8,9]]
        >>> direction = "4"
        >>> solve(time, direction)
        12
    """
    rows = len(time)
    cols = len(time[0])
    
    # Define movement directions
    if direction == "4":
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    else:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]

    # dist1[r][c] stores the minimum time to reach (r, c)
    # dist2[r][c] stores the second minimum time to reach (r, c)
    dist1 = [[float('inf')] * cols for _ in range(rows)]
    dist2 = [[float('inf')] * cols for _ in range(rows)]
    
    # Queue stores (current_time, row, col)
    queue = deque([(0, 0, 0)])
    dist1[0][0] = 0
    
    while queue:
        current_time, r, c = queue.popleft()
        
        # If we found a time greater than the current recorded minimum, 
        # it might be a candidate for the second minimum.
        if current_time > dist1[r][c] and current_time < dist2[r][c]:
            dist2[r][c] = current_time
            
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            
            if 0 <= nr < rows and 0 <= nc < cols:
                # The time to move to the next cell is the current time 
                # plus the time value of the next cell.
                # Note: The problem implies we must spend 'time[nr][nc]' 
                # to move into that cell.
                new_time = current_time + time[nr][nc]
                
                # Standard BFS logic for finding two shortest paths:
                # 1. If new_time is strictly better than the best known time
                if new_time < dist1[nr][nc]:
                    # The old best becomes the new second best
                    dist2[nr][nc] = dist1[nr][nc]
                    dist1[nr][nc] = new_time
                    queue.append((new_time, nr, nc))
                # 2. If new_time is better than the second best but not the best
                elif dist1[nr][nc] < new_time < dist2[nr][nc]:
                    dist2[nr][nc] = new_time
                    queue.append((new_time, nr, nc))
                    
    return int(dist2[rows - 1][cols - 1])
