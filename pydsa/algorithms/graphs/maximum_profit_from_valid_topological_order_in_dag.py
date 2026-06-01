METADATA = {
    "id": 3530,
    "name": "Maximum Profit from Valid Topological Order in DAG",
    "slug": "maximum-profit-from-valid-topological-order-in-dag",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dag", "dynamic_programming", "topological_sort"],
    "difficulty": "medium",
    "time_complexity": "O(V + E)",
    "space_complexity": "O(V + E)",
    "description": "Find the maximum profit achievable by traversing a path in a Directed Acyclic Graph where each node has a specific profit value.",
}

def solve(num_nodes: int, edges: list[list[int]], node_profits: list[int]) -> int:
    """
    Calculates the maximum profit achievable by following a path in a DAG.

    Args:
        num_nodes: The number of nodes in the graph (labeled 0 to num_nodes - 1).
        edges: A list of directed edges where edges[i] = [u, v] represents an edge from u to v.
        node_profits: A list where node_profits[i] is the profit gained by visiting node i.

    Returns:
        The maximum profit possible from any valid path in the DAG.

    Examples:
        >>> solve(3, [[0, 1], [1, 2]], [10, 20, 30])
        60
        >>> solve(4, [[0, 1], [0, 2], [1, 3], [2, 3]], [5, 10, 5, 20])
        35
    """
    # Build adjacency list and calculate in-degrees for topological sort
    adj = [[] for _ in range(num_nodes)]
    in_degree = [0] * num_nodes
    for u, v in edges:
        adj[u].append(v)
        in_degree[v] += 1

    # Kahn's algorithm for topological sort
    queue = []
    for i in range(num_nodes):
        if in_degree[i] == 0:
            queue.append(i)

    # dp[i] stores the maximum profit ending at node i
    # Initialize with the profit of the node itself
    dp = [profit for profit in node_profits]
    
    # Process nodes in topological order
    head = 0
    while head < len(queue):
        u = queue[head]
        head += 1
        
        for v in adj[u]:
            # Relaxation step: if path through u to v is better, update dp[v]
            if dp[u] + node_profits[v] > dp[v]:
                dp[v] = dp[u] + node_profits[v]
            
            in_degree[v] -= 1
            if in_degree[v] == 0:
                queue.append(v)

    # The answer is the maximum value found in the DP array
    return max(dp) if dp else 0
