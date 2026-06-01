METADATA = {
    "id": 2812,
    "name": "Find the Safest Path in a Grid",
    "slug": "find_the_safest_path_in_a_grid",
    "category": "Graphs",
    "aliases": [],
    "tags": ["bfs", "priority_queue", "graphs", "dijkstra"],
    "difficulty": "hard",
    "time_complexity": "O(m*n log(m*n))",
    "space_complexity": "O(m*n)",
    "description": "Find a path from (0,0) to (n-1,n-1) that maximizes the minimum distance to any thief encountered along the path.",
}

import heapq

def solve(grid: list[list[int]]) -> int:
    """
    Finds the maximum possible safety value for a path from the top-left to the bottom-right.
    The safety value of a path is the minimum distance to any thief among all cells in the path.

    Args:
        grid: An n x n integer grid where 1 represents a thief and 0 represents an empty cell.

    Returns:
        The maximum safety value possible for a path from (0, 0) to (n-1, n-1).

    Examples:
        >>> solve([[0, 0, 0], [0, 1, 0], [0, 0, 0]])
        1
        >>> solve([[0, 1, 0], [0, 0, 0], [0, 0, 0]])
        1
    """
    n = len(grid)
    thief_distances = [[-1] * n for _ in range(n)]
    thief_queue = []

    # Step 1: Multi-source BFS to calculate distance from every cell to the nearest thief
    for r in range(n):
        for c in range(n):
            if grid[r][c] == 1:
                thief_distances[r][c] = 0
                heapq.heappush(thief_queue, (0, r, c))

    # Standard BFS using a queue (using heapq here for consistency, but collections.deque is fine)
    # Since all edge weights are 1, BFS is O(N^2)
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    
    # Using a simple list as a queue for BFS since we are doing level-order
    bfs_queue = []
    for r in range(n):
        for c in range(n):
            if grid[r][c] == 1:
                bfs_queue.append((r, c))
    
    head = 0
    while head < len(bfs_queue):
        r, c = bfs_queue[head]
        head += 1
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < n and thief_distances[nr][nc] == -1:
                thief_distances[nr][nc] = thief_distances[r][c] + 1
                bfs_queue.append((nr, nc))

    # Step 2: Dijkstra-like approach to find the path that maximizes the minimum distance
    # We use a Max-Heap to always explore the cell with the highest current safety value
    # Python's heapq is a min-heap, so we store negative values to simulate a max-heap
    max_heap = [(-thief_distances[0][0], 0, 0)]
    visited = [[False] * n for _ in range(n)]
    visited[0][0] = True

    while max_heap:
        current_safety, r, c = heapq.heappop(max_heap)
        current_safety = -current_safety

        # If we reached the destination, this is the maximum possible safety value
        if r == n - 1 and c == n - 1:
            return current_safety

        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc]:
                visited[nr][nc] = True
                # The safety of the path to the neighbor is the minimum of 
                # the current path's safety and the neighbor's distance to a thief
                new_safety = min(current_safety, thief_distances[nr][nc])
                heapq.heappush(max_heap, (-new_safety, nr, nc))

    return 0
