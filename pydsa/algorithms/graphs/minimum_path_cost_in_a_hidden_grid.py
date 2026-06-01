METADATA = {
    "id": 1810,
    "name": "Minimum Path Cost in a Hidden Grid",
    "slug": "minimum-path-cost-in-a-hidden-grid",
    "category": "Graph",
    "aliases": [],
    "tags": ["dfs", "bfs", "dijkstra", "graph", "grid"],
    "difficulty": "hard",
    "time_complexity": "O(N)",
    "space_complexity": "O(N)",
    "description": "Find the minimum cost to reach a target cell in a hidden grid using DFS to map the grid and Dijkstra's algorithm to find the shortest path.",
}

import heapq

def solve(grid_reader: any) -> int:
    """
    Finds the minimum path cost to reach the target cell in a hidden grid.

    Args:
        grid_reader: An object with methods `read(row, col)` which returns 
                     0 (empty), 1 (target), 2 (obstacle), or -1 (out of bounds/wall).
                     It also has `move(direction)` to move the reader.

    Returns:
        int: The minimum cost to reach the target, or -1 if unreachable.

    Examples:
        # Assuming a grid where target is reachable
        solve(mock_reader) -> 5
    """

    # Directions mapping: 0: up, 1: right, 2: down, 3: left
    # We need to map these to the move() method requirements
    # The problem usually defines directions as: 0: up, 1: right, 2: down, 3: left
    # Let's assume the standard: 0: (-1, 0), 1: (0, 1), 2: (1, 0), 3: (0, -1)
    DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    
    # grid_map stores the value of the cell at (r, c)
    # target_pos stores the (r, c) of the target cell
    grid_map: dict[tuple[int, int], int] = {}
    target_pos: tuple[int, int] | None = None
    
    # Current position of the reader
    current_pos = (0, 0)

    def dfs(r: int, c: int) -> None:
        nonlocal target_pos
        
        # Mark current cell as visited by adding to map
        # We use the value read from the grid
        val = grid_reader.read(r, c)
        if val == -1:
            return
        
        grid_map[(r, c)] = val
        if val == 1:
            target_pos = (r, c)

        # Try moving in all 4 directions
        for i, (dr, dc) in enumerate(DIRECTIONS):
            nr, nc = r + dr, c + dc
            if (nr, nc) not in grid_map:
                # Attempt to move the physical reader
                if grid_reader.move(i):
                    dfs(nr, nc)
                    # Backtrack: move back to the original cell
                    # To move back, we move in the opposite direction (i + 2) % 4
                    grid_reader.move((i + 2) % 4)
                else:
                    # If move fails, we still mark it as visited in our map 
                    # to avoid re-trying impossible paths, but with a wall value
                    grid_map[(nr, nc)] = -1

    # Step 1: Map the reachable grid using DFS
    dfs(0, 0)

    if target_pos is None:
        return -1

    # Step 2: Dijkstra's algorithm to find the shortest path on the mapped grid
    # pq stores (cost, r, c)
    pq: list[tuple[int, int, int]] = [(0, 0, 0)]
    visited_costs: dict[tuple[int, int], int] = {(0, 0): 0}

    while pq:
        cost, r, c = heapq.heappop(pq)

        if (r, c) == target_pos:
            return cost

        if cost > visited_costs.get((r, c), float('inf')):
            continue

        for dr, dc in DIRECTIONS:
            nr, nc = r + dr, c + dc
            # Check if the neighbor is within our mapped grid and not a wall
            if (nr, nc) in grid_map and grid_map[(nr, nc)] != -1:
                new_cost = cost + 1
                if new_cost < visited_costs.get((nr, nc), float('inf')):
                    visited_costs[(nr, nc)] = new_cost
                    heapq.heappush(pq, (new_cost, nr, nc))

    return -1

# Note: The grid_reader implementation is provided by the LeetCode environment.
# The solve function above is designed to interface with that environment.