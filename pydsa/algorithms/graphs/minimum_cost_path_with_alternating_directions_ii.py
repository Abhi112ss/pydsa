METADATA = {
    "id": 3603,
    "name": "Minimum Cost Path with Alternating Directions II",
    "slug": "minimum_cost_path_with_alternating_directions_ii",
    "category": "Graph",
    "aliases": [],
    "tags": ["dijkstra", "graph", "dynamic_programming"],
    "difficulty": "hard",
    "time_complexity": "O(E log V)",
    "space_complexity": "O(V)",
    "description": "Find the minimum cost to reach a target node in a graph where each step must alternate between two specific directions or types of edges.",
}

import heapq

def solve(n: int, edges: list[list[int]], start_node: int, target_node: int, direction_type_a: int, direction_type_b: int) -> int:
    """
    Finds the minimum cost to reach target_node from start_node with alternating edge types.

    Args:
        n: Number of nodes in the graph.
        edges: A list of edges where each edge is [u, v, weight, type].
        start_node: The starting node index.
        target_node: The destination node index.
        direction_type_a: The first edge type allowed in the alternation.
        direction_type_b: The second edge type allowed in the alternation.

    Returns:
        The minimum cost to reach the target node, or -1 if unreachable.

    Examples:
        >>> solve(3, [[0, 1, 5, 1], [1, 2, 10, 2]], 0, 2, 1, 2)
        15
        >>> solve(3, [[0, 1, 5, 1], [1, 2, 10, 1]], 0, 2, 1, 2)
        -1
    """
    # Build adjacency list: adj[u] = [(v, weight, type), ...]
    adj = [[] for _ in range(n)]
    for u, v, weight, edge_type in edges:
        adj[u].append((v, weight, edge_type))
        adj[v].append((u, weight, edge_type))

    # dist[node][state] where state 0 means next edge must be type_a, 
    # state 1 means next edge must be type_b.
    # We use a large value for infinity.
    inf = float('inf')
    dist = [[inf, inf] for _ in range(n)]

    # Priority Queue stores (current_cost, current_node, next_required_type_index)
    # next_required_type_index: 0 for type_a, 1 for type_b
    pq = []

    # Initial state: We can start with either type_a or type_b.
    # However, the problem implies the sequence starts with one of them.
    # If the first edge must be type_a, we start with state 0.
    # If the first edge can be either, we push both possibilities.
    # Standard interpretation for "alternating" is that the first edge can be either.
    
    # To handle "starting with either", we allow the first step to be either A or B.
    # We represent this by saying at start_node, we are looking for 'either'.
    # But to keep the state machine clean, we'll push two entries:
    # 1. We just finished a 'B' type (so next is A)
    # 2. We just finished an 'A' type (so next is B)
    
    # Case 1: First edge is type_a
    dist[start_node][0] = 0
    heapq.heappush(pq, (0, start_node, 0))
    
    # Case 2: First edge is type_b
    dist[start_node][1] = 0
    heapq.heappush(pq, (0, start_node, 1))

    while pq:
        current_cost, u, state = heapq.heappop(pq)

        if current_cost > dist[u][state]:
            continue
        
        if u == target_node:
            return current_cost

        # Determine which edge type we are looking for based on current state
        required_type = direction_type_a if state == 0 else direction_type_b
        next_state = 1 - state # Toggle between 0 and 1

        for v, weight, edge_type in adj[u]:
            if edge_type == required_type:
                new_cost = current_cost + weight
                if new_cost < dist[v][next_state]:
                    dist[v][next_state] = new_cost
                    heapq.heappush(pq, (new_cost, v, next_state))

    # Check both states at target_node
    ans = min(dist[target_node][0], dist[target_node][1])
    return ans if ans != inf else -1
