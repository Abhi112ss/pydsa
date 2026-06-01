METADATA = {
    "id": 3651,
    "name": "Minimum Cost Path with Teleportations",
    "slug": "minimum-cost-path-with-teleportations",
    "category": "Graphs",
    "aliases": [],
    "tags": ["dijkstra", "graphs", "shortest-path"],
    "difficulty": "medium",
    "time_complexity": "O(E log V)",
    "space_complexity": "O(V + E)",
    "description": "Find the minimum cost to travel from a source to a destination in a grid with weighted edges and special teleportation links.",
}

import heapq

def solve(grid: list[list[int]], teleports: list[list[int]]) -> int:
    """
    Finds the minimum cost to travel from (0, 0) to (rows-1, cols-1) using Dijkstra's algorithm.

    Args:
        grid: A 2D list of integers representing the cost to enter each cell.
        teleports: A list of lists where each sub-list [r1, c1, r2, c2, cost] 
                   represents a teleportation link from (r1, c1) to (r2, c2) with a specific cost.

    Returns:
        The minimum cost to reach the destination, or -1 if unreachable.

    Examples:
        >>> grid = [[1, 1], [1, 1]]
        >>> teleports = [[0, 0, 1, 1, 1]]
        >>> solve(grid, teleports)
        2
    """
    if not grid or not grid[0]:
        return -1

    rows = len(grid)
    cols = len(grid[0])
    target = (rows - 1, cols - 1)

    # Map teleportation links by their starting cell for O(1) lookup during traversal
    teleport_map: dict[tuple[int, int], list[tuple[int, int, int]]] = {}
    for r1, c1, r2, c2, cost in teleports:
        if (r1, c1) not in teleport_map:
            teleport_map[(r1, c1)] = []
        teleport_map[(r1, c1)].append((r2, c2, cost))

    # Min-priority queue for Dijkstra: (cumulative_cost, current_row, current_col)
    # We start at (0, 0) with the initial cost of the starting cell
    pq = [(grid[0][0], 0, 0)]
    
    # Distance table to keep track of the minimum cost to reach each cell
    min_costs = [[float('inf')] * cols for _ in range(rows)]
    min_costs[0][0] = grid[0][0]

    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    while pq:
        current_cost, r, c = heapq.heappop(pq)

        # If we found a better path to this cell already, skip processing
        if current_cost > min_costs[r][c]:
            continue

        # If we reached the destination, return the cost
        if (r, c) == target:
            return current_cost

        # 1. Explore standard adjacent movements (Up, Down, Left, Right)
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols:
                new_cost = current_cost + grid[nr][nc]
                if new_cost < min_costs[nr][nc]:
                    min_costs[nr][nc] = new_cost
                    heapq.heappush(pq, (new_cost, nr, nc))

        # 2. Explore teleportation links starting from the current cell
        if (r, c) in teleport_map:
            for tr, tc, t_cost in teleport_map[(r, c)]:
                # Teleportation cost is the link cost + the cost of the destination cell
                new_cost = current_cost + t_cost + grid[tr][tc]
                if new_cost < min_costs[tr][tc]:
                    min_costs[tr][tc] = new_cost
                    heapq.heappush(pq, (new_cost, tr, tc))

    return -1 if min_costs[rows - 1][cols - 1] == float('inf') else min_costs[rows - 1][cols - 1]