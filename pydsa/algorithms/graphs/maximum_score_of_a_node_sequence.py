METADATA = {
    "id": 2242,
    "name": "Maximum Score of a Node Sequence",
    "slug": "maximum-score-of-a-node-sequence",
    "category": "Graph",
    "aliases": [],
    "tags": ["graph", "dfs", "degree_count", "greedy"],
    "difficulty": "hard",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Find the maximum score of a sequence of four nodes (u, v, w, x) such that u-v, v-w, and w-x are edges and all nodes are distinct.",
}

def solve(n: int, edges: list[list[int]]) -> int:
    """
    Calculates the maximum score of a node sequence (u, v, w, x) where 
    u-v, v-w, and w-x are edges and all nodes are distinct.
    The score is defined as u * v * w * x.

    Args:
        n: The number of nodes in the graph.
        edges: A list of edges where edges[i] = [u_i, v_i].

    Returns:
        The maximum score possible, or -1 if no such sequence exists.

    Examples:
        >>> solve(6, [[1,2],[2,3],[3,4],[4,5],[5,6]])
        120
        >>> solve(4, [[1,2],[2,3],[3,4]])
        24
    """
    # Build adjacency list and track degrees
    adj = [[] for _ in range(n + 1)]
    degree = [0] * (n + 1)
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
        degree[u] += 1
        degree[v] += 1

    # To maximize u*v*w*x, we only care about nodes with high degrees.
    # Specifically, for the middle nodes (v and w), we only need to consider 
    # the top 3 nodes with the highest degrees to ensure we can always 
    # pick distinct neighbors u and x.
    indexed_degrees = []
    for i in range(1, n + 1):
        indexed_degrees.append((degree[i], i))
    
    indexed_degrees.sort(key=lambda x: x[0], reverse=True)
    
    # We take the top 3 nodes to act as potential candidates for v and w.
    # Even if v and w are among the top 3, we need enough neighbors to pick u and x.
    candidates = []
    for i in range(min(n, 3)):
        candidates.append(indexed_degrees[i][1])

    max_score = -1

    # Iterate through all pairs of nodes (v, w) that have an edge between them.
    # We check if v and w are in our top candidates or if they are connected.
    # However, a more robust way is to iterate through all edges and check 
    # if the endpoints could be v and w.
    for u_edge, v_edge in edges:
        # We try both orientations: (v=u_edge, w=v_edge) and (v=v_edge, w=u_edge)
        for v, w in [(u_edge, v_edge), (v_edge, u_edge)]:
            # To maximize score, we need the largest neighbors of v and w 
            # that are not v, w, or each other.
            
            # Get top neighbors for v (excluding w)
            v_neighbors = []
            for neighbor in adj[v]:
                if neighbor != w:
                    v_neighbors.append(neighbor)
            v_neighbors.sort(reverse=True)
            
            # Get top neighbors for w (excluding v)
            w_neighbors = []
            for neighbor in adj[w]:
                if neighbor != v:
                    w_neighbors.append(neighbor)
            w_neighbors.sort(reverse=True)

            # We only need to check the top few neighbors to find the best u and x
            # because we need to ensure u != x, u != v, u != w, etc.
            # Checking top 3 neighbors for each is sufficient.
            for i in range(min(len(v_neighbors), 3)):
                u = v_neighbors[i]
                if u == w: continue
                
                for j in range(min(len(w_neighbors), 3)):
                    x = w_neighbors[j]
                    if x == v or x == u:
                        continue
                    
                    # Calculate score for the valid sequence u-v-w-x
                    current_score = u * v * w * x
                    if current_score > max_score:
                        max_score = current_score

    # The logic above is O(E), but we can optimize by only checking edges 
    # where at least one endpoint is a high-degree node.
    # Let's refine the search: v and w must be "relatively" high degree.
    # Actually, the most efficient way is to iterate through all edges (v, w)
    # and for each, pick the best u from adj[v] and best x from adj[w].
    
    # Re-calculating max_score with a more focused approach:
    max_score = -1
    for v, w in edges:
        # Try both directions for the edge (v, w)
        for node_v, node_w in [(v, w), (w, v)]:
            # Find top 3 neighbors of node_v excluding node_w
            best_u = []
            for neighbor in adj[node_v]:
                if neighbor != node_w:
                    best_u.append(neighbor)
            best_u.sort(reverse=True)
            best_u = best_u[:3]

            # Find top 3 neighbors of node_w excluding node_v
            best_x = []
            for neighbor in adj[node_w]:
                if neighbor != node_v:
                    best_x.append(neighbor)
            best_x.sort(reverse=True)
            best_x = best_x[:3]

            # Check combinations of top neighbors
            for u in best_u:
                for x in best_x:
                    if u != x and u != node_w and x != node_v:
                        score = u * node_v * node_w * x
                        if score > max_score:
                            max_score = score
                            
    return max_score
