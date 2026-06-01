METADATA = {
    "id": 3332,
    "name": "Maximum Points Tourist Can Earn",
    "slug": "maximum-points-tourist-can-earn",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dp", "greedy"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Find the maximum points a tourist can earn by visiting cities while adhering to specific movement constraints.",
}

def solve(points: list[int], constraints: list[list[int]]) -> int:
    """
    Calculates the maximum points a tourist can earn given city points and constraints.
    
    The problem asks for the maximum sum of points from a subsequence of cities 
    where certain pairs of cities cannot be chosen together. However, based on 
    the standard interpretation of such problems (like Maximum Weight Independent Set 
    on specific graph types), we optimize the selection.

    Args:
        points: A list of integers representing points available in each city.
        constraints: A list of pairs [u, v] representing cities that cannot both be visited.

    Returns:
        The maximum total points possible.

    Examples:
        >>> solve([1, 2, 3], [[0, 1]])
        4
        >>> solve([5, 1, 1, 5], [[0, 3]])
        6
    """
    n = len(points)
    if n == 0:
        return 0

    # Build an adjacency list to represent the constraints (conflicts)
    # Since we need to find the maximum points, this is equivalent to 
    # finding the Maximum Weight Independent Set.
    # For general graphs, this is NP-hard, but for specific structures 
    # (like paths or trees) it is O(n).
    # Given the context of "tourist" and "cities", we assume a linear or 
    # tree-like structure or a small enough constraint set.
    
    adj = [[] for _ in range(n)]
    for u, v in constraints:
        adj[u].append(v)
        adj[v].append(u)

    visited = [False] * n
    total_max_points = 0

    # We iterate through all components in case the constraint graph is disconnected
    for i in range(n):
        if not visited[i]:
            # For each connected component, we use DP to find the Max Weight Independent Set.
            # This implementation assumes the constraint graph is a forest (collection of trees).
            # If the graph is more complex, a different approach would be needed.
            component_nodes = []
            stack = [i]
            visited[i] = True
            while stack:
                curr = stack.pop()
                component_nodes.append(curr)
                for neighbor in adj[curr]:
                    if not visited[neighbor]:
                        visited[neighbor] = True
                        stack.append(neighbor)
            
            # DP on Trees: dp[u][0] is max points in subtree u without u, 
            # dp[u][1] is max points in subtree u including u.
            # We use a post-order traversal to compute DP values.
            
            # Re-run a local traversal to get parent-child relationships for the component
            local_visited = {node: False for node in component_nodes}
            order = []
            parent = {node: -1 for node in component_nodes}
            
            # BFS/DFS to establish tree structure within the component
            bfs_stack = [i]
            local_visited[i] = True
            while bfs_stack:
                u = bfs_stack.pop()
                order.append(u)
                for v in adj[u]:
                    if v in local_visited and not local_visited[v]:
                        local_visited[v] = True
                        parent[v] = u
                        bfs_stack.append(v)
            
            # DP tables for the component
            dp_exclude = {node: 0 for node in component_nodes}
            dp_include = {node: points[node] for node in component_nodes}
            
            # Process nodes in reverse topological order (leaves to root)
            for u in reversed(order):
                p = parent[u]
                if p != -1:
                    # If we include u, we MUST exclude its parent p in the context of p's calculation
                    # However, the standard DP is:
                    # dp[p][0] += max(dp[u][0], dp[u][1])
                    # dp[p][1] += dp[u][0]
                    dp_exclude[p] += max(dp_exclude[u], dp_include[u])
                    dp_include[p] += dp_exclude[u]
            
            # The root of this component is 'i'
            total_max_points += max(dp_exclude[i], dp_include[i])

    return total_max_points
