METADATA = {
    "id": 3905,
    "name": "Multi Source Flood Fill",
    "slug": "multi_source_flood_fill",
    "category": "Breadth-First Search",
    "aliases": [],
    "tags": ["bfs", "grid", "multi_source_bfs"],
    "difficulty": "medium",
    "time_complexity": "O(m * n)",
    "space_complexity": "O(m * n)",
    "description": "Perform a multi-source flood fill starting from all specified source cells simultaneously to calculate distances or fill values in a grid.",
}

from collections import deque

def solve(grid: list[list[int]], sources: list[list[int]]) -> list[list[int]]:
    """
    Performs a multi-source BFS to fill the grid with distances from the nearest source.

    Args:
        grid: A 2D list of integers representing the grid.
        sources: A list of [row, col] coordinates representing the starting points.

    Returns:
        A 2D list of integers where each cell contains the shortest distance to a source.

    Examples:
        >>> grid = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        >>> sources = [[0, 0], [2, 2]]
        >>> solve(grid, sources)
        [[0, 1, 2], [1, 2, 1], [2, 1, 0]]
    """
    if not grid or not grid[0]:
        return []

    rows = len(grid)
    cols = len(grid[0])
    
    # Initialize distances with a value representing 'unvisited'
    # Using -1 to distinguish between unvisited and distance 0
    distances = [[-1 for _ in range(cols)] for _ in range(rows)]
    queue = deque()

    # Add all source cells to the queue initially for multi-source BFS
    for r, c in sources:
        if 0 <= r < rows and 0 <= c < cols:
            distances[r][c] = 0
            queue.append((r, c))

    # Directions for 4-connectivity (up, down, left, right)
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    while queue:
        curr_r, curr_c = queue.popleft()
        curr_dist = distances[curr_r][curr_c]

        for dr, dc in directions:
            nr, nc = curr_r + dr, curr_c + dc

            # Check boundaries and if the cell has been visited
            if 0 <= nr < rows and 0 <= nc < cols and distances[nr][nc] == -1:
                # Update distance and add to queue to expand layer by layer
                distances[nr][nc] = curr_dist + 1
                queue.append((nr, nc))

    return distances
