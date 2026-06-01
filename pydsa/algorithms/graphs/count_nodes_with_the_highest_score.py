METADATA = {
    "id": 2049,
    "name": "Count Nodes With the Highest Score",
    "slug": "count-nodes-with-the-highest-score",
    "category": "Trees",
    "aliases": [],
    "tags": ["trees", "dfs", "graph"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Find the number of nodes that, when removed, result in the maximum product of the sizes of the resulting connected components.",
}

def solve(n: int, edges: list[list[int]]) -> int:
    """
    Calculates the number of nodes that yield the maximum score when removed.
    The score is the product of the sizes of the resulting connected components.

    Args:
        n: The number of nodes in the tree.
        edges: A list of undirected edges representing the tree structure.

    Returns:
        The count of nodes that achieve the maximum score.

    Examples:
        >>> solve(3, [[0, 1], [1, 2]])
        1
        >>> solve(5, [[0, 1], [0, 2], [2, 3], [2, 4]])
        1
    """
    if n == 1:
        return 1

    # Build adjacency list
    adj: dict[int, list[int]] = {i: [] for i in range(n)}
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    subtree_size: list[int] = [0] * n
    max_score: int = 0
    count_max_score: int = 0

    # Iterative DFS to avoid recursion depth issues in large trees
    # We need two passes: one to compute subtree sizes (post-order)
    # and one to calculate scores.
    
    # First, determine the post-order traversal using a stack
    post_order: list[int] = []
    stack: list[int] = [0]
    visited: list[bool] = [False] * n
    parent: list[int] = [-1] * n
    
    # Standard DFS to establish parent-child relationships and post-order
    visit_stack = [0]
    visited[0] = True
    while visit_stack:
        curr = visit_stack.pop()
        post_order.append(curr)
        for neighbor in adj[curr]:
            if not visited[neighbor]:
                visited[neighbor] = True
                parent[neighbor] = curr
                visit_stack.append(neighbor)

    # Process nodes in reverse post-order (bottom-up) to compute subtree sizes
    for node in reversed(post_order):
        subtree_size[node] = 1
        for neighbor in adj[node]:
            if neighbor != parent[node]:
                subtree_size[node] += subtree_size[neighbor]

    # Second pass: Calculate score for each node
    for node in range(n):
        product: int = 1
        sum_of_children_subtrees: int = 0
        
        # Components formed by children
        for neighbor in adj[node]:
            if neighbor != parent[node]:
                size = subtree_size[neighbor]
                product *= size
                sum_of_children_subtrees += size
            else:
                # Component formed by the "upper" part of the tree
                # Size is total nodes minus the current node's subtree
                size = n - subtree_size[node]
                if size > 0:
                    product *= size
        
        # If node is a leaf, the product logic above handles it, 
        # but we must ensure we don't multiply by 0 if the component is empty.
        # However, the problem implies components must exist.
        # If node is leaf, product is (n-1).
        if not adj[node]: # Should not happen in a tree with n > 1
            product = 0 
        elif len(adj[node]) == 1 and node != 0: # Leaf node
            product = n - 1

        if product > max_score:
            max_score = product
            count_max_score = 1
        elif product == max_score:
            count_max_score += 1

    return count_max_score
