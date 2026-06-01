METADATA = {
    "id": 3067,
    "name": "Count Pairs of Connectable Servers in a Weighted Tree Network",
    "slug": "count-pairs-of-connectable-servers-in-a-weighted-tree-network",
    "category": "Graphs",
    "aliases": [],
    "tags": ["graphs", "dfs", "tree"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Count pairs of nodes in a tree that can be connected without passing through any node with a weight of zero.",
}

def solve(n: int, weights: list[int], edges: list[list[int]]) -> int:
    """
    Counts the number of pairs of servers that can be connected in a tree network
    without passing through any server with a weight of 0.

    Args:
        n: The number of servers.
        weights: A list of integers representing the weight of each server.
        edges: A list of edges where edges[i] = [u, v] represents a connection.

    Returns:
        The total number of pairs (i, j) with i < j such that the path between
        i and j contains only servers with weight > 0.

    Examples:
        >>> solve(3, [1, 0, 1], [[0, 1], [1, 2]])
        0
        >>> solve(4, [1, 1, 1, 1], [[0, 1], [1, 2], [2, 3]])
        6
    """
    # Build adjacency list
    adj: dict[int, list[int]] = {i: [] for i in range(n)}
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    total_pairs = 0

    # We treat nodes with weight 0 as "blockers".
    # The problem is equivalent to finding the sizes of connected components
    # formed only by nodes with weight > 0.
    # For a component of size K, the number of pairs is K * (K - 1) // 2.
    
    visited = [False] * n

    for i in range(n):
        # If node is already visited or is a blocker (weight 0), skip it
        if visited[i] or weights[i] == 0:
            continue
        
        # Start a BFS/DFS to find the size of the current valid component
        component_size = 0
        stack = [i]
        visited[i] = True
        
        while stack:
            curr = stack.pop()
            component_size += 1
            
            for neighbor in adj[curr]:
                # Only traverse to neighbors that are not visited and have weight > 0
                if not visited[neighbor] and weights[neighbor] > 0:
                    visited[neighbor] = True
                    stack.append(neighbor)
        
        # A component of size K allows for K*(K-1)/2 pairs
        if component_size > 1:
            total_pairs += (component_size * (component_size - 1)) // 2

    return total_pairs
