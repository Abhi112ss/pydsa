METADATA = {
    "id": 2714,
    "name": "Find Shortest Path with K Hops",
    "slug": "find-shortest-path-with-k-hops",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["graphs", "dp", "bfs"],
    "difficulty": "medium",
    "time_complexity": "O(k * (V + E))",
    "space_complexity": "O(V)",
    "description": "Find the shortest path from a source node to a destination node using exactly k edges in a weighted graph.",
}

def solve(n: int, edges: list[list[int]], source: int, destination: int, k: int) -> int:
    """
    Finds the shortest path from source to destination using exactly k edges.

    Args:
        n: The number of nodes in the graph.
        edges: A list of edges where edges[i] = [u, v, weight].
        source: The starting node.
        destination: The target node.
        k: The exact number of edges (hops) required.

    Returns:
        The shortest path distance, or -1 if no such path exists.

    Examples:
        >>> solve(4, [[0,1,1], [1,2,1], [2,3,1], [0,3,5]], 0, 3, 3)
        3
        >>> solve(4, [[0,1,1], [1,2,1], [2,3,1], [0,3,5]], 0, 3, 1)
        5
    """
    # Use float('inf') to represent unreachable nodes
    inf = float('inf')
    
    # dp[v] stores the shortest distance to node v using 'current_k' edges.
    # We only need the previous state (k-1 edges) to calculate the current state (k edges).
    dp = [inf] * n
    dp[source] = 0

    # Iterate k times, once for each hop required
    for _ in range(k):
        # next_dp will store the shortest distances using exactly one more edge
        next_dp = [inf] * n
        
        # Relax all edges for the current hop
        for u, v, weight in edges:
            # If node u was reachable in the previous step
            if dp[u] != inf:
                # Update the distance to node v for the current step
                if dp[u] + weight < next_dp[v]:
                    next_dp[v] = dp[u] + weight
            
            # Note: If the graph is undirected, we would also check:
            # if dp[v] != inf:
            #     if dp[v] + weight < next_dp[u]:
            #         next_dp[u] = dp[v] + weight
            # However, standard LeetCode edge lists are usually directed unless specified.
            # For this specific problem structure, we assume directed edges.
            # If the problem implies undirected, the logic above should be applied.
            # Given the prompt context, we treat edges as directed.
            
        # Move to the next hop state
        dp = next_dp

    result = dp[destination]
    return int(result) if result != inf else -1
