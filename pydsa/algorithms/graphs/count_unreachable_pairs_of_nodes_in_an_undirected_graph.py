METADATA = {
    "id": 2316,
    "name": "Count Unreachable Pairs of Nodes in an Undirected Graph",
    "slug": "count-unreachable-pairs-of-nodes-in-an-undirected-graph",
    "category": "Graph",
    "aliases": [],
    "tags": ["dfs", "bfs", "union_find", "connected components"],
    "difficulty": "medium",
    "time_complexity": "O(n + e)",
    "space_complexity": "O(n)",
    "description": "Count the number of pairs of nodes that are not connected in an undirected graph.",
}

def solve(n: int, edges: list[list[int]]) -> int:
    """
    Calculates the number of pairs of nodes (i, j) such that i < j and there is no path between them.

    The algorithm finds the sizes of all connected components in the graph. 
    If the sizes of components are s1, s2, ..., sk, the number of unreachable pairs 
    is the sum of products of all distinct pairs of sizes. 
    Alternatively, it can be calculated as:
    Total pairs - Sum of (si * (si - 1) / 2) for all components.

    Args:
        n: The number of nodes in the graph.
        edges: A list of undirected edges where edges[i] = [u, v].

    Returns:
        The total number of unreachable pairs.

    Examples:
        >>> solve(4, [[1, 0], [2, 3]])
        1
        >>> solve(5, [[0, 1], [1, 2], [3, 4]])
        4
    """
    # Build adjacency list
    adj: list[list[int]] = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    visited: list[bool] = [False] * n
    component_sizes: list[int] = []

    # Traverse all nodes to find all connected components
    for i in range(n):
        if not visited[i]:
            # Start a BFS to find the size of the current component
            component_size = 0
            queue: list[int] = [i]
            visited[i] = True
            
            # Standard BFS implementation
            idx = 0
            while idx < len(queue):
                curr = queue[idx]
                idx += 1
                component_size += 1
                
                for neighbor in adj[curr]:
                    if not visited[neighbor]:
                        visited[neighbor] = True
                        queue.append(neighbor)
            
            component_sizes.append(component_size)

    # Calculate unreachable pairs:
    # Total pairs = n * (n - 1) // 2
    # Reachable pairs = sum of (size * (size - 1) // 2) for each component
    total_pairs = n * (n - 1) // 2
    reachable_pairs = 0
    for size in component_sizes:
        reachable_pairs += (size * (size - 1)) // 2

    return total_pairs - reachable_pairs
