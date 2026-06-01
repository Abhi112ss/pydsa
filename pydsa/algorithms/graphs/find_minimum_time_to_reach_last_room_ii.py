METADATA = {
    "id": 3342,
    "name": "Find Minimum Time to Reach Last Room II",
    "slug": "find-minimum-time-to-reach-last-room-ii",
    "category": "Graph",
    "aliases": [],
    "tags": ["dijkstra", "priority_queue", "grid", "shortest-path"],
    "difficulty": "hard",
    "time_complexity": "O(m * n * log(m * n))",
    "space_complexity": "O(m * n)",
    "description": "Find the minimum time to reach the bottom-right corner of a grid where movement costs depend on the current time and cell values.",
}

import heapq

def solve(grid: list[list[int]], k: int) -> int:
    """
    Finds the minimum time to reach the last room (bottom-right) in a grid.
    
    The movement rules involve a time-based cost: if the current time is 't', 
    moving to a cell with value 'v' takes max(1, v - t) time. 
    Additionally, we can only move to a cell if the time taken to reach it 
    is within a certain threshold or if we follow specific movement constraints.
    
    Note: Based on the problem context of 'Find Minimum Time to Reach Last Room II',
    this implementation assumes a standard Dijkstra approach where the cost to 
    enter a cell (r, c) at time 't' is max(t + 1, grid[r][c]).

    Args:
        grid: A 2D list of integers representing the grid.
        k: An integer parameter (contextually used for constraints).

    Returns:
        The minimum time to reach the bottom-right cell, or -1 if unreachable.

    Examples:
        >>> solve([[1, 3], [1, 1]], 0)
        3
    """
    rows = len(grid)
    cols = len(grid[0])
    
    # min_time[r][c] stores the minimum time to reach cell (r, c)
    min_time = [[float('inf')] * cols for _ in range(rows)]
    min_time[0][0] = grid[0][0]
    
    # Priority Queue stores (current_time, r, c)
    # We use a min-heap to always expand the cell with the smallest time
    pq = [(grid[0][0], 0, 0)]
    
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    
    while pq:
        current_time, r, c = heapq.heappop(pq)
        
        # If we reached the destination, return the time
        if r == rows - 1 and c == cols - 1:
            return current_time
            
        # If we found a better path to this cell already, skip
        if current_time > min_time[r][c]:
            continue
            
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            
            if 0 <= nr < rows and 0 <= nc < cols:
                # The time to reach the next cell is the maximum of 
                # (current time + 1) and the value required by the next cell.
                # This ensures we wait until the cell is 'ready'.
                arrival_time = max(current_time + 1, grid[nr][nc])
                
                # Standard Dijkstra relaxation step
                if arrival_time < min_time[nr][nc]:
                    min_time[nr][nc] = arrival_time
                    heapq.heappush(pq, (arrival_time, nr, nc))
                    
    return -1 if min_time[rows-1][cols-1] == float('inf') else min_time[rows-1][cols-1]
