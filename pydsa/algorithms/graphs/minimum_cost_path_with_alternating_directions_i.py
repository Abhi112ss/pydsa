METADATA = {
    "id": 3596,
    "name": "Minimum Cost Path with Alternating Directions I",
    "slug": "minimum-cost-path-with-alternating-directions-i",
    "category": "Graphs",
    "aliases": [],
    "tags": ["graphs", "dijkstra", "shortest-path"],
    "difficulty": "medium",
    "time_complexity": "O(E log V)",
    "space_complexity": "O(V)",
    "description": "Find the minimum cost to reach a target cell while alternating between horizontal and vertical movements.",
}

import heapq

def solve(grid: list[list[int]], start: list[int], target: list[int]) -> int:
    """
    Finds the minimum cost to travel from start to target in a grid, 
    alternating between horizontal and vertical moves at each step.

    Args:
        grid: A 2D list of integers representing the cost of entering each cell.
        start: A list of two integers [row, col] representing the starting position.
        target: A list of two integers [row, col] representing the target position.

    Returns:
        The minimum cost to reach the target, or -1 if the target is unreachable.

    Examples:
        >>> solve([[1, 1, 1], [1, 10, 1], [1, 1, 1]], [0, 0], [2, 2])
        5
    """
    rows = len(grid)
    cols = len(grid[0])
    start_row, start_col = start
    target_row, target_col = target

    # Priority Queue stores (current_cost, row, col, last_direction)
    # last_direction: 0 for horizontal, 1 for vertical, None for start
    # We use a tuple (cost, r, c, direction)
    pq = [(grid[start_row][start_col], start_row, start_col, None)]
    
    # dist[row][col][direction] stores min cost to reach (row, col) 
    # where the LAST move was 'direction' (0: horizontal, 1: vertical)
    # We use 2 for the initial state (no direction yet)
    dist = {}

    while pq:
        current_cost, r, c, last_dir = heapq.heappop(pq)

        if r == target_row and c == target_col:
            return current_cost

        # If we've found a cheaper way to reach this state, skip
        state = (r, c, last_dir)
        if state in dist and dist[state] <= current_cost:
            continue
        dist[state] = current_cost

        # Determine allowed directions:
        # If last move was horizontal (0), next must be vertical (1)
        # If last move was vertical (1), next must be horizontal (0)
        # If no last move (None), we can try both
        
        # Try Vertical moves (Up/Down)
        if last_dir is None or last_dir == 0:
            for dr in [-1, 1]:
                nr, nc = r + dr, c
                if 0 <= nr < rows and 0 <= nc < cols:
                    new_cost = current_cost + grid[nr][nc]
                    if (nr, nc, 1) not in dist or dist[(nr, nc, 1)] > new_cost:
                        heapq.heappush(pq, (new_cost, nr, nc, 1))

        # Try Horizontal moves (Left/Right)
        if last_dir is None or last_dir == 1:
            for dc in [-1, 1]:
                nr, nc = r, c + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    new_cost = current_cost + grid[nr][nc]
                    if (nr, nc, 0) not in dist or dist[(nr, nc, 0)] > new_cost:
                        heapq.heappush(pq, (new_cost, nr, nc, 0))

    return -1
