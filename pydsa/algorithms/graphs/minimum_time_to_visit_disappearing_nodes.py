METADATA = {
    "id": 3112,
    "name": "Minimum Time to Visit Disappearing Nodes",
    "slug": "minimum-time-to-visit-disappearing-nodes",
    "category": "Graphs",
    "aliases": [],
    "tags": ["dijkstra", "graphs", "shortest-path"],
    "difficulty": "medium",
    "time_complexity": "O(E log V)",
    "space_complexity": "O(V + E)",
    "description": "Find the minimum time to reach a target node in a graph where nodes disappear after a certain time threshold.",
}

import heapq

def solve(n: int, edges: list[list[int]], target: int, disappearing_nodes: list[list[int]]) -> int:
    """
    Finds the minimum time to reach the target node using Dijkstra's algorithm,
    ensuring that the time of arrival at any node is strictly less than its disappearance time.

    Args:
        n: The number of nodes in the graph (nodes are 0-indexed).
        edges: A list of edges where edges[i] = [u, v, weight].
        target: The destination node index.
        disappearing_nodes: A list of [node, time_limit] where the node disappears at time_limit.

    Returns:
        The minimum time to reach the target node, or -1 if the target is unreachable.

    Examples:
        >>> solve(3, [[0, 1, 1], [1, 2, 1]], 2, [[1, 1]])
        -1
        >>> solve(3, [[0, 1, 1], [1, 2, 1]], 2, [[1, 2]])
        2
    """
    # Map node index to its disappearance threshold for O(1) lookup
    # Using a dictionary to handle sparse disappearance constraints
    thresholds: dict[int, int] = {node: limit for node, limit in disappearing_nodes}

    # Build adjacency list: adj[u] = [(v, weight), ...]
    adj: list[list[tuple[int, int]]] = [[] for _ in range(n)]
    for u, v, w in edges:
        adj[u].append((v, w))
        adj[v].append((u, w))

    # min_time[i] stores the minimum time to reach node i
    min_time: list[int] = [float('inf')] * n
    min_time[0] = 0
    
    # Priority Queue for Dijkstra: (current_time, current_node)
    pq: list[tuple[int, int]] = [(0, 0)]

    while pq:
        current_time, u = heapq.heappop(pq)

        # If we found a better path already, skip
        if current_time > min_time[u]:
            continue

        # If we reached the target, since it's Dijkstra, this is the shortest time
        if u == target:
            return int(current_time)

        for v, weight in adj[u]:
            arrival_time = current_time + weight
            
            # Check if the neighbor v is still present at the arrival time
            # The node disappears AT time_limit, so we must arrive at time < time_limit
            if v in thresholds and arrival_time >= thresholds[v]:
                continue

            # Standard Dijkstra relaxation
            if arrival_time < min_time[v]:
                min_time[v] = arrival_time
                heapq.heappush(pq, (arrival_time, v))

    return -1 if min_time[target] == float('inf') else int(min_time[target])
