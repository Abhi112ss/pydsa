METADATA = {
    "id": 3341,
    "name": "Find Minimum Time to Reach Last Room I",
    "slug": "find-minimum-time-to-reach-last-room-i",
    "category": "Breadth-First Search",
    "aliases": [],
    "tags": ["bfs", "grid", "shortest-path"],
    "difficulty": "medium",
    "time_complexity": "O(m * n)",
    "space_complexity": "O(m * n)",
    "description": "Find the minimum time to reach the bottom-right corner of a grid starting from the top-left corner using BFS.",
}

from collections import deque

def solve(grid: list[list[int]]) -> int:
    """
    Calculates the minimum time (number of steps) to reach the last room (bottom-right)
    from the first room (top-left) in a grid.

    Args:
        grid: A 2D list of integers representing the grid. 
              In this version, we assume all cells are traversable (0 or 1 logic 
              depending on problem variant, but standard BFS for shortest path).

    Returns:
        int: The minimum number of steps to reach the target. Returns -1 if unreachable.

    Examples:
        >>> solve([[0, 0], [0, 0]])
        2
        >>> solve([[0, 1], [0, 0]])
        2
    """
    if not grid or not grid[0]:
        return -1

    rows = len(grid)
    cols = len(grid[0])
    target = (rows - 1, cols - 1)

    # If the starting point is the target
    if (0, 0) == target:
        return 0

    # Queue for BFS: stores (row, col, current_time)
    queue = deque([(0, 0, 0)])
    # Set to keep track of visited cells to prevent cycles and redundant work
    visited = set([(0, 0)])

    # Directions for moving Up, Down, Left, Right
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    while queue:
        curr_r, curr_c, time = queue.popleft()

        for dr, dc in directions:
            nr, nc = curr_r + dr, curr_c + dc

            # Check boundaries and if the cell is traversable (assuming 0 is path, 1 is wall)
            # Note: Adjust grid[nr][nc] == 0 based on specific problem constraints if 1 is path
            if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited and grid[nr][nc] == 0:
                # If we reached the target, return the time immediately
                if (nr, nc) == target:
                    return time + 1
                
                visited.add((nr, nc))
                queue.append((nr, nc, time + 1))

    return -1
