METADATA = {
    "id": 1548,
    "name": "The Most Similar Path in a Graph",
    "slug": "the_most_similar_path_in_a_graph",
    "category": "Graphs",
    "aliases": [],
    "tags": ["graphs", "bfs", "dfs", "dynamic programming"],
    "difficulty": "hard",
    "time_complexity": "O(V + E)",
    "space_complexity": "O(V)",
    "description": "Find the path in a graph that has the maximum similarity to a given target path by maximizing the sum of edge weights corresponding to the target sequence.",
}

def solve(n: int, edges: list[list[int]], target_path: list[int]) -> int:
    """
    Finds the maximum similarity score of a path in a graph compared to a target path.
    
    The similarity score is defined as the sum of weights of edges that match 
    the sequence of nodes in the target path. Since the problem asks for the 
    'most similar path', and the target path is a sequence of nodes, we are 
    essentially looking for the maximum weight sum of a subsequence of edges 
    that matches the target path's structure.

    Args:
        n: The number of nodes in the graph.
        edges: A list of edges where each edge is [u, v, weight].
        target_path: A list of node indices representing the target sequence.

    Returns:
        The maximum similarity score possible.

    Examples:
        >>> solve(3, [[0, 1, 5], [1, 2, 10]], [0, 1, 2])
        15
        >>> solve(3, [[0, 1, 5], [1, 2, 10]], [0, 2])
        0
    """
    # Build adjacency list for efficient traversal
    # adj[u] = [(v, weight), ...]
    adj: dict[int, list[tuple[int, int]]] = {}
    for u, v, weight in edges:
        if u not in adj:
            adj[u] = []
        adj[u].append((v, weight))
        # Assuming undirected graph based on standard similarity problems, 
        # but if directed, remove the following two lines.
        if v not in adj:
            adj[v] = []
        adj[v].append((u, weight))

    # dp[i] will store the maximum similarity score ending at node i
    # where the path matches the prefix of target_path up to some index.
    # However, the problem is essentially finding the max weight sum 
    # of a path that follows the target_path sequence.
    
    # Let's redefine: we want to find the max similarity score.
    # The similarity is the sum of weights of edges (target_path[i], target_path[i+1])
    # that actually exist in the graph.
    
    # Actually, the problem asks for the most similar path. 
    # If the target path is [p0, p1, p2...], we check if (p0, p1) exists, 
    # then (p1, p2), etc.
    
    total_similarity = 0
    
    # We iterate through the target path and check if the edge exists in the graph.
    # To do this efficiently, we use a set of tuples for edge lookups.
    edge_lookup: set[tuple[int, int]] = set()
    weight_lookup: dict[tuple[int, int], int] = {}
    
    for u, v, w in edges:
        # Store both directions for undirected graph
        edge_lookup.add((u, v))
        edge_lookup.add((v, u))
        # If multiple edges exist, we take the max weight for similarity
        weight_lookup[(u, v)] = max(weight_lookup.get((u, v), 0), w)
        weight_lookup[(v, u)] = max(weight_lookup.get((v, u), 0), w)

    # Traverse the target path and accumulate weights of existing edges
    for i in range(len(target_path) - 1):
        u = target_path[i]
        v = target_path[i + 1]
        
        # If the edge exists in the graph, add its weight to similarity
        if (u, v) in edge_lookup:
            total_similarity += weight_lookup[(u, v)]
            
    return total_similarity
