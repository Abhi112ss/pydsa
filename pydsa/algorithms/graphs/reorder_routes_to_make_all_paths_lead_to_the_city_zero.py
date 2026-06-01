METADATA = {
    "id": 1466,
    "name": "Reorder Routes to Make All Paths Lead to the City Zero",
    "slug": "reorder-routes-to-make-all-paths-lead-to-the-city-zero",
    "category": "Graph",
    "aliases": [],
    "tags": ["graph", "dfs", "bfs", "tree"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Reorder the directions of some edges so that all paths lead to city zero.",
}

def solve(n: int, connections: list[list[int]]) -> int:
    """
    Calculates the minimum number of edges that need to be flipped so that 
    all paths lead to city zero.

    The algorithm treats the graph as undirected to ensure connectivity and 
    traverses it starting from city zero. For every edge encountered during 
    traversal that exists in the original direction (from current to neighbor), 
    it must be flipped.

    Args:
        n: The number of cities.
        connections: A list of edges where connections[i] = [from_i, to_i].

    Returns:
        The total number of edges that need to be reversed.

    Examples:
        >>> solve(6, [[0,1],[1,3],[2,3],[4,0],[4,5]])
        3
        >>> solve(3, [[0,1],[1,2]])
        0
    """
    # adjacency_list stores (neighbor, is_original_direction)
    # is_original_direction is True if the edge is [u -> v]
    # is_original_direction is False if the edge is [v -> u] (artificial for traversal)
    adjacency_list: dict[int, list[tuple[int, bool]]] = {i: [] for i in range(n)}
    
    for u, v in connections:
        # Original edge: u -> v. If we move from u to v, we are going "away" from zero.
        adjacency_list[u].append((v, True))
        # Artificial edge: v -> u. If we move from v to u, we are following the "natural" flow.
        adjacency_list[v].append((u, False))

    flip_count = 0
    visited = [False] * n
    # Using a stack for iterative DFS to avoid recursion depth issues
    stack = [0]
    visited[0] = True

    while stack:
        current_node = stack.pop()
        
        for neighbor, is_original in adjacency_list[current_node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                
                # If the edge is original (current -> neighbor), it points AWAY from zero.
                # Since we are traversing outward from zero, any original edge we 
                # traverse must be flipped to point TOWARDS zero.
                if is_original:
                    flip_count += 1
                
                stack.append(neighbor)

    return flip_count
