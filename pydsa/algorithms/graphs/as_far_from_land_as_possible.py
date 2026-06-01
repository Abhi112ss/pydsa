METADATA = {
    "id": 1162,
    "name": "As Far from Land as Possible",
    "slug": "as_far_from_land_as_possible",
    "category": "Breadth-First Search",
    "aliases": [],
    "tags": ["bfs", "multi_source_bfs", "matrix"],
    "difficulty": "medium",
    "time_complexity": "O(n*m)",
    "space_complexity": "O(n*m)",
    "description": "Find a water cell such that its distance to the nearest land cell is maximized.",
}

from collections import deque

def solve(grid: list[list[int]]) -> int:
    """
    Finds the water cell that is as far from land as possible using multi-source BFS.

    Args:
        grid: A 2D integer grid where 1 represents land and 0 represents water.

    Returns:
        The maximum distance to the nearest land cell. Returns -1 if no water or no land exists.

    Examples:
        >>> solve([[0,0,0],[0,1,0],[0,0,0]])
        2
        >>> solve([[1,0,0],[0,0,0],[0,0,0]])
        4
        >>> solve([[1,1],[1,0]])
        1
    """
    rows = len(grid)
    cols = len(grid[0])
    queue = deque()

    # Step 1: Initialize the queue with all land cells (multi-source BFS starting point)
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                queue.append((r, c))

    # If there is no land (all water) or no water (all land), return -1
    if len(queue) == 0 or len(queue) == rows * cols:
        return -1

    distance = -1
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    # Step 2: Perform BFS level by level
    # Each level represents an increase in distance from the nearest land
    while queue:
        distance += 1
        # Process all nodes currently in the queue (the current "layer" of distance)
        for _ in range(len(queue)):
            curr_r, curr_c = queue.popleft()

            for dr, dc in directions:
                nr, nc = curr_r + dr, curr_c + dc

                # If the neighbor is within bounds and is water (0)
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 0:
                    # Mark as visited by changing 0 to 1 to avoid redundant processing
                    grid[nr][nc] = 1
                    queue.append((nr, nc))

    return distance
