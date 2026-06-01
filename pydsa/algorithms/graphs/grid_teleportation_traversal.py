METADATA = {
    "id": 3552,
    "name": "Grid Teleportation Traversal",
    "slug": "grid-teleportation-traversal",
    "category": "Graphs",
    "aliases": [],
    "tags": ["bfs", "graphs", "shortest-path"],
    "difficulty": "medium",
    "time_complexity": "O(R * C + T)",
    "space_complexity": "O(R * C + T)",
    "description": "Find the shortest path in a grid containing obstacles and teleportation portals using BFS.",
}

from collections import deque


def solve(
    rows: int,
    cols: int,
    grid: list[list[int]],
    start: tuple[int, int],
    target: tuple[int, int],
    teleports: dict[tuple[int, int], list[tuple[int, int]]],
) -> int:
    """
    Finds the shortest path from start to target in a grid with teleports.

    Args:
        rows: Number of rows in the grid.
        cols: Number of columns in the grid.
        grid: 2D list where 0 is empty, 1 is an obstacle.
        start: (r, c) starting coordinates.
        target: (r, c) target coordinates.
        teleports: Dictionary mapping (r, c) to a list of (r, c) destinations.

    Returns:
        The minimum number of steps to reach target, or -1 if unreachable.

    Examples:
        >>> solve(3, 3, [[0,0,0],[0,1,0],[0,0,0]], (0,0), (2,2), {})
        4
        >>> solve(3, 3, [[0,0,0],[0,1,0],[0,0,0]], (0,0), (2,2), {(0,0): [(2,2)]})
        1
    """
    # Standard BFS setup
    queue = deque([(start[0], start[1], 0)])
    visited = set()
    visited.add(start)

    # Directions for 4-way movement
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    while queue:
        curr_r, curr_c, dist = queue.popleft()

        if (curr_r, curr_c) == target:
            return dist

        # 1. Try moving to adjacent cells
        for dr, dc in directions:
            nr, nc = curr_r + dr, curr_c + dc

            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 0:
                if (nr, nc) not in visited:
                    visited.add((nr, nc))
                    queue.append((nr, nc, dist + 1))

        # 2. Try using teleports if the current cell is a portal entrance
        if (curr_r, curr_c) in teleports:
            for tr, tc in teleports[(curr_r, curr_c)]:
                if 0 <= tr < rows and 0 <= tc < cols and grid[tr][tc] == 0:
                    if (tr, tc) not in visited:
                        visited.add((tr, tc))
                        # Teleportation counts as 1 step (moving from entrance to exit)
                        queue.append((tr, tc, dist + 1))

    return -1
