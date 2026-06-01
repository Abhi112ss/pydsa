METADATA = {
    "id": 261,
    "name": "Graph Valid Tree",
    "slug": "graph_valid_tree",
    "category": "Graph",
    "aliases": [],
    "tags": ["dfs", "bfs", "union_find", "graph"],
    "difficulty": "medium",
    "time_complexity": "O(V + E)",
    "space_complexity": "O(V + E)",
    "description": "Determine if a given set of edges forms a valid tree structure for n nodes.",
}

def solve(n: int, edges: list[list[int]]) -> bool:
    """
    Determines if the given edges form a valid tree.
    
    A graph is a valid tree if and only if:
    1. It has exactly n - 1 edges.
    2. It is fully connected (all nodes are reachable from a single starting node).
    
    Args:
        n: The number of nodes in the graph (labeled 0 to n-1).
        edges: A list of undirected edges where edges[i] = [u, v].
        
    Returns:
        True if the graph is a valid tree, False otherwise.
        
    Examples:
        >>> solve(5, [[0, 1], [0, 2], [0, 3], [1, 4]])
        True
        >>> solve(5, [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]])
        False
    """
    # A tree with n nodes must have exactly n-1 edges.
    # If it has more, there's a cycle. If it has fewer, it's disconnected.
    if len(edges) != n - 1:
        return False
    
    # Handle the edge case of a single node with no edges
    if n == 0:
        return False
    if n == 1:
        return True

    # Build adjacency list for BFS/DFS traversal
    adj_list: dict[int, list[int]] = {i: [] for i in range(n)}
    for u, v in edges:
        adj_list[u].append(v)
        adj_list[v].append(u)

    # Use BFS to check connectivity
    visited: set[int] = set()
    queue: list[int] = [0]
    visited.add(0)
    
    head = 0
    while head < len(queue):
        current_node = queue[head]
        head += 1
        
        for neighbor in adj_list[current_node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    
    # If the number of visited nodes equals n, the graph is connected.
    # Since we already verified len(edges) == n - 1, connectivity implies no cycles.
    return len(visited) == n
