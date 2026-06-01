METADATA = {
    "id": 3604,
    "name": "Minimum Time to Reach Destination in Directed Graph",
    "slug": "minimum-time-to-reach-destination-in-directed-graph",
    "category": "Graph",
    "aliases": [],
    "tags": ["bfs", "dijkstra", "graph"],
    "difficulty": "medium",
    "time_complexity": "O(E log V)",
    "space_complexity": "O(V + E)",
    "description": "Find the minimum time to reach a destination node in a weighted directed graph using Dijkstra's algorithm.",
}

import heapq

def solve(n: int, edges: list[list[int]], start: int, destination: int) -> int:
    """
    Finds the minimum time (shortest path) to reach the destination from the start node.

    Args:
        n: The number of nodes in the graph (nodes are labeled 0 to n-1).
        edges: A list of directed edges where edges[i] = [u, v, weight].
        start: The starting node index.
        destination: The target node index.

    Returns:
        The minimum time to reach the destination, or -1 if the destination is unreachable.

    Examples:
        >>> solve(4, [[0, 1, 1], [1, 2, 2], [0, 2, 4], [2, 3, 1]], 0, 3)
        4
        >>> solve(3, [[0, 1, 5], [1, 2, 5]], 0, 2)
        10
        >>> solve(3, [[0, 1, 5]], 0, 2)
        -1
    """
    # Build adjacency list: adj[u] = [(v, weight), ...]
    adj: dict[int, list[tuple[int, int]]] = {i: [] for i in range(n)}
    for u, v, weight in edges:
        adj[u].append((v, weight))

    # min_times[i] stores the minimum time found so far to reach node i
    min_times: list[float] = [float('inf')] * n
    min_times[start] = 0

    # Priority queue stores (current_time, current_node)
    # Using a heap ensures we always expand the node with the smallest accumulated time
    priority_queue: list[tuple[int, int]] = [(0, start)]

    while priority_queue:
        current_time, u = heapq.heappop(priority_queue)

        # If we found a shorter path to u already, skip this entry
        if current_time > min_times[u]:
            continue

        # If we reached the destination, we can return immediately due to Dijkstra's property
        if u == destination:
            return int(current_time)

        # Explore neighbors
        for v, weight in adj[u]:
            new_time = current_time + weight
            
            # Relaxation step: if a shorter path to v is found, update and push to heap
            if new_time < min_times[v]:
                min_times[v] = new_time
                heapq.heappush(priority_queue, (new_time, v))

    # If destination was never reached
    result = min_times[destination]
    return int(result) if result != float('inf') else -1
