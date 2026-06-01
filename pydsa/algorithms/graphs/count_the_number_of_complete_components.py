METADATA = {
    "id": 2685,
    "name": "Count the Number of Complete Components",
    "slug": "count-the-number-of-complete-components",
    "category": "Graph",
    "aliases": [],
    "tags": ["dfs", "bfs", "graphs"],
    "difficulty": "medium",
    "time_complexity": "O(V + E)",
    "space_complexity": "O(V)",
    "description": "Count the number of connected components in an undirected graph that are complete graphs.",
}

def solve(n: int, edges: list[list[int]]) -> int:
    """
    Counts the number of connected components that are complete graphs.
    A complete graph with k vertices must have exactly k * (k - 1) / 2 edges.

    Args:
        n: The number of vertices in the graph.
        edges: A list of undirected edges where edges[i] = [u, v].

    Returns:
        The number of complete components.

    Examples:
        >>> solve(6, [[0,1],[0,2],[1,2],[3,4],[4,5],[3,5]])
        2
        >>> solve(6, [[0,1],[0,2],[1,2],[3,4]])
        1
    """
    # Build adjacency list
    adj: list[list[int]] = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    visited: list[bool] = [False] * n
    complete_components_count = 0

    for i in range(n):
        if not visited[i]:
            # Start a BFS/DFS to find all nodes and edges in the current component
            component_nodes = 0
            component_edges = 0
            
            stack = [i]
            visited[i] = True
            
            while stack:
                u = stack.pop()
                component_nodes += 1
                # Count the degree of the current node
                component_edges += len(adj[u])
                
                for neighbor in adj[u]:
                    if not visited[neighbor]:
                        visited[neighbor] = True
                        stack.append(neighbor)
            
            # In an undirected graph, the sum of degrees is 2 * number of edges.
            # For a complete graph with k nodes, edges = k * (k - 1) / 2.
            # Therefore, sum of degrees must be k * (k - 1).
            if component_edges == component_nodes * (component_nodes - 1):
                complete_components_count += 1

    return complete_components_count
