METADATA = {
    "id": 3812,
    "name": "Minimum Edge Toggles on a Tree",
    "slug": "minimum-edge-toggles-on-a-tree",
    "category": "Trees",
    "aliases": [],
    "tags": ["dfs", "dp", "trees"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Find the minimum number of edge toggles required to satisfy node parity constraints in a tree.",
}

def solve(n: int, edges: list[list[int]], constraints: list[int]) -> int:
    """
    Calculates the minimum number of edge toggles needed to satisfy node parity constraints.
    
    Each node i has a constraint constraints[i]. An edge toggle flips the parity 
    of the two connected nodes. We need to find if a valid configuration exists 
    and return the minimum toggles.

    Args:
        n: The number of nodes in the tree.
        edges: A list of undirected edges where edges[i] = [u, v].
        constraints: A list where constraints[i] is the required parity (0 or 1) 
                     for node i.

    Returns:
        The minimum number of edge toggles required, or -1 if impossible.

    Examples:
        >>> solve(3, [[0, 1], [1, 2]], [1, 0, 1])
        1
        >>> solve(3, [[0, 1], [1, 2]], [1, 1, 1])
        -1
    """
    # Build adjacency list
    adj: dict[int, list[int]] = {i: [] for i in range(n)}
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    # total_toggles tracks the count of edges we decide to 'flip'
    total_toggles = 0
    # visited array to handle tree traversal without recursion depth issues if needed
    # but for standard tree problems, a post-order DFS is standard.
    visited = [False] * n
    
    # We use a post-order traversal to decide whether to toggle the edge 
    # connecting a node to its parent.
    # The decision for edge (u, parent) is forced by the current parity of u.
    
    def dfs(u: int, p: int) -> int:
        """
        Returns the current parity of node u after all toggles in its subtree.
        """
        nonlocal total_toggles
        visited[u] = True
        
        # current_parity represents the parity of node u after processing children
        current_parity = constraints[u]
        
        for v in adj[u]:
            if v == p:
                continue
            
            # child_parity is the parity of the child after its subtree is processed
            child_parity = dfs(v, u)
            
            # If the child's parity does not match its constraint, 
            # we MUST toggle the edge (u, v).
            if child_parity != constraints[v]:
                total_toggles += 1
                # Toggling the edge (u, v) flips the parity of both u and v.
                # Since we already satisfied v, we only care about the flip on u.
                current_parity = 1 - current_parity
                
        return current_parity

    # Start DFS from root (node 0)
    # Note: In a tree, the root's parity must match its constraint after all toggles.
    # However, the logic above is slightly different: 
    # We check if the child needs a toggle to satisfy its OWN constraint.
    
    # Let's refine the logic:
    # A node u is satisfied if its parity matches constraints[u].
    # We process bottom-up. For a leaf, if it doesn't match, we toggle (leaf, parent).
    # This toggle affects the parent.
    
    # Re-implementing logic clearly:
    # dfs(u) returns the parity of node u AFTER all edges in its subtree have been toggled.
    
    def dfs_refined(u: int, p: int) -> int:
        nonlocal total_toggles
        visited[u] = True
        
        # current_parity starts as the initial constraint
        current_parity = constraints[u]
        
        for v in adj[u]:
            if v == p:
                continue
            
            # Get the parity of the child after its subtree is processed
            child_parity = dfs_refined(v, u)
            
            # If child_parity != constraints[v], we MUST toggle edge (u, v)
            if child_parity != constraints[v]:
                total_toggles += 1
                # Toggling (u, v) flips the parity of u
                current_parity = 1 - current_parity
                
        return current_parity

    # The root's parity must also match its constraint.
    # But wait, the root has no parent to toggle with. 
    # If the root's parity doesn't match, it's impossible.
    
    # Let's use a more robust approach:
    # The sum of constraints must have the same parity as the sum of toggles * 2? 
    # No, each toggle changes parity of 2 nodes. 
    # So sum(constraints) % 2 must be 0 if we consider parity as 0/1.
    # Actually, the rule is: sum(constraints) % 2 == 0 is NOT required.
    # Each toggle flips two nodes. So (sum of parities) changes by 0 or +/- 2.
    # Therefore, sum(constraints) % 2 must be equal to sum(initial_parities) % 2.
    # Since initial parities are all 0 (if we consider toggles as the only source of 1s),
    # the sum of constraints must be even.
    
    # Wait, the problem implies constraints are the TARGET parities.
    # Let's assume initial state is all nodes have parity 0.
    # Each toggle adds 1 to the parity of two nodes.
    # Thus, sum(constraints) must be even.
    
    if sum(constraints) % 2 != 0:
        return -1

    # Reset for the actual logic
    total_toggles = 0
    visited = [False] * n
    
    # The logic: 
    # 1. Traverse bottom up.
    # 2. If child v's current parity != constraints[v], toggle (u, v).
    # 3. This toggle flips parity of u and v.
    # 4. After processing all children, check if root satisfies constraints[root].
    
    # We need to track the "current" parity of each node.
    # Let's use an array to track parity changes.
    current_node_parity = [0] * n
    
    def dfs_final(u: int, p: int) -> None:
        nonlocal total_toggles
        visited[u] = True
        
        for v in adj[u]:
            if v == p:
                continue
            dfs_final(v, u)
            
            # After child v is processed, check if v's parity matches constraints[v]
            # v's parity is (initial_parity[v] + toggles_on_edges_connected_to_v) % 2
            # Since initial is 0, it's just (toggles_on_edges_connected_to_v) % 2
            if current_node_parity[v] != constraints[v]:
                total_toggles += 1
                current_node_parity[v] = 1 - current_node_parity[v]
                current_node_parity[u] = 1 - current_node_parity[u]

    dfs_final(0, -1)
    
    # Final check for root
    if current_node_parity[0] != constraints[0]:
        return -1
        
    return total_toggles
