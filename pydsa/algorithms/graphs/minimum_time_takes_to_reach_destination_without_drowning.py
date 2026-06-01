METADATA = {
    "id": 2814,
    "name": "Minimum Time Takes to Reach Destination Without Drowning",
    "slug": "minimum-time-takes-to-reach-destination-without-drowning",
    "category": "Graphs",
    "aliases": [],
    "tags": ["bfs", "graphs", "shortest path"],
    "difficulty": "medium",
    "time_complexity": "O(m * n)",
    "space_complexity": "O(m * n)",
    "description": "Find the minimum time to reach the bottom-right cell from the top-left cell such that the time taken is always strictly less than the water level at each cell.",
}

from collections import deque

def solve(heights: list[list[int]], distance: int) -> int:
    """
    Finds the minimum time to reach the destination (m-1, n-1) from (0, 0).
    The time taken to reach a cell must be strictly less than the height of that cell.

    Args:
        heights: A 2D grid where heights[i][j] represents the water level at cell (i, j).
        distance: The maximum allowed time/distance to reach the destination.

    Returns:
        The minimum time to reach the destination, or -1 if it is impossible.

    Examples:
        >>> solve([[10, 10, 10], [10, 1, 10], [10, 10, 10]], 5)
        4
        >>> solve([[1, 1], [1, 1]], 5)
        -1
    """
    rows = len(heights)
    cols = len(heights[0])
    
    # If the starting cell's water level is not greater than 0, we drown immediately.
    if heights[0][0] <= 0:
        return -1

    # Queue stores (row, col, current_time)
    queue = deque([(0, 0, 0)])
    # Visited set to prevent cycles and redundant processing
    visited = {(0, 0)}

    while queue:
        r, c, time = queue.popleft()

        # Check if we reached the destination
        if r == rows - 1 and c == cols - 1:
            return time

        # Explore 4-directional neighbors
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nr, nc = r + dr, c + dc

            # Check boundaries and if the cell has been visited
            if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited:
                new_time = time + 1
                
                # The core constraint: time taken must be strictly less than the water level
                # and the total time must not exceed the allowed distance.
                if new_time < heights[nr][nc] and new_time <= distance:
                    visited.add((nr, nc))
                    queue.append((nr, nc, new_time))

    return -1
