METADATA = {
    "id": 1730,
    "name": "Shortest Path to Get Food",
    "slug": "shortest_path_to_get_food",
    "category": "graph",
    "aliases": [],
    "tags": ["bfs", "graphs"],
    "difficulty": "medium",
    "time_complexity": "O(m * n)",
    "space_complexity": "O(m * n)",
    "description": "Find the minimum number of steps required to reach a food cell in a grid.",
}


from collections import deque
from typing import List, Tuple


def solve(grid: List[List[str]]) -> int:
    """Find the shortest path from the starting cell to any food cell.

    Args:
        grid: A 2‑D list representing the map where
            'W' denotes water (impassable),
            'L' denotes land (passable),
            'F' denotes food (target),
            '*' denotes the starting position (also land).

    Returns:
        The minimum number of steps required to reach a food cell.
        Returns -1 if no food is reachable.

    Examples:
        >>> solve([['*','L','L'],['W','W','L'],['L','F','L']])
        3
        >>> solve([['*','W','F']])
        -1
    """
    if not grid or not grid[0]:
        return -1

    rows: int = len(grid)
    cols: int = len(grid[0])

    # Locate the starting position.
    start_row: int = -1
    start_col: int = -1
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '*':
                start_row, start_col = r, c
                break
        if start_row != -1:
            break

    if start_row == -1:
        return -1  # No starting point found.

    # BFS initialization.
    queue: deque[Tuple[int, int, int]] = deque()
    queue.append((start_row, start_col, 0))
    visited: List[List[bool]] = [[False] * cols for _ in range(rows)]
    visited[start_row][start_col] = True

    # Directions: up, down, left, right.
    direction_offsets: List[Tuple[int, int]] = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while queue:
        current_row, current_col, distance = queue.popleft()

        # If we have reached food, return the distance.
        if grid[current_row][current_col] == 'F':
            return distance

        # Explore neighboring cells.
        for dr, dc in direction_offsets:
            next_row: int = current_row + dr
            next_col: int = current_col + dc

            # Check bounds and passability.
            if 0 <= next_row < rows and 0 <= next_col < cols:
                if not visited[next_row][next_col] and grid[next_row][next_col] != 'W':
                    visited[next_row][next_col] = True
                    queue.append((next_row, next_col, distance + 1))

    # No reachable food found.
    return -1