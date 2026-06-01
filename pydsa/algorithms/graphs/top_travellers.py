METADATA = {
    "id": 1407,
    "name": "Top Travellers",
    "slug": "top_travellers",
    "category": "Graphs",
    "aliases": [],
    "tags": ["graphs", "dfs", "cycle detection"],
    "difficulty": "medium",
    "time_complexity": "O(N)",
    "space_complexity": "O(N)",
    "description": "Determine if a traveler can reach a destination in a directed graph without getting stuck in a cycle.",
}

def solve(n: int, edges: list[list[int]]) -> bool:
    """
    Determines if there is a path from any node to a destination node 
    without encountering a cycle that prevents reaching the destination.
    
    In the context of this problem (often interpreted as finding if a 
    valid path exists in a functional graph or detecting if a cycle 
    is reachable), we check if all paths eventually lead to a terminal 
    node or if we can reach the target.

    Args:
        n: The number of nodes in the graph.
        edges: A list of directed edges where edges[i] = [u, v].

    Returns:
        bool: True if a valid path exists, False otherwise.

    Examples:
        >>> solve(3, [[0, 1], [1, 2]])
        True
        >>> solve(3, [[0, 1], [1, 0]])
        False
    """
    # Build adjacency list
    adj: dict[int, list[int]] = {i: [] for i in range(n)}
    for u, v in edges:
        adj[u].append(v)

    # visited: 0 = unvisited, 1 = visiting (in current stack), 2 = visited (safe)
    visited: list[int] = [0] * n

    def has_cycle(node: int) -> bool:
        """
        DFS to detect cycles using three-color marking.
        """
        if visited[node] == 1:
            # Found a node currently in the recursion stack: Cycle detected
            return True
        if visited[node] == 2:
            # Node already fully processed and confirmed cycle-free
            return False

        # Mark as visiting
        visited[node] = 1
        
        for neighbor in adj[node]:
            if has_cycle(neighbor):
                return True
        
        # Mark as fully visited (safe)
        visited[node] = 2
        return False

    # Check every node to ensure no cycles exist in the graph components
    # Note: The specific problem logic depends on whether we want to find 
    # if ANY cycle exists or if a specific path is cycle-free.
    # Standard interpretation for "Top Travellers" style problems:
    # Can we traverse the graph without getting stuck?
    for i in range(n):
        if visited[i] == 0:
            if has_cycle(i):
                return False
                
    return True
