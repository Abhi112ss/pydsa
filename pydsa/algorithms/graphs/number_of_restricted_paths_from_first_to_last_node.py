METADATA = {
    "id": 1786,
    "name": "Number of Restricted Paths From First to Last Node",
    "slug": "number-of-restricted-paths-from-first-to-last-node",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dp", "bfs", "graph_traversal", "shortest_path"],
    "difficulty": "medium",
    "time_complexity": "O(n * (n + m))",
    "space_complexity": "O(n + m)",
    "description": "Count the number of restricted paths from node 1 to node n where a path is restricted if the distance between consecutive nodes is greater than the distance between the current node and node n.",
}

from collections import deque

def solve(n: int, edges: list[list[int]]) -> int:
    """
    Calculates the number of restricted paths from node 1 to node n.
    
    A path is restricted if for every consecutive pair of nodes (u, v) in the path,
    dist(u, n) > dist(v, n).

    Args:
        n: The number of nodes in the graph.
        edges: A list of undirected edges where edges[i] = [u, v].

    Returns:
        The number of restricted paths from node 1 to node n modulo 10^9 + 7.

    Examples:
        >>> solve(4, [[1, 2], [2, 3], [3, 4]])
        1
        >>> solve(3, [[1, 2], [2, 3], [1, 3]])
        2
    """
    MOD = 10**9 + 7
    
    # Build adjacency list
    adj: dict[int, list[int]] = {i: [] for i in range(1, n + 1)}
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    def get_distances_from(start_node: int) -> list[int]:
        """Standard BFS to find shortest distances from a specific node."""
        distances = [-1] * (n + 1)
        distances[start_node] = 0
        queue = deque([start_node])
        while queue:
            curr = queue.popleft()
            for neighbor in adj[curr]:
                if distances[neighbor] == -1:
                    distances[neighbor] = distances[curr] + 1
                    queue.append(neighbor)
        return distances

    # Step 1: Precompute distances from node n to all other nodes
    # This allows us to check the restriction: dist(u, n) > dist(v, n)
    dist_to_n = get_distances_from(n)

    # Step 2: Sort nodes by their distance to node n in ascending order.
    # This ensures that when we process node 'u', all nodes 'v' with 
    # dist(v, n) < dist(u, n) have already been processed (DP order).
    nodes_by_dist = sorted(range(1, n + 1), key=lambda x: dist_to_n[x])

    # Step 3: Dynamic Programming
    # dp[u] = number of restricted paths from node u to node n
    dp = [0] * (n + 1)
    dp[n] = 1  # Base case: there is 1 path from n to n (the empty path)

    for u in nodes_by_dist:
        if u == n:
            continue
        
        # A path from u to n is valid if we move to a neighbor v 
        # such that dist(u, n) > dist(v, n)
        current_dist = dist_to_n[u]
        for v in adj[u]:
            if current_dist > dist_to_n[v]:
                dp[u] = (dp[u] + dp[v]) % MOD

    return dp[1]
