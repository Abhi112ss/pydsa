METADATA = {
    "id": 2876,
    "name": "Count Visited Nodes in a Directed Graph",
    "slug": "count-visited-nodes-in-a-directed-graph",
    "category": "Graphs",
    "aliases": [],
    "tags": ["graphs", "dfs", "bfs"],
    "difficulty": "medium",
    "time_complexity": "O(V + E)",
    "space_complexity": "O(V)",
    "description": "Count the number of nodes reachable from a given source node in a directed graph.",
}

from collections import deque

def solve(n: int, edges: list[list[int]], source: int) -> int:
    """
    Counts the number of unique nodes reachable from the source node in a directed graph.

    Args:
        n: The total number of nodes in the graph (nodes are labeled 0 to n-1).
        edges: A list of directed edges where edges[i] = [u, v] represents an edge from u to v.
        source: The starting node for the traversal.

    Returns:
        The total count of nodes visited, including the source node itself.

    Examples:
        >>> solve(3, [[0, 1], [1, 2]], 0)
        3
        >>> solve(3, [[0, 1], [0, 2]], 0)
        3
        >>> solve(3, [[0, 1], [1, 0]], 2)
        1
    """
    # Build adjacency list for efficient neighbor lookup
    adj: dict[int, list[int]] = {i: [] for i in range(n)}
    for u, v in edges:
        adj[u].append(v)

    # Use a set to track visited nodes to avoid cycles and redundant processing
    visited: set[int] = {source}
    # Queue for Breadth-First Search (BFS)
    queue: deque[int] = deque([source])

    while queue:
        current_node = queue.popleft()

        # Explore all neighbors of the current node
        for neighbor in adj[current_node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    # The number of visited nodes is the size of the visited set
    return len(visited)
