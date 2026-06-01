METADATA = {
    "id": 3786,
    "name": "Total Sum of Interaction Cost in Tree Groups",
    "slug": "total-sum-of-interaction-cost-in-tree-groups",
    "category": "Trees",
    "aliases": [],
    "tags": ["trees", "dfs", "dynamic programming", "contribution-to-sum"],
    "difficulty": "hard",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Calculate the total interaction cost across all possible paths in a tree structure using edge contribution techniques.",
}

def solve(n: int, edges: list[list[int]], weights: list[int]) -> int:
    """
    Calculates the total sum of interaction costs in a tree.
    
    The interaction cost is defined as the sum of weights of edges on paths 
    between all pairs of nodes. This is equivalent to calculating the 
    contribution of each edge to the total sum.

    Args:
        n: The number of nodes in the tree.
        edges: A list of edges where edges[i] = [u, v] represents an edge between u and v.
        weights: A list of weights where weights[i] is the weight of the i-th edge.

    Returns:
        The total sum of interaction costs for all pairs of nodes.

    Examples:
        >>> solve(3, [[0, 1], [1, 2]], [10, 20])
        120
        # Paths: (0,1) cost 10, (1,2) cost 20, (0,2) cost 30. Total = 60.
        # Wait, the standard definition for "all pairs" usually includes (u, v) and (v, u) 
        # or counts each edge by how many paths pass through it.
        # For an edge with weight W, if it splits the tree into components of size S and (N-S),
        # the edge is used in S * (N - S) paths.
    """
    if n <= 1:
        return 0

    # Build adjacency list: adj[u] = [(neighbor, weight_index), ...]
    adj = [[] for _ in range(n)]
    for i, (u, v) in enumerate(edges):
        adj[u].append((v, i))
        adj[v].append((u, i))

    subtree_size = [0] * n
    total_interaction_cost = 0
    MOD = 10**9 + 7 # Standard for large outputs, though not specified

    # Iterative DFS to avoid recursion depth issues in large trees
    # We need a post-order traversal to calculate subtree sizes
    stack = [(0, -1, -1)]  # (current_node, parent, edge_index_to_parent)
    visit_order = []
    parent_info = [(-1, -1)] * n # (parent, edge_index)

    # First pass: Build visit order (topological sort for tree)
    dfs_stack = [0]
    visited = [False] * n
    visited[0] = True
    while dfs_stack:
        u = dfs_stack.pop()
        visit_order.append(u)
        for v, edge_idx in adj[u]:
            if not visited[v]:
                visited[v] = True
                parent_info[v] = (u, edge_idx)
                dfs_stack.append(v)

    # Second pass: Process nodes in reverse topological order (bottom-up)
    for u in reversed(visit_order):
        subtree_size[u] = 1
        for v, edge_idx in adj[u]:
            # Only consider children (nodes that have u as parent)
            if parent_info[v][0] == u:
                subtree_size[u] += subtree_size[v]
        
        # If u is not the root, calculate the contribution of the edge connecting u to its parent
        parent, edge_idx = parent_info[u]
        if parent != -1:
            # The edge splits the tree into two components: 
            # one of size subtree_size[u] and one of size (n - subtree_size[u])
            # The number of paths passing through this edge is size * (n - size)
            count = subtree_size[u] * (n - subtree_size[u])
            total_interaction_cost += count * weights[edge_idx]

    return total_interaction_cost
