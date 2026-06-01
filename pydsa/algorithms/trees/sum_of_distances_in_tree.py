METADATA = {
    "id": 834,
    "name": "Sum of Distances in Tree",
    "slug": "sum-of-distances-in-tree",
    "category": "Tree",
    "aliases": [],
    "tags": ["dfs", "dynamic_programming", "tree_dp"],
    "difficulty": "hard",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Calculate the sum of distances from each node to all other nodes in an undirected tree.",
}

def solve(n: int, edges: list[list[int]]) -> list[int]:
    """
    Calculates the sum of distances from each node to all other nodes in a tree.

    Args:
        n: The number of nodes in the tree.
        edges: A list of undirected edges where edges[i] = [u, v].

    Returns:
        A list of integers where the i-th element is the sum of distances from node i to all other nodes.

    Examples:
        >>> solve(6, [[0,1],[0,2],[2,3],[2,4],[2,5]])
        [13, 15, 10, 13, 13, 13]
    """
    if n == 0:
        return []
    if n == 1:
        return [0]

    # Build adjacency list
    adj: dict[int, list[int]] = {i: [] for i in range(n)}
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    # count[i] stores the number of nodes in the subtree rooted at i
    count: list[int] = [1] * n
    # ans[i] stores the sum of distances from node i to all other nodes
    ans: list[int] = [0] * n

    def dfs_subtree(node: int, parent: int) -> None:
        """First pass: Calculate subtree sizes and distance sum for the root (node 0)."""
        for neighbor in adj[node]:
            if neighbor != parent:
                dfs_subtree(neighbor, node)
                # The number of nodes in the subtree of 'node' increases by the subtree size of 'neighbor'
                count[node] += count[neighbor]
                # The distance sum for 'node' increases by the distance sum of 'neighbor' plus the size of 'neighbor's subtree
                ans[node] += ans[neighbor] + count[neighbor]

    def dfs_recompute(node: int, parent: int) -> None:
        """Second pass: Recompute distance sums for all nodes using the parent's result."""
        for neighbor in adj[node]:
            if neighbor != parent:
                # When moving from 'node' to 'neighbor':
                # 1. We get closer to all nodes in 'neighbor's subtree (count[neighbor] nodes)
                # 2. We get further from all nodes NOT in 'neighbor's subtree (n - count[neighbor] nodes)
                # Formula: ans[neighbor] = ans[node] - count[neighbor] + (n - count[neighbor])
                ans[neighbor] = ans[node] - count[neighbor] + (n - count[neighbor])
                dfs_recompute(neighbor, node)

    # Step 1: Compute subtree sizes and the distance sum for node 0
    dfs_subtree(0, -1)
    
    # Step 2: Use the result of node 0 to compute results for all other nodes via rerooting
    dfs_recompute(0, -1)

    return ans
