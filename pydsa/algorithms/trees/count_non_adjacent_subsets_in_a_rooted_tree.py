METADATA = {
    "id": 3939,
    "name": "Count Non Adjacent Subsets in a Rooted Tree",
    "slug": "count-non-adjacent-subsets-in-a-rooted-tree",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["trees", "dp"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Count the number of subsets of nodes in a rooted tree such that no two nodes in the subset are adjacent.",
}

def solve(n: int, edges: list[list[int]]) -> int:
    """
    Counts the number of subsets of nodes in a rooted tree such that no two 
    nodes in the subset are adjacent.

    Args:
        n: The number of nodes in the tree (nodes are labeled 0 to n-1).
        edges: A list of undirected edges representing the tree structure.

    Returns:
        The total number of valid non-adjacent subsets (including the empty set).

    Examples:
        >>> solve(3, [[0, 1], [0, 2]])
        5
        # Subsets: {}, {0}, {1}, {2}, {1, 2}
    """
    if n == 0:
        return 1
    
    # Build adjacency list
    adj: list[list[int]] = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    # dp_included[u]: number of valid subsets in subtree u where u IS included
    # dp_excluded[u]: number of valid subsets in subtree u where u IS NOT included
    dp_included: list[int] = [0] * n
    dp_excluded: list[int] = [0] * n
    
    # To avoid recursion depth issues in Python, use an iterative post-order traversal
    # We use two stacks to simulate post-order (children before parents)
    order: list[int] = []
    stack: list[int] = [0]
    visited: list[bool] = [False] * n
    visited[0] = True
    
    # Standard DFS to get topological order (parent before children)
    dfs_stack = [0]
    parent = [-1] * n
    traversal_order = []
    
    while dfs_stack:
        u = dfs_stack.pop()
        traversal_order.append(u)
        for v in adj[u]:
            if v != parent[u]:
                parent[v] = u
                dfs_stack.append(v)
    
    # Process nodes in reverse topological order (leaves to root)
    for u in reversed(traversal_order):
        # Base case: if u is included, children MUST be excluded
        # If u is excluded, children can be either included or excluded
        inc = 1
        exc = 1
        
        for v in adj[u]:
            if v == parent[u]:
                continue
            
            # If u is included, we can only pick subsets from children where child is excluded
            inc *= dp_excluded[v]
            
            # If u is excluded, for each child we can either include it or exclude it
            # The number of ways for child v is (dp_included[v] + dp_excluded[v])
            exc *= (dp_included[v] + dp_excluded[v])
            
        dp_included[u] = inc
        dp_excluded[u] = exc

    # The answer is the sum of ways where the root is included and where it is excluded
    return dp_included[0] + dp_excluded[0]
