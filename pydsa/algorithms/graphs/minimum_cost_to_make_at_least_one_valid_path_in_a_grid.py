METADATA = {
    "id": 1368,
    "name": "Minimum Cost to Make at Least One Valid Path in a Grid",
    "slug": "minimum-cost-to-make-at-least-one-valid-path-in-a-grid",
    "category": "Graph",
    "aliases": [],
    "tags": ["dijkstra", "bfs", "graph", "priority queue"],
    "difficulty": "hard",
    "time_complexity": "O(m * n * log(m * n))",
    "space_complexity": "O(m * n)",
    "description": "Find the minimum cost to reach the bottom-right corner of a grid where changing direction costs 1 and following the arrow costs 0.",
}

import heapq

def solve(grid: list[list[int]]) -> int:
    """
    Finds the minimum cost to reach the bottom-right corner from the top-left.
    
    The grid contains arrows (1: right, 2: left, 3: down, 4: up). 
    Moving in the direction of the arrow costs 0. 
    Changing the direction to move to an adjacent cell costs 1.

    Args:
        grid: A 2D list of integers representing directions.

    Returns:
        The minimum cost to reach (rows-1, cols-1) from (0, 0).

    Examples:
        >>> solve([[1,1,1,1],[4,4,4,1],[1,1,1,1],[4,4,4,1]])
        0
        >>> solve([[1,1,1,1],[4,4,4,1],[1,1,1,1],[4,4,4,4]])
        3
    """
    rows = len(grid)
    cols = len(grid[0])
    
    # Directions mapping: 1: right, 2: left, 3: down, 4: up
    # Using (dr, dc) format
    directions = {
        1: (0, 1),
        2: (0, -1),
        3: (1, 0),
        4: (-1, 0)
    }
    
    # min_costs[r][c] stores the minimum cost to reach cell (r, c)
    min_costs = [[float('inf')] * cols for _ in range(rows)]
    min_costs[0][0] = 0
    
    # Priority Queue for Dijkstra: (cost, row, col)
    priority_queue = [(0, 0, 0)]
    
    while priority_queue:
        current_cost, r, c = heapq.heappop(priority_queue)
        
        # If we found a better path to this cell already, skip
        if current_cost > min_costs[r][c]:
            continue
            
        # Target reached
        if r == rows - 1 and c == cols - 1:
            return current_cost
            
        # Explore all 4 neighbors
        for direction_val, (dr, dc) in directions.items():
            nr, nc = r + dr, c + dc
            
            if 0 <= nr < rows and 0 <= nc < cols:
                # Cost is 0 if we follow the arrow, 1 if we change direction
                # Note: grid[r][c] is the direction at the CURRENT cell
                move_cost = 0 if grid[r][c] == direction_val else 1
                new_cost = current_cost + move_cost
                
                # If this path to (nr, nc) is cheaper than any previously found path
                if new_cost < min_costs[nr][nc]:
                    min_costs[nr][nc] = new_cost
                    heapq.heappush(priority_queue, (new_cost, nr, nc))
                    
    return min_costs[rows - 1][cols - 1]
