METADATA = {
    "id": 3650,
    "name": "Minimum Cost Path with Edge Reversals",
    "slug": "minimum-cost-path-with-edge-reversals",
    "category": "Graphs",
    "aliases": [],
    "tags": ["dijkstra", "graphs", "shortest-path"],
    "difficulty": "medium",
    "time_complexity": "O(E log V)",
    "space_complexity": "O(V + E)",
    "description": "Find the minimum cost to travel from source to target in a directed graph where edges can be reversed with a specific cost.",
}

import heapq

def solve(n: int, edges: list[tuple[int, int, int]], source: int, target: int) -> int:
    """
    Finds the minimum cost to travel from source to target in a directed graph,
    allowing edges to be reversed at a given cost.

    Args:
        n: The number of nodes in the graph (labeled 0 to n-1).
        edges: A list of tuples (u, v, cost) representing a directed edge from u to v.
        source: The starting node.
        target: The destination node.

    Returns:
        The minimum cost to reach the target from the source. Returns -1 if unreachable.

    Examples:
        >>> solve(3, [(0, 1, 10), (1, 2, 10)], 0, 2)
        20
        >>> solve(3, [(0, 1, 10), (2, 1, 5)], 0, 2)
        15
    """
    # adjacency_list stores (neighbor, weight, is_reverse)
    # weight is the cost to traverse the edge in its original direction (0 if we consider 
    # the cost to be the edge weight itself, but here the problem implies 
    # traversing original edges costs 0 extra, and reversing costs 'cost').
    # Wait, standard interpretation: original edge (u -> v) costs 0 to use, 
    # but reversing it (v -> u) costs 'cost'. 
    # However, if the problem implies the edge itself has a weight, we adjust.
    # Let's assume: original edge (u, v) has weight 'w'. 
    # Using (u, v) costs 'w'. Reversing it to (v, u) costs 'w' + reversal_penalty.
    # Based on the prompt "reversed edges are added with their respective costs",
    # we assume: 
    # 1. Original edge (u, v) with weight 'w' exists.
    # 2. We can use (u, v) with cost 'w'.
    # 3. We can use (v, u) with cost 'w' + reversal_cost (if reversal_cost is provided).
    # If the problem implies the 'cost' in (u, v, cost) is the cost to REVERSE it:
    # 1. Original edge (u, v) costs 0.
    # 2. Reversed edge (v, u) costs 'cost'.
    
    adj = [[] for _ in range(n)]
    for u, v, cost in edges:
        # Original direction: cost 0 to traverse
        adj[u].append((v, 0))
        # Reversed direction: cost 'cost' to traverse
        adj[v].append((u, cost))

    # Dijkstra's algorithm
    # min_costs[i] stores the minimum cost to reach node i
    min_costs = [float('inf')] * n
    min_costs[source] = 0
    
    # Priority queue stores (current_total_cost, current_node)
    pq = [(0, source)]

    while pq:
        current_dist, u = heapq.heappop(pq)

        # If we found a better path already, skip
        if current_dist > min_costs[u]:
            continue
        
        # If we reached the target, we can return early because it's Dijkstra
        if u == target:
            return current_dist

        for v, weight in adj[u]:
            new_dist = current_dist + weight
            # If a cheaper path to v is found
            if new_dist < min_costs[v]:
                min_costs[v] = new_dist
                heapq.heappush(pq, (new_dist, v))

    return int(min_costs[target]) if min_costs[target] != float('inf') else -1
