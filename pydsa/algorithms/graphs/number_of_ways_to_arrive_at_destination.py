METADATA = {
    "id": 1976,
    "name": "Number of Ways to Arrive at Destination",
    "slug": "number-of-ways-to-arrive-at-destination",
    "category": "Graph",
    "aliases": [],
    "tags": ["dijkstra", "graphs", "dp", "shortest-path"],
    "difficulty": "medium",
    "time_complexity": "O(E log V)",
    "space_complexity": "O(V + E)",
    "description": "Find the number of ways to reach the destination node using the shortest path in a weighted graph.",
}

import heapq

def solve(n: int, paths: list[list[int]]) -> int:
    """
    Calculates the number of ways to reach the destination node (n-1) 
    using the shortest path from the source node (0).

    Args:
        n: The number of nodes in the graph.
        paths: A list of paths where paths[i] = [from, to, weight].

    Returns:
        The number of ways to reach node n-1 via the shortest path, modulo 10^9 + 7.

    Examples:
        >>> solve(7, [[0,1,2],[0,2,1],[1,2,3],[1,3,1],[2,1,1],[2,3,4],[2,4,6],[3,5,2],[4,5,1],[5,6,1]])
        1
    """
    MOD = 1_000_000_007
    
    # Build adjacency list
    adj = [[] for _ in range(n)]
    for u, v, w in paths:
        adj[u].append((v, w))
        adj[v].append((u, w))

    # min_distances[i] stores the shortest distance from node 0 to node i
    min_distances = [float('inf')] * n
    # num_ways[i] stores the number of ways to reach node i with min_distances[i]
    num_ways = [0] * n

    min_distances[0] = 0
    num_ways[0] = 1

    # Priority queue stores (distance, current_node)
    pq = [(0, 0)]

    while pq:
        current_dist, u = heapq.heappop(pq)

        # If we found a longer path than the current known shortest, skip it
        if current_dist > min_distances[u]:
            continue

        for v, weight in adj[u]:
            new_dist = current_dist + weight

            # Found a strictly shorter path to node v
            if new_dist < min_distances[v]:
                min_distances[v] = new_dist
                # Reset ways to the number of ways we reached u
                num_ways[v] = num_ways[u]
                heapq.heappush(pq, (new_dist, v))
            
            # Found another path to node v with the same minimum distance
            elif new_dist == min_distances[v]:
                # Add the ways to reach u to the ways to reach v
                num_ways[v] = (num_ways[v] + num_ways[u]) % MOD

    return num_ways[n - 1]
