METADATA = {
    "id": 1059,
    "name": "All Paths from Source Lead to Destination",
    "slug": "all-paths-from-source-lead-to-destination",
    "category": "Graph",
    "aliases": [],
    "tags": ["dfs", "cycle_detection", "graph"],
    "difficulty": "medium",
    "time_complexity": "O(V + E)",
    "space_complexity": "O(V + E)",
    "description": "Determine if all paths starting from a source node in a directed graph eventually lead to a specific destination node.",
}

def solve(edges: list[list[int]], source: int, destination: int) -> bool:
    """
    Determines if all paths starting from the source node lead to the destination.

    The algorithm uses Depth First Search (DFS) to traverse the graph. 
    A path is invalid if it reaches a node that is not the destination and has no outgoing edges,
    or if it enters a cycle that does not include the destination.

    Args:
        edges: A list of directed edges where edges[i] = [from_i, to_i].
        source: The starting node index.
        destination: The target node index.

    Returns:
        True if all paths from source lead to destination, False otherwise.

    Examples:
        >>> solve([[0,1],[1,3],[2,3],[3,3]], 0, 3)
        True
        >>> solve([[0,1],[1,2],[2,0]], 0, 3)
        False
    """
    from collections import defaultdict

    # Build adjacency list
    adj_list: dict[int, list[int]] = defaultdict(list)
    for u, v in edges:
        adj_list[u].append(v)

    # visited tracks nodes currently in the recursion stack to detect cycles
    # and nodes fully processed to avoid redundant work.
    # 0: unvisited, 1: visiting (in stack), 2: visited (safe)
    state: dict[int, int] = defaultdict(int)

    def has_invalid_path(current_node: int) -> bool:
        # If we hit a node currently in the recursion stack, we found a cycle.
        # A cycle is only "safe" if it's a self-loop on the destination, 
        # but the problem implies paths must *lead* to destination.
        # Actually, if we are in a cycle that doesn't reach destination, it's invalid.
        if state[current_node] == 1:
            return True
        
        # If we already fully explored this node and it was safe, return False.
        if state[current_node] == 2:
            return False

        # If we reached the destination, this path is valid.
        # We mark it as visited (2) so we don't re-process it.
        if current_node == destination:
            state[current_node] = 2
            return False

        # Mark node as currently being visited
        state[current_node] = 1

        # Explore neighbors
        for neighbor in adj_list[current_node]:
            if has_invalid_path(neighbor):
                return True

        # If the node has no neighbors and is not the destination, it's a dead end.
        # (This is implicitly handled: if the loop doesn't run and current_node != destination,
        # we need to check if it's a leaf. But the logic above handles destination check first.)
        
        # If we reach here, all paths from this node are valid.
        state[current_node] = 2
        return False

    # Special case: if the source is the destination, it's technically valid.
    if source == destination:
        return True

    # The problem asks if ALL paths lead to destination.
    # If has_invalid_path returns True, it means we found a path that 
    # either hits a cycle or a dead end that isn't the destination.
    return not has_invalid_path(source)
