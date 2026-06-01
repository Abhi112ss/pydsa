METADATA = {
    "id": 3108,
    "name": "Minimum Cost Walk in Weighted Graph",
    "slug": "minimum-cost-walk-in-weighted-graph",
    "category": "Graphs",
    "aliases": [],
    "tags": ["dijkstra", "graphs", "shortest-path"],
    "difficulty": "medium",
    "time_complexity": "O(E log V)",
    "space_complexity": "O(V + E)",
    "description": "Find the minimum cost to travel from a starting node to a target node in a weighted graph using Dijkstra's algorithm.",
}

import heapq

def solve(n: int, edges: list[list[int]], start: int, target: int) -> int:
    """
    Finds the minimum cost to travel from start to target using Dijkstra's algorithm.

    Args:
        n: The number of nodes in the graph.
        edges: A list of edges where each edge is [u, v, weight].
        start: The starting node index.
        target: The target node index.

    Returns:
        The minimum cost to reach the target from the start. Returns -1 if unreachable.

    Examples:
        >>> solve(3, [[0, 1, 10], [1, 2, 5], [0, 2, 20]], 0, 2)
        15
        >>> solve(3, [[0, 1, 10]], 0, 2)
        -1
    """
    # Build adjacency list for efficient neighbor lookup
    adj: dict[int, list[tuple[int, int]]] = {}
    for u, v, weight in edges:
        if u not in adj:
            adj[u] = []
        if v not in adj:
            adj[v] = []
        adj[u].append((v, weight))
        adj[v].append((u, weight))

    # min_costs stores the minimum distance found so far to each node
    min_costs = [float('inf')] * n
    min_costs[start] = 0
    
    # Priority queue stores (current_cost, current_node)
    priority_queue: list[tuple[int, int]] = [(0, start)]

    while priority_queue:
        current_cost, u = heapq.heappop(priority_queue)

        # If we found a better path to u already, skip this entry
        if current_cost > min_costs[u]:
            continue

        # If we reached the target, we can return early as Dijkstra guarantees shortest path
        if u == target:
            return int(current_cost)

        # Explore neighbors
        if u in adj:
            for v, weight in adj[u]:
                new_cost = current_cost + weight
                # Relaxation step: if a shorter path to v is found
                if new_cost < min_costs[v]:
                    min_costs[v] = new_cost
                    heapq.heappush(priority_queue, (new_cost, v))

    return -1 if min_costs[target] == float('inf') else int(min_costs[target])
