METADATA = {
    "id": 882,
    "name": "Reachable Nodes In Subdivided Graph",
    "slug": "reachable-nodes-in-subdivided-graph",
    "category": "Graph",
    "aliases": [],
    "tags": ["dijkstra", "shortest_path", "heap", "graph"],
    "difficulty": "hard",
    "time_complexity": "O(E log V)",
    "space_complexity": "O(V + E)",
    "description": "Calculate the total number of reachable nodes in a graph where edges are subdivided into multiple sub-nodes.",
}

import heapq

def solve(num_nodes: int, edges: list[list[int]], reachable: list[int]) -> int:
    """
    Calculates the total number of reachable nodes in a subdivided graph.

    Args:
        num_nodes: The number of main nodes.
        edges: A list of edges where each edge is [u, v, intemediate_nodes].
        reachable: A list where reachable[i] is 1 if node i is reachable, 0 otherwise.

    Returns:
        The total number of reachable nodes (main nodes + sub-nodes).

    Examples:
        >>> solve(2, [[0, 1, 10]], [1, 1])
        13
        >>> solve(3, [[0, 1, 10], [1, 2, 10]], [1, 0, 1])
        13
    """
    # Build adjacency list: adj[u] = [(v, intermediate_count), ...]
    adj = [[] for _ in range(num_nodes)]
    for u, v, count in edges:
        adj[u].append((v, count))
        adj[v].append((u, count))

    # distances[i] stores the minimum number of sub-nodes needed to reach main node i
    # from any reachable main node.
    distances = [float('inf')] * num_nodes
    priority_queue = []

    # Initialize Dijkstra with all reachable main nodes
    for i in range(num_nodes):
        if reachable[i] == 1:
            distances[i] = 0
            heapq.heappush(priority_queue, (0, i))

    # Dijkstra's algorithm to find the shortest "sub-node distance" to each main node
    while priority_queue:
        current_dist, u = heapq.heappop(priority_queue)

        if current_dist > distances[u]:
            continue

        for v, count in adj[u]:
            # The distance to v via u is current_dist + count + 1
            # (count sub-nodes + the node v itself, but we only care about sub-nodes)
            # Actually, the distance to reach v's "territory" is current_dist + count + 1
            new_dist = current_dist + count + 1
            if new_dist < distances[v]:
                distances[v] = new_dist
                heapq.heappush(priority_queue, (new_dist, v))

    # Start counting with the reachable main nodes
    total_reachable = sum(reachable)

    # For each edge, calculate how many sub-nodes are reachable from both ends
    for u, v, count in edges:
        # The number of sub-nodes reachable from u is max(0, count - distances[u])
        # However, distances[u] is the distance to reach node u.
        # The sub-nodes on the edge are indexed 1 to count.
        # A sub-node at position 'k' is reachable if:
        # dist_to_u + k <= count AND dist_to_v + (count - k + 1) <= count is not quite right.
        
        # Correct logic:
        # Sub-nodes reachable from u: count - distances[u] (if we consider distance to u)
        # But distances[u] is the number of sub-nodes to reach u.
        # Let's refine: distances[u] is the min sub-nodes to reach u.
        # The sub-nodes on edge (u, v) are reachable if they are within 'count' steps.
        # Sub-nodes reachable from u side: max(0, count - distances[u])
        # Sub-nodes reachable from v side: max(0, count - distances[v])
        # But we must not double count. The total reachable sub-nodes on this edge is:
        # min(count, max(0, count - distances[u]) + max(0, count - distances[v]))
        # Wait, the standard way:
        # Reachable from u: count - distances[u]
        # Reachable from v: count - distances[v]
        # Total on edge: min(count, (count - distances[u]) + (count - distances[v])) 
        # is wrong. It's actually:
        # The number of sub-nodes reachable from u is max(0, count - distances[u])
        # The number of sub-nodes reachable from v is max(0, count - distances[v])
        # The total sub-nodes reachable on this edge is the sum of these, 
        # capped at the total number of sub-nodes 'count'.
        
        reachable_from_u = max(0, count - distances[u])
        reachable_from_v = max(0, count - distances[v])
        
        # If the sum of reachable sub-nodes from both sides covers the whole edge, 
        # we cap it at 'count'.
        total_reachable += min(count, reachable_from_u + reachable_from_v)

    return total_reachable
