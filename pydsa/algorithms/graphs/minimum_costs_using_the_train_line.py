METADATA = {
    "id": 2361,
    "name": "Minimum Costs Using the Train Line",
    "slug": "minimum-costs-using-the-train-line",
    "category": "Graph",
    "aliases": [],
    "tags": ["dijkstra", "graph", "priority_queue"],
    "difficulty": "hard",
    "time_complexity": "O(E log V)",
    "space_complexity": "O(V + E)",
    "description": "Find the minimum cost to travel from station 0 to station n-1 using given train lines with specific costs.",
}

import heapq
from collections import defaultdict

def solve(n: int, connections: list[list[int]]) -> int:
    """
    Finds the minimum cost to travel from station 0 to station n-1 using Dijkstra's algorithm.

    Args:
        n: The number of stations.
        connections: A list of connections where each connection is [u, v, cost].
            Note that connections are directed.

    Returns:
        The minimum cost to reach station n-1 from station 0. 
        Returns -1 if station n-1 is unreachable.

    Examples:
        >>> solve(3, [[0, 1, 10], [1, 2, 20], [0, 2, 50]])
        30
        >>> solve(3, [[0, 1, 10], [0, 2, 50]])
        50
        >>> solve(4, [[0, 1, 1], [1, 2, 1], [2, 3, 1], [0, 3, 10]])
        3
    """
    # Build adjacency list: graph[u] = [(v, cost), ...]
    graph = defaultdict(list)
    for u, v, cost in connections:
        graph[u].append((v, cost))

    # min_costs[i] stores the minimum cost found so far to reach station i
    min_costs = [float('inf')] * n
    min_costs[0] = 0

    # Priority queue stores (current_total_cost, current_station)
    # We use a min-heap to always expand the cheapest known path
    priority_queue = [(0, 0)]

    while priority_queue:
        current_cost, u = heapq.heappop(priority_queue)

        # If we found a path to u that is more expensive than one we've already processed, skip it
        if current_cost > min_costs[u]:
            continue

        # If we reached the destination, we can return early because Dijkstra's 
        # guarantees the first time we pop a node, it's the shortest path.
        if u == n - 1:
            return current_cost

        # Explore neighbors
        for v, weight in graph[u]:
            new_cost = current_cost + weight
            
            # Relaxation step: if a cheaper path to v is found, update and push to heap
            if new_cost < min_costs[v]:
                min_costs[v] = new_cost
                heapq.heappush(priority_queue, (new_cost, v))

    # If the destination station was never reached
    result = min_costs[n - 1]
    return int(result) if result != float('inf') else -1
