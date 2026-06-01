METADATA = {
    "id": 1571,
    "name": "Warehouse Manager",
    "slug": "warehouse-manager",
    "category": "Graph",
    "aliases": [],
    "tags": ["graph", "dfs", "bfs", "connectivity"],
    "difficulty": "medium",
    "time_complexity": "O(N + E)",
    "space_complexity": "O(N)",
    "description": "Determine if all nodes in a warehouse network are reachable from a specific starting node.",
}

def solve(num_nodes: int, edges: list[tuple[int, int]], start_node: int) -> bool:
    """
    Determines if all nodes in a warehouse network are reachable from a starting node.

    Args:
        num_nodes: The total number of nodes (warehouses) in the network.
        edges: A list of tuples representing directed connections between nodes.
        start_node: The index of the starting warehouse.

    Returns:
        True if every node from 0 to num_nodes - 1 is reachable, False otherwise.

    Examples:
        >>> solve(3, [(0, 1), (1, 2)], 0)
        True
        >>> solve(3, [(0, 1), (0, 2)], 0)
        True
        >>> solve(3, [(0, 1)], 0)
        False
    """
    if num_nodes == 0:
        return True

    # Build adjacency list for efficient graph traversal
    adjacency_list: dict[int, list[int]] = {i: [] for i in range(num_nodes)}
    for u, v in edges:
        if u < num_nodes:
            adjacency_list[u].append(v)

    # Use Breadth-First Search (BFS) to find all reachable nodes
    visited: set[int] = set()
    queue: list[int] = [start_node]
    visited.add(start_node)

    head = 0
    while head < len(queue):
        current_node = queue[head]
        head += 1

        for neighbor in adjacency_list.get(current_node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    # If the number of visited nodes equals the total nodes, all are reachable
    return len(visited) == num_nodes
