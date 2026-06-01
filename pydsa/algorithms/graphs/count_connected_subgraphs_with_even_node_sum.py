METADATA = {
    "id": 3910,
    "name": "Count Connected Subgraphs with Even Node Sum",
    "slug": "count_connected_subgraphs_with_even_node_sum",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dp_on_trees", "dfs", "graphs"],
    "difficulty": "hard",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Count the number of connected subgraphs in a tree where the sum of node values is even.",
}

def solve(n: int, edges: list[list[int]], values: list[int]) -> int:
    """
    Counts the number of connected subgraphs in a tree where the sum of node values is even.
    
    The problem is solved using Tree Dynamic Programming. For each node, we calculate
    the number of connected subgraphs rooted at that node that have an even sum
    and an odd sum.

    Args:
        n: The number of nodes in the tree.
        edges: A list of undirected edges [u, v].
        values: A list of node values.

    Returns:
        The total number of connected subgraphs with an even sum.

    Examples:
        >>> solve(3, [[0, 1], [1, 2]], [1, 2, 1])
        2
        # Subgraphs: {1} (sum 2), {0, 1, 2} (sum 4)
    """
    MOD = 10**9 + 7
    
    # Build adjacency list
    adj: list[list[int]] = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    # dp_even[u]: number of connected subgraphs rooted at u with even sum
    # dp_odd[u]: number of connected subgraphs rooted at u with odd sum
    dp_even = [0] * n
    dp_odd = [0] * n
    total_even_subgraphs = 0

    # To avoid recursion depth issues in Python, we use an iterative DFS approach
    # for post-order traversal (bottom-up processing).
    visited = [False] * n
    order = []
    stack = [0]
    parent = [-1] * n
    visited[0] = True
    
    # First pass: Generate topological order (parent before children)
    while stack:
        u = stack.pop()
        order.append(u)
        for v in adj[u]:
            if not visited[v]:
                visited[v] = True
                parent[v] = u
                stack.append(v)

    # Second pass: Process nodes in reverse topological order (bottom-up)
    for u in reversed(order):
        # Base case: The subgraph containing only the node u itself
        if values[u] % 2 == 0:
            curr_even = 1
            curr_odd = 0
        else:
            curr_even = 0
            curr_odd = 1
        
        for v in adj[u]:
            if v == parent[u]:
                continue
            
            # When combining the current subtree at u with a subtree rooted at child v:
            # A new even sum can be formed by:
            # 1. (current even) * (child even + 1) -> the +1 represents NOT picking child v
            # 2. (current odd) * (child odd)
            # However, the standard way to handle "connected subgraphs rooted at u" 
            # is to consider that for each child v, we either include a connected 
            # subgraph rooted at v or we don't.
            
            # If we include child v, we can pick any connected subgraph rooted at v.
            # The number of ways to pick a connected subgraph rooted at v is (dp_even[v] + dp_odd[v]).
            # But we must distinguish between even and odd contributions.
            
            next_even = (curr_even * (1 + dp_even[v]) + curr_odd * dp_odd[v]) % MOD
            next_odd = (curr_odd * (1 + dp_even[v]) + curr_even * dp_odd[v]) % MOD
            
            curr_even, curr_odd = next_even, next_odd
            
        dp_even[u] = curr_even
        dp_odd[u] = curr_odd
        
        # Add all even-sum subgraphs rooted at u to the global count
        total_even_subgraphs = (total_even_subgraphs + curr_even) % MOD

    return total_even_subgraphs
