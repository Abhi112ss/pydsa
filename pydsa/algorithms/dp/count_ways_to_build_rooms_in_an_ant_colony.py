METADATA = {
    "id": 1916,
    "name": "Count Ways to Build Rooms in an Ant Colony",
    "slug": "count-ways-to-build-rooms-in-an-ant-colony",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dynamic_programming", "combinatorics", "trees"],
    "difficulty": "hard",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Count the number of valid topological sorts of a tree structure modulo 10^9 + 7.",
}

def solve(n: int, parent: list[int]) -> int:
    """
    Calculates the number of valid ways to build rooms given a parent array.
    The parent array represents a tree where parent[i] is the parent of room i.
    A room can only be built after its parent is built.

    Args:
        n: The total number of rooms.
        parent: A list where parent[i] is the parent of room i. 
                parent[i] = -1 indicates room i is the root.

    Returns:
        The number of valid sequences to build rooms modulo 10^9 + 7.

    Examples:
        >>> solve(3, [-1, 0, 0])
        2
        >>> solve(3, [-1, 0, 1])
        1
    """
    MOD = 1_000_000_007

    # Build adjacency list to represent the tree
    adj = [[] for _ in range(n)]
    root = -1
    for i, p in enumerate(parent):
        if p == -1:
            root = i
        else:
            adj[p].append(i)

    # Precompute factorials and inverse factorials for combinations
    # We need combinations up to n
    fact = [1] * (n + 1)
    inv_fact = [1] * (n + 1)
    for i in range(1, n + 1):
        fact[i] = (fact[i - 1] * i) % MOD

    # Modular inverse using Fermat's Little Theorem
    inv_fact[n] = pow(fact[n], MOD - 2, MOD)
    for i in range(n - 1, -1, -1):
        inv_fact[i] = (inv_fact[i + 1] * (i + 1)) % MOD

    def nCr(n_val: int, r_val: int) -> int:
        if r_val < 0 or r_val > n_val:
            return 0
        num = fact[n_val]
        den = (inv_fact[r_val] * inv_fact[n_val - r_val]) % MOD
        return (num * den) % MOD

    # subtree_size[u] stores the number of nodes in the subtree rooted at u
    # ways[u] stores the number of valid topological sorts for the subtree rooted at u
    subtree_size = [0] * n
    ways = [0] * n

    # Iterative DFS to avoid recursion depth issues in Python
    # Post-order traversal is required to compute subtree properties
    stack = [(root, False)]
    order = []
    
    while stack:
        u, visited = stack.pop()
        if visited:
            order.append(u)
        else:
            stack.append((u, True))
            for v in adj[u]:
                stack.append((v, False))

    # Process nodes in post-order (bottom-up)
    for u in order:
        current_size = 1
        current_ways = 1
        
        for v in adj[u]:
            # The number of ways to interleave the sequences of children subtrees
            # is calculated using the formula: 
            # ways[u] = Product(ways[child] * nCr(total_size_so_far + child_size, child_size))
            current_ways = (current_ways * ways[v]) % MOD
            current_ways = (current_ways * nCr(current_size + subtree_size[v] - 1, subtree_size[v])) % MOD
            current_size += subtree_size[v]
            
        subtree_size[u] = current_size
        ways[u] = current_ways

    # The result is the number of ways to arrange the entire tree starting from root
    # However, the formula above calculates ways to arrange children relative to each other.
    # For a tree, the total ways is: (n! / Product of subtree_size[i] for all i)
    # But since we are building bottom-up, the 'ways[root]' already accumulates this.
    # Let's re-verify: the standard formula for tree topological sorts is n! / Product(subtree_size[i]).
    
    # Let's use the direct formula for efficiency and correctness:
    # Total ways = n! / Product_{i=0}^{n-1} (subtree_size[i])
    
    # Re-calculating subtree sizes using a simple post-order traversal
    # (The 'order' list from before is already post-order)
    actual_subtree_size = [1] * n
    for u in order:
        for v in adj[u]:
            actual_subtree_size[u] += actual_subtree_size[v]
            
    ans = fact[n]
    for i in range(n):
        # Divide by subtree_size[i] using modular inverse
        ans = (ans * pow(actual_subtree_size[i], MOD - 2, MOD)) % MOD
        
    return ans
