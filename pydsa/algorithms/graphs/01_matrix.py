METADATA = {
    "id": 542,
    "name": "01 Matrix",
    "slug": "01-matrix",
    "category": "Breadth-First Search",
    "aliases": [],
    "tags": ["bfs", "dynamic_programming", "matrix"],
    "difficulty": "medium",
    "time_complexity": "O(m*n)",
    "space_complexity": "O(m*n)",
    "description": "Find the distance of the nearest 0 for each cell in a binary matrix.",
}

from collections import deque

def solve(mat: list[list[int]]) -> list[list[int]]:
    """
    Finds the distance of the nearest 0 for each cell in a binary matrix using multi-source BFS.

    Args:
        mat: A 2D list of integers where each element is either 0 or 1.

    Returns:
        A 2D list of integers representing the distance to the nearest 0 for each cell.

    Examples:
        >>> solve([[0,0,0],[0,1,0],[1,1,1]])
        [[0, 0, 0], [0, 1, 0], [1, 2, 1]]
        >>> solve([[0,1],[1,0]])
        [[0, 1], [1, 0]]
    """
    if not mat or not mat[0]:
        return []

    rows = len(mat)
    cols = len(mat[0])
    
    # Initialize distances with a special value (e.g., -1) to indicate unvisited cells
    distances = [[-1 for _ in range(cols)] for _ in range(rows)]
    queue = deque()

    # Multi-source BFS initialization:
    # Add all cells containing 0 to the queue and set their distance to 0.
    # These act as the starting points for the breadth-first search.
    for r in range(rows):
        for c in range(cols):
            if mat[r][c] == 0:
                distances[r][c] = 0
                queue.append((r, c))

    # Directions for moving Up, Down, Left, Right
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    while queue:
        curr_r, curr_c = queue.popleft()

        for dr, dc in directions:
            nr, nc = curr_r + dr, curr_c + dc

            # If the neighbor is within bounds and has not been visited yet
            if 0 <= nr < rows and 0 <= nc < cols and distances[nr][nc] == -1:
                # The distance to the nearest 0 for the neighbor is the current cell's distance + 1
                distances[nr][nc] = distances[curr_r][curr_c] + 1
                queue.append((nr, nc))

    return distances
