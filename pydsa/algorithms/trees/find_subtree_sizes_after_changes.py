METADATA = {
    "id": 3331,
    "name": "Find Subtree Sizes After Changes",
    "slug": "find-subtree-sizes-after-changes",
    "category": "Trees",
    "aliases": [],
    "tags": ["trees", "dfs", "depth-first-search"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Calculate the sizes of all subtrees after incrementing the values of specific nodes in a tree.",
}

def solve(n: int, edges: list[list[int]], values: list[int], queries: list[list[int]]) -> list[int]:
    """
    Calculates the size of each subtree after applying node value increments.

    Args:
        n: The number of nodes in the tree.
        edges: A list of undirected edges representing the tree structure.
        values: The initial values of the nodes.
        queries: A list of queries where each query is [index, increment].

    Returns:
        A list of integers representing the subtree sizes after all queries are applied.

    Examples:
        >>> solve(3, [[0, 1], [0, 2]], [1, 2, 3], [[0, 1]])
        [4, 2, 3]
    """
    # Build adjacency list
    adj: list[list[int]] = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    # Apply all queries to the node values first
    # Since we only care about the final state, we can pre-process queries
    current_values = list(values)
    for index, increment in queries:
        current_values[index] += increment

    # To calculate subtree sizes, we need a post-order traversal.
    # We use an iterative approach to avoid recursion depth issues in Python.
    subtree_sizes: list[int] = [0] * n
    parent: list[int] = [-1] * n
    order: list[int] = []
    stack: list[int] = [0]
    visited: list[bool] = [False] * n
    visited[0] = True

    # Step 1: BFS/DFS to establish parent-child relationships and processing order
    # We use a stack to perform a DFS to get a topological order (pre-order)
    stack = [0]
    while stack:
        u = stack.pop()
        order.append(u)
        for v in adj[u]:
            if not visited[v]:
                visited[v] = True
                parent[v] = u
                stack.append(v)

    # Step 2: Process nodes in reverse topological order (post-order)
    # This ensures children are processed before their parents.
    for i in range(n):
        subtree_sizes[i] = current_values[i]

    # Iterate backwards through the pre-order list to simulate post-order
    for i in range(n - 1, 0, -1):
        u = order[i]
        p = parent[u]
        if p != -1:
            # Add the current node's accumulated subtree size to its parent
            subtree_sizes[p] += subtree_sizes[u]

    return subtree_sizes
