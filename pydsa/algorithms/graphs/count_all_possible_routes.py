METADATA = {
    "id": 1575,
    "name": "Count All Possible Routes",
    "slug": "count-all-possible-routes",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dfs", "graph", "dynamic programming", "memoization"],
    "difficulty": "medium",
    "time_complexity": "O(n + e)",
    "space_complexity": "O(n)",
    "description": "Count the number of possible routes from any node to a destination node in a directed acyclic graph.",
}

def solve(n: int, edges: list[list[int]], destination: int) -> int:
    """
    Counts the number of possible routes from any node to the destination node.

    Args:
        n: The number of nodes in the graph.
        edges: A list of directed edges where edges[i] = [from_i, to_i].
        destination: The target node index.

    Returns:
        The total number of routes from all nodes to the destination.

    Examples:
        >>> solve(4, [[0,1],[0,2],[1,3],[2,3]], 3)
        6
        >>> solve(3, [[0,1],[1,2]], 2)
        3
    """
    MOD = 10**9 + 7
    
    # Build adjacency list for the graph
    adj: dict[int, list[int]] = {i: [] for i in range(n)}
    for u, v in edges:
        adj[u].append(v)
        
    # memo[i] stores the number of routes from node i to destination
    memo: list[int] = [-1] * n

    def dfs(current_node: int) -> int:
        # Base case: if we reached the destination, there is 1 route (staying put)
        if current_node == destination:
            return 1
        
        # Return cached result if already computed
        if memo[current_node] != -1:
            return memo[current_node]
        
        total_routes = 0
        # Explore all neighbors and sum up their routes to destination
        for neighbor in adj[current_node]:
            total_routes = (total_routes + dfs(neighbor)) % MOD
            
        memo[current_node] = total_routes
        return total_routes

    # Sum up routes from every node to the destination
    total_sum = 0
    for i in range(n):
        total_sum = (total_sum + dfs(i)) % MOD
        
    return total_sum
