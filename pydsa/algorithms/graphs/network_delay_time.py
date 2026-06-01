METADATA = {
    "id": 743,
    "name": "Network Delay Time",
    "slug": "network-delay-time",
    "category": "Graph",
    "aliases": [],
    "tags": ["dijkstra", "shortest_path", "heap", "bfs"],
    "difficulty": "medium",
    "time_complexity": "O(E log V)",
    "space_complexity": "O(V + E)",
    "description": "Find the minimum time it takes for all nodes in a network to receive a signal from a source node.",
}

import heapq
from collections import defaultdict

def solve(times: list[list[int]], n: int, k: int) -> int:
    """
    Calculates the minimum time required for all nodes to receive a signal 
    starting from node k using Dijkstra's algorithm.

    Args:
        times: A list of directed edges where times[i] = [u, v, w] 
               representing an edge from u to v with weight w.
        n: The total number of nodes in the network (labeled 1 to n).
        k: The starting node index.

    Returns:
        The minimum time for all nodes to receive the signal, or -1 if 
        not all nodes can be reached.

    Examples:
        >>> solve([[2,1,1],[2,3,1],[3,4,1]], 4, 2)
        2
        >>> solve([[1,2,1]], 2, 2)
        -1
    """
    # Build adjacency list: graph[u] = [(v, weight), ...]
    graph = defaultdict(list)
    for u, v, w in times:
        graph[u].append((v, w))

    # min_times stores the shortest distance from k to each node
    # Initialize with infinity
    min_times = {node: float('inf') for node in range(1, n + 1)}
    min_times[k] = 0

    # Priority queue stores (current_distance, current_node)
    # We use a min-heap to always expand the node with the smallest distance
    priority_queue = [(0, k)]

    while priority_queue:
        current_distance, u = heapq.heappop(priority_queue)

        # If we found a longer path than already recorded, skip it
        if current_distance > min_times[u]:
            continue

        # Explore neighbors
        for v, weight in graph[u]:
            distance = current_distance + weight
            
            # If a shorter path to v is found, update and push to heap
            if distance < min_times[v]:
                min_times[v] = distance
                heapq.heappush(priority_queue, (distance, v))

    # The time taken for all nodes to receive the signal is the maximum 
    # of the shortest paths to all nodes.
    max_delay = max(min_times.values())

    # If max_delay is still infinity, it means some nodes are unreachable
    return int(max_delay) if max_delay != float('inf') else -1
