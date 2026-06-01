METADATA = {
    "id": 1293,
    "name": "Shortest Path in a Grid with Obstacles Elimination",
    "slug": "shortest-path-in-a-grid-with-obstacles-elimination",
    "category": "Graph",
    "aliases": [],
    "tags": ["bfs", "matrix", "graph"],
    "difficulty": "hard",
    "time_complexity": "O(m * n * k)",
    "space_complexity": "O(m * n * k)",
    "description": "Find the shortest path from the top-left to the bottom-right of a grid, allowing up to k obstacle removals.",
}

from collections import deque

def solve(grid: list[list[int]], k: int) -> int:
    """
    Finds the shortest path in a grid from (0, 0) to (m-1, n-1) allowing up to k obstacle removals.

    Args:
        grid: A 2D list of integers where 0 is empty and 1 is an obstacle.
        k: The maximum number of obstacles that can be removed.

    Returns:
        The length of the shortest path (number of steps), or -1 if no path exists.

    Examples:
        >>> solve([[0,0,0],[1,1,0],[0,0,0],[0,1,1],[0,0,0]], 1)
        6
        >>> solve([[0,1,0],[0,1,0],[0,1,0],[0,1,0],[0,0,0]], 0)
        -1
    """
    rows = len(grid)
    cols = len(grid[0])
    target_row, target_col = rows - 1, cols - 1

    # Optimization: If k is large enough to cover any Manhattan distance path,
    # the shortest path is simply the Manhattan distance.
    if k >= (rows - 1) + (cols - 1):
        return (rows - 1) + (cols - 1)

    # Queue stores (row, col, remaining_k, current_steps)
    queue = deque([(0, 0, k, 0)])
    
    # visited stores (row, col, remaining_k) to prevent redundant processing.
    # We use remaining_k because reaching a cell with more 'k' left is strictly better.
    # A set of (row, col, remaining_k) is sufficient.
    visited = {(0, 0, k)}

    while queue:
        r, c, rem_k, steps = queue.popleft()

        # Check if we reached the destination
        if r == target_row and c == target_col:
            return steps

        # Explore 4-directional neighbors
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nr, nc = r + dr, c + dc

            # Boundary check
            if 0 <= nr < rows and 0 <= nc < cols:
                new_k = rem_k - grid[nr][nc]

                # If we have enough k left and haven't visited this state
                if new_k >= 0 and (nr, nc, new_k) not in visited:
                    # Optimization: If we reach a cell with the same or more k, 
                    # we don't need to explore it again with less k.
                    # However, the standard BFS with (r, c, k) state handles this.
                    visited.add((nr, nc, new_k))
                    queue.append((nr, nc, new_k, steps + 1))

    return -1
