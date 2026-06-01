METADATA = {
    "id": 2959,
    "name": "Number of Possible Sets of Closing Branches",
    "slug": "number-of-possible-sets-of-closing-branches",
    "category": "Trees",
    "aliases": [],
    "tags": ["trees", "dp", "dynamic programming"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Count the number of ways to close branches in a tree such that every node has at most one child that remains open.",
}

def solve(n: int, edges: list[list[int]]) -> int:
    """
    Calculates the number of ways to close branches in a tree such that 
    each node has at most one child that remains open.

    Args:
        n: The number of nodes in the tree.
        edges: A list of undirected edges representing the tree structure.

    Returns:
        The number of valid ways to close branches modulo 10^9 + 7.

    Examples:
        >>> solve(3, [[0, 1], [0, 2]])
        2
        >>> solve(4, [[0, 1], [1, 2], [2, 3]])
        4
    """
    MOD = 10**9 + 7
    
    # Build adjacency list
    adj: dict[int, list[int]] = {i: [] for i in range(n)}
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    # dp[u][0]: Number of ways to configure subtree at u such that u's connection 
    # to its parent is CLOSED.
    # dp[u][1]: Number of ways to configure subtree at u such that u's connection 
    # to its parent is OPEN.
    dp0 = [0] * n
    dp1 = [0] * n

    def dfs(u: int, p: int) -> None:
        # Base case: leaf node
        # If connection to parent is closed, there is 1 way (the node itself).
        # If connection to parent is open, there is 1 way (the node itself).
        # However, the logic is easier if we treat the "open" state as 
        # "this node is part of an active path from the parent".
        
        # product_all_closed: product of dp0[v] for all children v.
        # This represents the case where all children's connections to u are closed.
        product_all_closed = 1
        children = []
        
        for v in adj[u]:
            if v == p:
                continue
            dfs(v, u)
            children.append(v)
            product_all_closed = (product_all_closed * dp0[v]) % MOD

        # Case 1: u's connection to parent is CLOSED (dp0[u])
        # u can have at most one child v such that the edge (u, v) is OPEN.
        # If no child is open: product_all_closed
        # If exactly one child v is open: sum over all v of (dp1[v] * product_{w != v} dp0[w])
        # This can be calculated as: product_all_closed * sum(dp1[v] / dp0[v])
        # To avoid division (and handle dp0[v] == 0), we use the sum of (dp1[v] * product_others)
        
        ways_to_have_one_open_child = 0
        # We use a prefix/suffix product approach or simply iterate if we want to be safe,
        # but since we need to sum (dp1[v] * product_{w != v} dp0[w]), 
        # we can use the property: (dp1[v] * product_all_closed) / dp0[v] if dp0[v] != 0.
        # A more robust way for O(N) is prefix and suffix products.
        
        m = len(children)
        if m == 0:
            dp0[u] = 1
            dp1[u] = 1
            return

        prefix = [1] * (m + 1)
        suffix = [1] * (m + 1)
        
        for i in range(m):
            prefix[i+1] = (prefix[i] * dp0[children[i]]) % MOD
        for i in range(m - 1, -1, -1):
            suffix[i] = (suffix[i+1] * dp0[children[i]]) % MOD
            
        # Summing ways where exactly one child is open
        for i in range(m):
            # ways = (product of dp0 for all children except i) * dp1[i]
            term = (prefix[i] * suffix[i+1]) % MOD
            term = (term * dp1[children[i]]) % MOD
            ways_to_have_one_open_child = (ways_to_have_one_open_child + term) % MOD
            
        dp0[u] = (product_all_closed + ways_to_have_one_open_child) % MOD
        
        # Case 2: u's connection to parent is OPEN (dp1[u])
        # If u's connection to parent is open, u can have NO children with open connections.
        # Because if u has an open connection to parent AND an open connection to a child,
        # u would have two open connections, which is forbidden.
        # Therefore, all children must have their connections to u CLOSED.
        dp1[u] = product_all_closed

    # Start DFS from root 0
    dfs(0, -1)
    
    # The answer is dp0[0] because the root has no parent (effectively connection to parent is closed)
    return dp0[0]
