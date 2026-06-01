METADATA = {
    "id": 3772,
    "name": "Maximum Subgraph Score in a Tree",
    "slug": "maximum-subgraph-score-in-a-tree",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dfs", "dynamic_programming", "tree"],
    "difficulty": "hard",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Find the maximum score of a subgraph in a tree where the score is defined by the sum of node values minus the sum of edge weights within the subgraph.",
}

def solve(n: int, edges: list[list[int]], values: list[int], weights: list[int]) -> int:
    """
    Calculates the maximum subgraph score in a tree.
    
    The score of a subgraph is defined as (sum of values of nodes in subgraph) - 
    (sum of weights of edges connecting nodes in the subgraph).
    
    Args:
        n: The number of nodes in the tree.
        edges: A list of edges where edges[i] = [u, v].
        values: A list where values[i] is the value of node i.
        weights: A list where weights[i] is the weight of the i-th edge.
        
    Returns:
        The maximum possible score of any connected subgraph.
        
    Examples:
        >>> solve(3, [[0, 1], [1, 2]], [10, 10, 10], [5, 5])
        20
        >>> solve(3, [[0, 1], [1, 2]], [1, 1, 1], [5, 5])
        1
    """
    # Build adjacency list: adj[u] = [(v, weight), ...]
    adj: list[list[tuple[int, int]]] = [[] for _ in range(n)]
    for i in range(len(edges)):
        u, v = edges[i]
        w = weights[i]
        adj[u].append((v, w))
        adj[v].append((u, w))

    # dp[u] stores the maximum score of a connected subgraph rooted at u,
    # including node u itself.
    dp: list[int] = [0] * n
    max_score = float('-inf')

    # To avoid recursion depth issues in Python, we use an iterative post-order traversal.
    # We first perform a BFS/DFS to get a topological ordering (parent-child relationship).
    order: list[int] = []
    parent: list[int] = [-1] * n
    edge_to_parent_weight: list[int] = [0] * n
    stack: list[int] = [0]
    visited: list[bool] = [False] * n
    visited[0] = True

    # Standard iterative DFS to establish parent-child relationships and processing order
    traversal_stack = [0]
    while traversal_stack:
        u = traversal_stack.pop()
        order.append(u)
        for v, w in adj[u]:
            if not visited[v]:
                visited[v] = True
                parent[v] = u
                edge_to_parent_weight[v] = w
                traversal_stack.append(v)

    # Process nodes in reverse topological order (post-order)
    for u in reversed(order):
        # Start with the value of the current node
        current_node_max_score = values[u]
        
        # For each child, decide whether to include the subtree rooted at that child.
        # We only include the child's subtree if (dp[child] - edge_weight) > 0.
        for v, w in adj[u]:
            if v == parent[u]:
                continue
            
            # The contribution of child v to node u's subgraph score
            contribution = dp[v] - w
            if contribution > 0:
                current_node_max_score += contribution
        
        dp[u] = current_node_max_score
        
        # The global maximum could be any dp[u] because any node can be the 'root' 
        # of the optimal subgraph.
        if dp[u] > max_score:
            max_score = dp[u]

    return int(max_score)
