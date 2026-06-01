METADATA = {
    "id": 407,
    "name": "Trapping Rain Water II",
    "slug": "trapping-rain-water-ii",
    "category": "Hard",
    "aliases": [],
    "tags": ["priority_queue", "bfs", "matrix", "heap"],
    "difficulty": "hard",
    "time_complexity": "O(m*n log(m*n))",
    "space_complexity": "O(m*n)",
    "description": "Calculate the volume of water trapped in a 3D terrain represented by a 2D grid of heights.",
}

import heapq

def solve(heightMap: list[list[int]]) -> int:
    """
    Calculates the total volume of water trapped in a 3D terrain.

    The algorithm uses a Min-Priority Queue to simulate the process of water 
    filling from the boundaries inward. We always process the lowest cell 
    on the current 'boundary' to ensure that water cannot leak out at a 
    lower point.

    Args:
        heightMap: A 2D grid of integers representing the height of the terrain.

    Returns:
        The total volume of water trapped.

    Examples:
        >>> solve([[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]])
        4
        >>> solve([[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]])
        4
    """
    if not heightMap or not heightMap[0]:
        return 0

    rows = len(heightMap)
    cols = len(heightMap[0])
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    min_heap = []

    # Add all boundary cells to the priority queue
    for r in range(rows):
        for c in range(cols):
            if r == 0 or r == rows - 1 or c == 0 or c == cols - 1:
                heapq.heappush(min_heap, (heightMap[r][c], r, c))
                visited[r][c] = True

    total_water = 0
    # The current boundary height level we are processing
    current_max_boundary_height = 0

    # Directions for 4-connectivity (up, down, left, right)
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    while min_heap:
        height, r, c = heapq.heappop(min_heap)
        
        # The water level is determined by the maximum height seen on the boundary path
        current_max_boundary_height = max(current_max_boundary_height, height)

        for dr, dc in directions:
            nr, nc = r + dr, c + dc

            # Check bounds and if the cell has been visited
            if 0 <= nr < rows and 0 <= nc < cols and not visited[nr][nc]:
                visited[nr][nc] = True
                
                # If the neighbor is lower than the current boundary height, it traps water
                if heightMap[nr][nc] < current_max_boundary_height:
                    total_water += current_max_boundary_height - heightMap[nr][nc]
                
                # Push the neighbor into the heap. 
                # We push the actual height to maintain the priority queue logic.
                heapq.heappush(min_heap, (heightMap[nr][nc], nr, nc))

    return total_water
