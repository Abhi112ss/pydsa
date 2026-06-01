METADATA = {
    "id": 3620,
    "name": "Network Recovery Pathways",
    "slug": "network_recovery_pathways",
    "category": "Graph",
    "aliases": [],
    "tags": ["dfs", "graph", "bridges", "connected components"],
    "difficulty": "medium",
    "time_complexity": "O(V + E)",
    "space_complexity": "O(V)",
    "description": "Find the minimum number of edges required to connect all components in a network.",
}

def solve(n: int, edges: list[list[int]]) -> int:
    """
    Calculates the minimum number of edges needed to make the entire network connected.

    The problem reduces to finding the number of connected components in the graph.
    If there are 'C' connected components, we need exactly 'C - 1' edges to connect them.

    Args:
        n: The number of nodes in the network (labeled 0 to n-1).
        edges: A list of undirected edges where edges[i] = [u, v].

    Returns:
        The minimum number of edges required to connect all nodes.

    Examples:
        >>> solve(4, [[0, 1], [1, 2]])
        1
        >>> solve(4, [[0, 1], [2, 3]])
        1
        >>> solve(5, [[0, 1], [0, 2], [3, 4]])
        1
        >>> solve(6, [[0, 1], [2, 3], [4, 5]])
        2
    """
    if n <= 1:
        return 0

    # Build adjacency list
    adj: dict[int, list[int]] = {i: [] for i in range(n)}
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    visited: set[int] = set()
    num_components = 0

    # Iterate through all nodes to find all connected components
    for node in range(n):
        if node not in visited:
            # Found a new component
            num_components += 1
            
            # Perform iterative DFS to mark all nodes in this component
            stack: list[int] = [node]
            visited.add(node)
            
            while stack:
                current = stack.pop()
                for neighbor in adj[current]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        stack.append(neighbor)

    # To connect C components, we need C - 1 edges
    return num_components - 1
