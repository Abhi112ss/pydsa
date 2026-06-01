METADATA = {
    "id": 2603,
    "name": "Collect Coins in a Tree",
    "slug": "collect-coins-in-a-tree",
    "category": "Tree",
    "aliases": [],
    "tags": ["dfs", "tree", "degree_reduction", "topological_sort"],
    "difficulty": "hard",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Calculate the minimum number of edges to traverse to collect all coins in a tree, where coins are at leaves and can be collected from distance k.",
}

from collections import deque

def solve(edges: list[list[int]], k: int) -> int:
    """
    Calculates the minimum number of edges to traverse to collect all coins.
    
    The strategy is to iteratively prune all leaf nodes k times. 
    After k rounds of pruning leaves, the remaining edges represent the 
    path required to traverse the core of the tree.
    
    Args:
        edges: A list of undirected edges representing the tree.
        k: The maximum distance from which a coin can be collected.
        
    Returns:
        The minimum number of edges to traverse.
        
    Examples:
        >>> solve([[1,2],[2,3],[3,4],[4,5],[5,6]], 2)
        2
        >>> solve([[1,2],[2,3],[3,4],[4,5],[5,6]], 1)
        4
    """
    n = len(edges) + 1
    if n <= 2 * k + 1:
        return 0

    adj = [set() for _ in range(n)]
    degree = [0] * n
    for u, v in edges:
        adj[u].add(v)
        adj[v].add(u)
        degree[u] += 1
        degree[v] += 1

    # Step 1: Prune all leaves k times to remove nodes that can collect coins
    # from a distance of k.
    leaves = deque([i for i in range(n) if degree[i] == 1])
    remaining_nodes = n
    
    for _ in range(k):
        leaves_count = len(leaves)
        for _ in range(leaves_count):
            leaf = leaves.popleft()
            remaining_nodes -= 1
            # Find the neighbor of the leaf to update its degree
            for neighbor in adj[leaf]:
                adj[neighbor].remove(leaf)
                degree[neighbor] -= 1
                if degree[neighbor] == 1:
                    leaves.append(neighbor)
            # Effectively remove the leaf
            degree[leaf] = 0

    # Step 2: After pruning k layers, we are left with the core nodes.
    # To collect coins from these nodes, we must traverse the edges 
    # connecting them. However, we can collect coins from distance 2 
    # from the remaining nodes. This is equivalent to pruning 2 more layers.
    
    # Re-identify current leaves in the pruned tree
    current_leaves = deque([i for i in range(n) if degree[i] == 1])
    
    # Prune 2 more layers to find the minimal path (the core edges)
    for _ in range(2):
        leaves_count = len(current_leaves)
        for _ in range(leaves_count):
            leaf = current_leaves.popleft()
            remaining_nodes -= 1
            for neighbor in adj[leaf]:
                adj[neighbor].remove(leaf)
                degree[neighbor] -= 1
                if degree[neighbor] == 1:
                    current_leaves.append(neighbor)
            degree[leaf] = 0

    # The number of edges in a tree is (number of nodes - 1).
    # If remaining_nodes <= 1, it means we've pruned everything or just one node.
    return max(0, remaining_nodes - 1) * 2
