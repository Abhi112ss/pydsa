METADATA = {
    "id": 3778,
    "name": "Minimum Distance Excluding One Maximum Weighted Edge",
    "slug": "minimum-distance-excluding-one-maximum-weighted-edge",
    "category": "Graph",
    "aliases": [],
    "tags": ["dijkstra", "graphs", "shortest-path"],
    "difficulty": "medium",
    "time_complexity": "O(E log V)",
    "space_complexity": "O(V + E)",
    "description": "Find the shortest path between two nodes after removing exactly one edge that has the maximum weight in the graph.",
}

import heapq

def solve(n: int, edges: list[list[int]], source: int, target: int) -> int:
    """
    Args:
        n: The number of nodes in the graph.
        edges: A list of edges where each edge is [u, v, weight].
        source: The starting node.
        target: The destination node.

    Returns:
        The shortest distance from source to target after removing one edge with the maximum weight. 
        If no path exists, return -1.
    """
    if not edges:
        return -1

    max_weight = -1
    for _, _, weight in edges:
        if weight > max_weight:
            max_weight = weight

    adj = [[] for _ in range(n)]
    for u, v, weight in edges:
        if weight == max_weight:
            continue
        adj[u].append((v, weight))
        adj[v].append((u, weight))

    distances = [float('inf')] * n
    distances[source] = 0
    priority_queue = [(0, source)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_distance > distances[current_node]:
            continue

        if current_node == target:
            break

        for neighbor, weight in adj[current_node]:
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    result = distances[target]
    return int(result) if result != float('inf') else -1