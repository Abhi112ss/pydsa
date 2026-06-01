METADATA = {
    "id": 2852,
    "name": "Sum of Remoteness of All Cells",
    "slug": "sum-of-remoteness-of-all-cells",
    "category": "Tree",
    "aliases": [],
    "tags": ["tree", "dp", "dfs", "rerooting"],
    "difficulty": "hard",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Calculate the sum of the maximum distances from each cell to any other cell in a tree structure.",
}

def solve(n: int, edges: list[list[int]]) -> list[int]:
    """
    Calculates the sum of remoteness for all cells in a tree.
    The remoteness of a cell is the maximum distance from that cell to any other cell.

    Args:
        n: The number of nodes in the tree.
        edges: A list of undirected edges representing the tree.

    Returns:
        A list of integers where the i-th element is the remoteness of node i.

    Examples:
        >>> solve(2, [[0, 1]])
        [1, 1]
        >>> solve(3, [[0, 1], [1, 2]])
        [2, 1, 2]
    """
    if n == 1:
        return [0]

    adj: list[list[int]] = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    # max_dist[u] will store the maximum distance from node u to any node in its subtree
    # second_max_dist[u] will store the second maximum distance from node u to any node in its subtree
    # (where the two distances must come from different child branches)
    max_dist: list[int] = [0] * n
    second_max_dist: list[int] = [0] * n
    
    # To handle rerooting, we need to know which child provided the max_dist
    max_child: list[int] = [-1] * n

    # First DFS: Bottom-up DP to find max distances within subtrees
    # We use an iterative approach to avoid recursion depth issues in Python
    order: list[int] = []
    stack: list[int] = [0]
    parent: list[int] = [-1] * n
    visited: list[bool] = [False] * n
    visited[0] = True
    
    # Standard BFS/DFS to get topological order for tree processing
    processing_stack = [0]
    while processing_stack:
        u = processing_stack.pop()
        order.append(u)
        for v in adj[u]:
            if v != parent[u]:
                parent[v] = u
                visited[v] = True
                processing_stack.append(v)

    # Process nodes in reverse topological order (bottom-up)
    for u in reversed(order):
        for v in adj[u]:
            if v == parent[u]:
                continue
            
            dist_via_v = max_dist[v] + 1
            if dist_via_v > max_dist[u]:
                second_max_dist[u] = max_dist[u]
                max_dist[u] = dist_via_v
                max_child[u] = v
            elif dist_via_v > second_max_dist[u]:
                second_max_dist[u] = dist_via_v

    # remoteness[u] will store the final answer for node u
    remoteness: list[int] = [0] * n
    # up_dist[u] stores the maximum distance from u to any node NOT in its subtree
    up_dist: list[int] = [0] * n

    # Second DFS: Top-down DP (Rerooting)
    # Process nodes in topological order (top-down)
    for u in order:
        # The remoteness is the maximum of the longest path down or the longest path up
        remoteness[u] = max(max_dist[u], up_dist[u])
        
        for v in adj[u]:
            if v == parent[u]:
                continue
            
            # Calculate the max distance going 'up' from child v
            # Option 1: Go up to u and then further up from u
            # Option 2: Go up to u and then down a different branch of u
            if max_child[u] == v:
                # v was the branch that gave u its max_dist, so we must use the second best
                up_dist[v] = max(up_dist[u], second_max_dist[u]) + 1
            else:
                # v was not the max branch, so we can use u's max_dist
                up_dist[v] = max(up_dist[u], max_dist[u]) + 1

    return remoteness
