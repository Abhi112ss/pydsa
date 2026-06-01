METADATA = {
    "id": 2378,
    "name": "Choose Edges to Maximize Score in a Tree",
    "slug": "choose-edges-to-maximize-score-in-a-tree",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dfs", "dp", "graphs", "tree"],
    "difficulty": "hard",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Maximize the score by choosing edges to remove, where score is the product of the sizes of the three resulting components.",
}

def solve(n: int, edges: list[list[int]]) -> int:
    """
    Calculates the maximum score possible by removing two edges from a tree.
    The score is defined as the product of the sizes of the three resulting components.

    Args:
        n: The number of nodes in the tree.
        edges: A list of edges where edges[i] = [u, v] represents an edge between u and v.

    Returns:
        The maximum score possible.

    Examples:
        >>> solve(5, [[0, 1], [1, 2], [1, 3], [1, 4]])
        4
        >>> solve(6, [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5]])
        8
    """
    # Build adjacency list
    adj: dict[int, list[int]] = {i: [] for i in range(n)}
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    subtree_size: list[int] = [0] * n
    # We need to store the order of traversal to avoid recursion depth issues 
    # and to process nodes in post-order for subtree calculations.
    order: list[int] = []
    parent: list[int] = [-1] * n
    stack: list[int] = [0]
    visited: list[bool] = [False] * n
    visited[0] = True

    # Iterative DFS to get topological order and parents
    dfs_stack = [0]
    while dfs_stack:
        curr = dfs_stack.pop()
        order.append(curr)
        for neighbor in adj[curr]:
            if not visited[neighbor]:
                visited[neighbor] = True
                parent[neighbor] = curr
                dfs_stack.append(neighbor)

    # Calculate subtree sizes using post-order traversal
    for node in reversed(order):
        subtree_size[node] += 1
        if parent[node] != -1:
            subtree_size[parent[node]] += subtree_size[node]

    max_score = 0

    # To find the max score, we iterate through all possible pairs of edges.
    # An edge can be represented by the child node it connects to (except root).
    # Let edge1 be represented by node 'u' and edge2 by node 'v'.
    # There are two cases:
    # 1. One node is an ancestor of the other (e.g., v is in u's subtree).
    #    Sizes: size(v), size(u) - size(v), n - size(u)
    # 2. Neither is an ancestor of the other.
    #    Sizes: size(u), size(v), n - size(u) - size(v)

    # To handle case 1 efficiently, we need to know if 'v' is in 'u's subtree.
    # We can use entry and exit times from DFS.
    entry_time: list[int] = [0] * n
    exit_time: list[int] = [0] * n
    timer = 0
    
    # Re-run a simple DFS to get entry/exit times for ancestor checks
    # Using a manual stack to avoid recursion limits
    timer = 0
    entry_time = [0] * n
    exit_time = [0] * n
    visited = [False] * n
    stack = [(0, False)] # (node, is_processed)
    
    while stack:
        curr, processed = stack.pop()
        if not processed:
            timer += 1
            entry_time[curr] = timer
            visited[curr] = True
            stack.append((curr, True))
            for neighbor in adj[curr]:
                if not visited[neighbor]:
                    stack.append((neighbor, False))
        else:
            exit_time[curr] = timer

    def is_ancestor(u: int, v: int) -> bool:
        """Checks if u is an ancestor of v."""
        return entry_time[u] <= entry_time[v] and exit_time[u] >= exit_time[v]

    # The nodes representing edges (excluding root 0)
    edge_nodes = [i for i in range(1, n)]
    
    # O(N^2) is acceptable given N <= 1000
    for i in range(len(edge_nodes)):
        u = edge_nodes[i]
        size_u = subtree_size[u]
        for j in range(i + 1, len(edge_nodes)):
            v = edge_nodes[j]
            size_v = subtree_size[v]
            
            if is_ancestor(u, v):
                # v is in u's subtree
                # Components: size(v), size(u)-size(v), n-size(u)
                score = size_v * (size_u - size_v) * (n - size_u)
            elif is_ancestor(v, u):
                # u is in v's subtree
                # Components: size(u), size(v)-size(u), n-size(v)
                score = size_u * (size_v - size_u) * (n - size_v)
            else:
                # Disjoint subtrees
                # Components: size(u), size(v), n-size(u)-size(v)
                score = size_u * size_v * (n - size_u - size_v)
            
            if score > max_score:
                max_score = score
                
    return max_score
