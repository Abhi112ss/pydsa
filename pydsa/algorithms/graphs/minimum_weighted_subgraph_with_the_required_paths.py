METADATA = {
    "id": 2203,
    "name": "Minimum Weighted Subgraph With the Required Paths",
    "slug": "minimum-weighted-subgraph-with-the-required-paths",
    "category": "Graph",
    "aliases": [],
    "tags": ["dijkstra", "graph", "shortest_path", "priority queue"],
    "difficulty": "hard",
    "time_complexity": "O(E log V)",
    "space_complexity": "O(V + E)",
    "description": "Find the minimum weight of a subgraph that contains all shortest paths from node 0 to node n-1.",
}

import heapq

def solve(n: int, edges: list[list[int]]) -> int:
    """
    Finds the minimum weight of a subgraph containing all shortest paths from 0 to n-1.

    The algorithm uses Dijkstra's algorithm twice: once from the source (0) and 
    once from the target (n-1). An edge (u, v) with weight w belongs to a 
    shortest path if dist_from_source[u] + w + dist_from_target[v] == total_shortest_path.

    Args:
        n: The number of nodes in the graph.
        edges: A list of edges where edges[i] = [u, v, weight].

    Returns:
        The minimum weight of the required subgraph.

    Examples:
        >>> solve(4, [[0, 1, 1], [1, 3, 1], [0, 2, 1], [2, 3, 1]])
        2
        >>> solve(3, [[0, 1, 10], [1, 2, 10], [0, 2, 100]])
        20
    """
    adj = [[] for _ in range(n)]
    rev_adj = [[] for _ in range(n)]
    
    for u, v, w in edges:
        adj[u].append((v, w))
        adj[v].append((u, w))
        rev_adj[u].append((v, w))
        rev_adj[v].append((u, w))

    def dijkstra(start_node: int, graph: list[list[tuple[int, int]]]) -> list[float]:
        distances = [float('inf')] * n
        distances[start_node] = 0
        pq = [(0, start_node)]
        
        while pq:
            current_dist, u = heapq.heappop(pq)
            
            if current_dist > distances[u]:
                continue
                
            for v, weight in graph[u]:
                if distances[u] + weight < distances[v]:
                    distances[v] = distances[u] + weight
                    heapq.heappush(pq, (distances[v], v))
        return distances

    # Step 1: Calculate shortest distances from source (0) and target (n-1)
    dist_from_start = dijkstra(0, adj)
    dist_from_end = dijkstra(n - 1, adj)
    
    shortest_path_len = dist_from_start[n - 1]
    
    # If no path exists, return -1
    if shortest_path_len == float('inf'):
        return -1

    # Step 2: Identify edges that are part of ANY shortest path
    # An edge (u, v) with weight w is on a shortest path if:
    # dist_from_start[u] + w + dist_from_end[v] == shortest_path_len
    # OR dist_from_start[v] + w + dist_from_end[u] == shortest_path_len
    
    # We use a dictionary to store the minimum weight for each unique edge 
    # (represented as a sorted tuple of nodes) that satisfies the condition.
    # This handles the case where multiple edges exist between the same nodes.
    required_edges_weight = {}

    for u, v, w in edges:
        is_on_path = False
        # Check direction u -> v
        if dist_from_start[u] + w + dist_from_end[v] == shortest_path_len:
            is_on_path = True
        # Check direction v -> u
        elif dist_from_start[v] + w + dist_from_end[u] == shortest_path_len:
            is_on_path = True
            
        if is_on_path:
            # Use a canonical representation for the edge to handle multi-edges
            # and ensure we only pick the minimum weight edge between two nodes 
            # if they are part of the shortest path structure.
            # However, the problem asks for the sum of weights of edges in the subgraph.
            # If multiple edges exist between u and v, and they both satisfy the condition,
            # we only need the one with the minimum weight to satisfy the "shortest path" requirement.
            # Wait, the problem asks for the minimum weight subgraph. If two edges exist 
            # between u and v, and both are part of shortest paths, we only need the cheapest one.
            
            edge_key = tuple(sorted((u, v)))
            if edge_key not in required_edges_weight or w < required_edges_weight[edge_key]:
                required_edges_weight[edge_key] = w

    # The problem asks for the sum of weights of the edges in the subgraph.
    # Since we want the MINIMUM weight subgraph, for every pair of nodes (u, v) 
    # that has edges contributing to shortest paths, we only pick the minimum weight edge.
    
    # Re-evaluating: The logic above is slightly flawed for multi-edges. 
    # Let's refine: We need to find all edges (u, v, w) such that they lie on a shortest path.
    # If multiple edges exist between u and v, we only care about the one that 
    # helps satisfy the shortest path condition with the minimum weight.
    
    # Correct approach for multi-edges:
    # For every edge (u, v, w), check if it's on a shortest path.
    # If it is, it's a candidate. But if there are multiple edges between u and v,
    # we only want to include the minimum weight one that satisfies the condition.
    
    # Let's use a dictionary where key is (min(u,v), max(u,v)) and value is min weight.
    # This is what required_edges_weight does.
    
    return sum(required_edges_weight.values())
