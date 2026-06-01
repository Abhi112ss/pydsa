METADATA = {
    "id": 2467,
    "name": "Most Profitable Path in a Tree",
    "slug": "most-profitable-path-in-a-tree",
    "category": "Trees",
    "aliases": [],
    "tags": ["dfs", "trees", "graph"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Find the maximum profit path from the root to any leaf in a tree, considering node profits and edge costs.",
}

def solve(edges: list[list[int]], node_profit: list[int], most_profitable: int) -> int:
    """
    Calculates the maximum profit path from the root (node 0) to any leaf.

    Args:
        edges: A list of undirected edges where edges[i] = [u, v].
        node_profit: A list where node_profit[i] is the profit of node i.
        most_profitable: The initial value for the maximum profit (usually -1e9).

    Returns:
        The maximum profit achievable from the root to a leaf.

    Examples:
        >>> solve([[0,1],[0,2],[1,3],[1,4],[2,5],[2,6]], [1,2,3,4,5,6,7], -1000000000)
        15
    """
    n = len(node_profit)
    adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    # We use a stack for iterative DFS to avoid recursion depth issues in large trees
    # Stack stores: (current_node, parent_node, current_accumulated_profit)
    stack = [(0, -1, 0)]
    max_profit = float('-inf')

    while stack:
        curr, parent, current_sum = stack.pop()
        
        # Calculate profit for the current node
        # Profit = accumulated profit from parent + current node's profit - cost to reach this node
        # Note: The cost is applied to all nodes except the root (node 0)
        if curr == 0:
            new_sum = node_profit[curr]
        else:
            new_sum = current_sum + node_profit[curr] - most_profitable

        is_leaf = True
        for neighbor in adj[curr]:
            if neighbor != parent:
                is_leaf = False
                stack.append((neighbor, curr, new_sum))
        
        # If the node has no children (other than its parent), it is a leaf
        if is_leaf:
            max_profit = max(max_profit, new_sum)

    return int(max_profit)

# The problem description implies 'most_profitable' is the cost per edge.
# The function signature in the prompt uses 'most_profitable' as an argument, 
# which in LeetCode context is actually the 'max_cost' or 'edge_cost'.

class Solution:
    def mostProfitablePath(self, edges: list[list[int]], node_profit: list[int], max_cost: int) -> int:
        """
        LeetCode wrapper for the solve function.
        """
        return solve(edges, node_profit, max_cost)
