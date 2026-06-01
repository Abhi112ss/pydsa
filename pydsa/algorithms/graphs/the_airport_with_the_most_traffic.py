METADATA = {
    "id": 2112,
    "name": "The Airport With the Most Traffic",
    "slug": "the-airport-with-the-most-traffic",
    "category": "Graph",
    "aliases": [],
    "tags": ["graph", "topological_sort", "dfs", "dynamic_programming"],
    "difficulty": "hard",
    "time_complexity": "O(n + e)",
    "space_complexity": "O(n + e)",
    "description": "Find the airport with the maximum number of flights passing through it in a directed acyclic graph of flight paths.",
}

def solve(n: int, flights: list[list[int]]) -> int:
    """
    Finds the airport with the most traffic in a directed acyclic graph.
    Traffic is defined as the number of paths passing through a node.
    In a DAG, for a node 'u', traffic = (paths ending at u) * (paths starting at u).

    Args:
        n: The number of airports.
        flights: A list of directed edges [from, to].

    Returns:
        The index of the airport with the most traffic. If there's a tie, 
        returns the smallest index.

    Examples:
        >>> solve(3, [[0, 1], [1, 2]])
        1
        >>> solve(4, [[0, 1], [0, 2], [1, 3], [2, 3]])
        1
    """
    # Build adjacency list and calculate in-degrees for topological sort
    adj = [[] for _ in range(n)]
    rev_adj = [[] for _ in range(n)]
    in_degree = [0] * n
    out_degree = [0] * n
    
    for u, v in flights:
        adj[u].append(v)
        rev_adj[v].append(u)
        in_degree[v] += 1
        out_degree[u] += 1

    # dp_forward[i] = number of paths starting from any source and ending at i
    dp_forward = [0] * n
    # dp_backward[i] = number of paths starting at i and ending at any sink
    dp_backward = [0] * n

    # Kahn's algorithm for topological sort to compute dp_forward
    queue = []
    for i in range(n):
        if in_degree[i] == 0:
            queue.append(i)
            dp_forward[i] = 1
            
    # We use a pointer instead of pop(0) for O(1) queue operations
    head = 0
    topo_order = []
    while head < len(queue):
        u = queue[head]
        head += 1
        topo_order.append(u)
        for v in adj[u]:
            dp_forward[v] += dp_forward[u]
            in_degree[v] -= 1
            if in_degree[v] == 0:
                queue.append(v)

    # Compute dp_backward using the reverse topological order
    # A node with no outgoing edges is a sink, so it has 1 path starting from it
    for i in range(n):
        if out_degree[i] == 0:
            dp_backward[i] = 1

    # Process nodes in reverse topological order to propagate path counts backwards
    for u in reversed(topo_order):
        for v in adj[u]:
            dp_backward[u] += dp_backward[v]

    # The traffic at node i is (paths ending at i) * (paths starting at i)
    # However, the problem defines traffic as paths passing THROUGH the node.
    # In a DAG, the number of paths containing node i is:
    # (paths ending at i) * (paths starting at i)
    # Note: dp_forward[i] includes the path of length 0 (just node i).
    # dp_backward[i] includes the path of length 0 (just node i).
    # The product correctly counts all paths where i is an intermediate or endpoint.
    
    max_traffic = -1
    best_airport = -1

    for i in range(n):
        # Traffic calculation: paths ending at i * paths starting at i
        current_traffic = dp_forward[i] * dp_backward[i]
        
        if current_traffic > max_traffic:
            max_traffic = current_traffic
            best_airport = i
        elif current_traffic == max_traffic:
            # Tie-breaker: smallest index
            if best_airport == -1 or i < best_airport:
                best_airport = i

    return best_airport
