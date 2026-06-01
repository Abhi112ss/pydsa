METADATA = {
    "id": 2581,
    "name": "Count Number of Possible Root Nodes",
    "slug": "count-number-of-possible-root-nodes",
    "category": "Tree",
    "aliases": [],
    "tags": ["tree", "dfs", "subtree_size"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Count how many nodes can serve as the root of a tree such that the number of special nodes in each subtree is at most half the total number of special nodes.",
}

def solve(n: int, edges: list[list[int]], special_nodes: list[int]) -> int:
    """
    Calculates the number of nodes that can be the root of the tree such that 
    every subtree contains at most half of the total special nodes.

    Args:
        n: The number of nodes in the tree.
        edges: A list of undirected edges where edges[i] = [u, v].
        special_nodes: A list of nodes that are marked as special.

    Returns:
        The count of valid root nodes.

    Examples:
        >>> solve(7, [[0,1],[0,2],[2,3],[2,4],[2,5],[2,6]], [1,3,4,5,6])
        1
    """
    # Build adjacency list
    adj: dict[int, list[int]] = {i: [] for i in range(n)}
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    # Mark special nodes for O(1) lookup
    is_special = [False] * n
    for node in special_nodes:
        is_special[node] = True
    
    total_special = len(special_nodes)
    # subtree_special_count[i] stores number of special nodes in subtree rooted at i
    subtree_special_count = [0] * n
    
    # To avoid recursion depth issues in large trees, we use an iterative DFS
    # to compute subtree sizes (post-order traversal).
    order = []
    stack = [0]
    parent = [-1] * n
    visited = [False] * n
    visited[0] = True
    
    # First pass: BFS/DFS to get topological order (parent-child relationships)
    processing_stack = [0]
    while processing_stack:
        curr = processing_stack.pop()
        order.append(curr)
        for neighbor in adj[curr]:
            if not visited[neighbor]:
                visited[neighbor] = True
                parent[neighbor] = curr
                processing_stack.append(neighbor)
                
    # Second pass: Process nodes in reverse topological order (bottom-up)
    for node in reversed(order):
        if is_special[node]:
            subtree_special_count[node] += 1
        if parent[node] != -1:
            subtree_special_count[parent[node]] += subtree_special_count[node]

    # A node is a valid root if for every neighbor 'v', the component containing 'v'
    # has <= total_special / 2 special nodes.
    # If we root at 'u', the components are:
    # 1. Subtrees of children of 'u' (already calculated in subtree_special_count)
    # 2. The "upward" component (total_special - subtree_special_count[u])
    
    valid_roots_count = 0
    for u in range(n):
        is_valid = True
        
        # Check all children components
        for v in adj[u]:
            if v == parent[u]:
                # This is the "upward" component
                upward_special = total_special - subtree_special_count[u]
                if upward_special > total_special // 2:
                    is_valid = False
                    break
            else:
                # This is a downward subtree component
                if subtree_special_count[v] > total_special // 2:
                    is_valid = False
                    break
        
        if is_valid:
            valid_roots_count += 1
            
    return valid_roots_count
