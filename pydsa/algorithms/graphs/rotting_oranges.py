METADATA = {
    "id": 994,
    "name": "Rotting Oranges",
    "slug": "rotting-oranges",
    "category": "Breadth-First Search",
    "aliases": [],
    "tags": ["bfs", "matrix", "queue"],
    "difficulty": "medium",
    "time_complexity": "O(r * c)",
    "space_complexity": "O(r * c)",
    "description": "Determine the minimum number of minutes that must elapse until no fresh oranges are left, or return -1 if impossible.",
}

from collections import deque

def solve(grid: list[list[int]]) -> int:
    """
    Simulates the spread of rot using a multi-source Breadth-First Search.

    Args:
        grid: A 2D list where 0 is empty, 1 is fresh, and 2 is rotten.

    Returns:
        The minimum minutes elapsed until no fresh oranges remain, or -1 if impossible.

    Examples:
        >>> solve([[2,1,1],[1,1,0],[0,1,1]])
        4
        >>> solve([[2,1,1],[0,1,1],[1,0,1]])
        -1
        >>> solve([[0,2]])
        0
    """
    if not grid or not grid[0]:
        return 0

    rows = len(grid)
    cols = len(grid[0])
    queue = deque()
    fresh_count = 0

    # Initialize the queue with all initially rotten oranges and count fresh ones
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 2:
                queue.append((r, c))
            elif grid[r][c] == 1:
                fresh_count += 1

    # If there are no fresh oranges, 0 minutes have passed
    if fresh_count == 0:
        return 0

    minutes_elapsed = 0
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    # Perform multi-source BFS level by level
    while queue and fresh_count > 0:
        minutes_elapsed += 1
        # Process all oranges currently in the queue (one full minute's spread)
        for _ in range(len(queue)):
            curr_r, curr_c = queue.popleft()

            for dr, dc in directions:
                nr, nc = curr_r + dr, curr_c + dc

                # If neighbor is within bounds and is a fresh orange
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                    # Infect the orange and add to queue for next minute
                    grid[nr][nc] = 2
                    fresh_count -= 1
                    queue.append((nr, nc))

    # If fresh oranges remain, it's impossible to rot them all
    return minutes_elapsed if fresh_count == 0 else -1
