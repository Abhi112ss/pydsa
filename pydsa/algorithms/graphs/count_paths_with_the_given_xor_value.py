METADATA = {
    "id": 3393,
    "name": "Count Paths With the Given XOR Value",
    "slug": "count-paths-with-the-given-xor-value",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dp", "dfs", "graphs", "bit-manipulation"],
    "difficulty": "hard",
    "time_complexity": "O(N * K)",
    "space_complexity": "O(N * K)",
    "description": "Count the number of paths in a tree that result in a specific XOR sum of node values.",
}

def solve(n: int, edges: list[list[int]], values: list[int], k: int) -> int:
    """
    Counts the number of paths in a tree where the XOR sum of node values equals k.
    
    The problem asks for paths in a tree. In a tree, a path is uniquely defined 
    by its two endpoints. However, the problem context (based on standard tree path 
    counting) usually implies paths starting from any node. Since it's a tree, 
    we can use DP on trees or a DFS approach to count paths.
    
    Args:
        n: The number of nodes in the tree.
        edges: A list of undirected edges [u, v].
        values: The value associated with each node.
        k: The target XOR sum.

    Returns:
        The total number of paths whose node values XOR to k.

    Examples:
        >>> solve(3, [[0, 1], [1, 2]], [1, 2, 3], 0)
        1
    """
    from collections import defaultdict

    # Build adjacency list
    adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    MOD = 10**9 + 7
    total_paths = 0

    # dp[u][current_xor] stores the number of paths starting from node u 
    # and going down into its subtree that result in current_xor.
    # Note: To avoid double counting and handle all paths, we use a 
    # standard tree DP approach where we count paths passing through 'u'.
    
    def dfs(u: int, p: int) -> dict[int, int]:
        nonlocal total_paths
        
        # current_node_paths[x] = number of paths starting at u and ending in u's subtree with XOR sum x
        current_node_paths = {values[u]: 1}
        
        # If the single node u itself satisfies the condition
        if values[u] == k:
            total_paths = (total_paths + 1) % MOD

        for v in adj[u]:
            if v == p:
                continue
            
            child_paths = dfs(v, u)
            
            # Before merging child_paths into current_node_paths, 
            # count paths that pass through u by combining a path from 
            # the current subtree of u and a path from the new subtree of v.
            for xor_u, count_u in current_node_paths.items():
                for xor_v, count_v in child_paths.items():
                    # The path is (path in u's existing subtree) -> u -> (path in v's subtree)
                    # However, current_node_paths already includes values[u].
                    # The child_paths contains XOR sums of paths starting at v.
                    # To form a path through u: (path_u_ending_at_u) XOR (path_v_starting_at_v)
                    # But current_node_paths[xor_u] already includes values[u].
                    # The correct logic: path_u (ends at u) XOR path_v (starts at v)
                    # Since path_u includes values[u], and path_v does NOT include values[u],
                    # the combined XOR is xor_u ^ xor_v.
                    # Wait, the child_paths returned by dfs(v) should be paths starting at v.
                    # So path_u ^ path_v is the XOR sum of the path.
                    if (xor_u ^ xor_v) == k:
                        total_paths = (total_paths + (count_u * count_v)) % MOD

            # Merge child_paths into current_node_paths
            # A path starting at u and going into v's subtree has XOR: values[u] ^ xor_v
            for xor_v, count_v in child_paths.items():
                new_xor = values[u] ^ xor_v
                current_node_paths[new_xor] = (current_node_paths.get(new_xor, 0) + count_v) % MOD
                
        return current_node_paths

    # The problem asks for paths. In a tree, every path is uniquely identified by its endpoints.
    # The DFS above counts paths where 'u' is the highest node (LCA) of the path.
    dfs(0, -1)
    
    return total_paths
