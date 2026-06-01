METADATA = {
    "id": 3543,
    "name": "Maximum Weighted K-Edge Path",
    "slug": "maximum_weighted_k_edge_path",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dynamic_programming", "graph_traversal", "shortest_path"],
    "difficulty": "medium",
    "time_complexity": "O(K * (V + E))",
    "space_complexity": "O(K * V)",
    "description": "Find the maximum weight of a path consisting of exactly K edges in a weighted directed graph.",
}

def solve(n: int, edges: list[list[int]], k: int) -> int:
    """
    Finds the maximum weight of a path consisting of exactly K edges.

    Args:
        n: The number of nodes in the graph (nodes are 0-indexed).
        edges: A list of edges where each edge is [u, v, weight].
        k: The exact number of edges required in the path.

    Returns:
        The maximum weight of a path of length K. Returns -float('inf') if no such path exists.

    Examples:
        >>> solve(3, [[0, 1, 5], [1, 2, 10], [0, 2, 2]], 2)
        15
        >>> solve(3, [[0, 1, 5], [1, 2, 10]], 3)
        -float('inf')
    """
    # dp[i][u] represents the maximum weight of a path of length i ending at node u.
    # Initialize with negative infinity because we are looking for maximum weight.
    dp = [[-float('inf')] * n for _ in range(k + 1)]

    # Base case: A path of length 0 can end at any node with weight 0.
    for node in range(n):
        dp[0][node] = 0

    # Iterate through the number of edges from 1 to k.
    for i in range(1, k + 1):
        # For each edge, try to extend a path of length i-1 to a path of length i.
        for u, v, weight in edges:
            if dp[i - 1][u] != -float('inf'):
                # Update the maximum weight for node v at step i.
                new_weight = dp[i - 1][u] + weight
                if new_weight > dp[i][v]:
                    dp[i][v] = new_weight

    # The answer is the maximum value in the dp table for exactly k edges.
    max_path_weight = max(dp[k])
    
    return max_path_weight
