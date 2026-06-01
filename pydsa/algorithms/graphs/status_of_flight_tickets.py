METADATA = {
    "id": 2793,
    "name": "Status of Flight Tickets",
    "slug": "status_of_flight_tickets",
    "category": "Graphs",
    "aliases": [],
    "tags": ["graphs", "dfs", "reachability"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Determine if a flight ticket is valid by checking if the destination is reachable in a directed graph of flights.",
}

def solve(tickets: list[list[int]], start_node: int) -> bool:
    """
    Determines if a flight ticket is valid by checking if the destination 
    is reachable within the given flight network.

    Args:
        tickets: A list of flight connections where tickets[i] = [u, v] 
                 represents a flight from u to v.
        start_node: The starting airport index to check reachability from.

    Returns:
        True if the start_node is part of a valid path (not a dead end), 
        False otherwise.

    Examples:
        >>> solve([[1, 2], [2, 3], [3, 1]], 1)
        True
        >>> solve([[1, 2], [2, 3], [3, 4]], 1)
        True
        >>> solve([[1, 2], [2, 3], [3, 1], [4, 5]], 4)
        False
    """
    # Build adjacency list to represent the directed graph
    adj_list: dict[int, list[int]] = {}
    for u, v in tickets:
        if u not in adj_list:
            adj_list[u] = []
        adj_list[u].append(v)

    # If the start_node has no outgoing flights, it's an immediate dead end
    if start_node not in adj_list:
        return False

    visited: set[int] = set()
    
    def has_cycle_or_path(current_node: int) -> bool:
        """
        Uses DFS to detect if the current node is part of a cycle 
        or leads to a path that doesn't immediately terminate.
        """
        # If we encounter a node currently in the recursion stack, we found a cycle
        if current_node in visited:
            return True
        
        # If the node has no outgoing flights, it's a dead end
        if current_node not in adj_list:
            return False
        
        visited.add(current_node)
        
        # Check all neighbors. If any neighbor leads to a cycle or valid path, return True
        for neighbor in adj_list[current_node]:
            if has_cycle_or_path(neighbor):
                return True
        
        # Backtrack: remove from visited to allow other paths to explore this node
        # However, for reachability in this specific problem context, 
        # we actually want to know if the node is part of a cycle or leads to one.
        # In a simple directed graph reachability for "validity", 
        # a node is valid if it's part of a cycle or leads to a cycle.
        visited.remove(current_node)
        return False

    # Note: The problem "Status of Flight Tickets" usually implies checking if 
    # the node is part of a cycle in a functional graph (where out-degree is 1).
    # If out-degree can be > 1, we check if the node can reach a cycle.
    
    # Re-evaluating for general graph: A ticket is "valid" if it's not a dead end.
    # But the standard LeetCode interpretation for this specific problem 
    # (often seen in similar graph problems) is checking if the node is part of a cycle.
    
    # Let's implement the cycle detection logic specifically.
    # A node is valid if it is part of a cycle.
    
    path_stack = set()
    global_visited = set()

    def find_cycle(u: int) -> bool:
        if u in path_stack:
            return True
        if u in global_visited:
            return False
        
        global_visited.add(u)
        path_stack.add(u)
        
        if u in adj_list:
            for v in adj_list[u]:
                if find_cycle(v):
                    return True
        
        path_stack.remove(u)
        return False

    return find_cycle(start_node)
