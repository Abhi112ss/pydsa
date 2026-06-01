METADATA = {
    "id": 2477,
    "name": "Minimum Fuel Cost to Report to the Capital",
    "slug": "minimum-fuel-cost-to-report-to-the-capital",
    "category": "Graph",
    "aliases": [],
    "tags": ["dfs", "graphs", "tree"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Calculate the minimum fuel cost to report to the capital where each edge cost depends on the number of nodes in the subtree it connects.",
}

def solve(n: int, routes: list[list[int]]) -> int:
    """
    Calculates the minimum fuel cost for all nodes to report to the capital (node 0).
    
    The cost of traversing an edge is equal to the number of nodes in the subtree 
    that must pass through that edge to reach the capital.

    Args:
        n: The number of nodes in the tree.
        routes: A list of edges where routes[i] = [u, v] represents an edge between u and v.

    Returns:
        The total minimum fuel cost.

    Examples:
        >>> solve(4, [[0, 1], [1, 2], [1, 3]])
        4
        >>> solve(2, [[0, 1]])
        1
    """
    # Build adjacency list
    adj: dict[int, list[int]] = {i: [] for i in range(n)}
    for u, v in routes:
        adj[u].append(v)
        adj[v].append(u)

    total_fuel = 0

    def dfs(current_node: int, parent_node: int) -> int:
        """
        Performs DFS to count nodes in subtrees and accumulate fuel costs.
        
        Args:
            current_node: The node currently being visited.
            parent_node: The parent of the current node to avoid cycles.

        Returns:
            The number of nodes in the subtree rooted at current_node.
        """
        nonlocal total_fuel
        subtree_size = 1  # Count the current node itself
        
        for neighbor in adj[current_node]:
            if neighbor != parent_node:
                # Recursively find the size of the child's subtree
                child_subtree_size = dfs(neighbor, current_node)
                
                # The edge between current_node and neighbor must be traversed 
                # by every node in the child's subtree.
                total_fuel += child_subtree_size
                
                # Add child's subtree size to current node's subtree size
                subtree_size += child_subtree_size
                
        return subtree_size

    # Start DFS from the capital (node 0)
    dfs(0, -1)
    
    return total_fuel
