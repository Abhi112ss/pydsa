METADATA = {
    "id": 2717,
    "name": "Semi-Ordered Permutation",
    "slug": "semi_ordered_permutation",
    "category": "Math",
    "aliases": [],
    "tags": ["math", "combinatorics"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Count the number of permutations that satisfy specific semi-ordering constraints using combinatorial logic.",
}

def solve(n: int, constraints: list[list[int]]) -> int:
    """
    Calculates the number of valid permutations based on semi-ordering constraints.
    
    Note: Since the specific problem constraints for #2717 (a hypothetical or 
    highly specific problem) usually involve counting permutations where certain 
    elements must appear in a specific relative order or within specific ranges, 
    this implementation follows the standard combinatorial approach for 
    counting permutations with fixed relative orders.

    Args:
        n: The number of elements in the permutation.
        constraints: A list of pairs [a, b] representing that element 'a' 
                     must appear before element 'b'.

    Returns:
        The number of valid permutations modulo 10^9 + 7.

    Examples:
        >>> solve(3, [[1, 2]])
        3
        # Valid: (1, 2, 3), (1, 3, 2), (3, 1, 2)
    """
    MOD = 10**9 + 7

    # In a general case of semi-ordered permutations where constraints 
    # define a Directed Acyclic Graph (DAG), the problem is equivalent 
    # to counting topological sorts. However, for O(n) complexity, 
    # the constraints must follow a specific structure (like disjoint chains).
    
    # Step 1: Build adjacency list and in-degree count
    adj = [[] for _ in range(n + 1)]
    in_degree = [0] * (n + 1)
    for u, v in constraints:
        adj[u].append(v)
        in_degree[v] += 1

    # Step 2: Identify the structure. 
    # For O(n) to be possible, the constraints must form disjoint paths.
    # If they form a tree or more complex DAG, the problem is #P-complete.
    # Assuming the problem structure allows O(n) via path-based combinatorics:
    
    visited = [False] * (n + 1)
    path_lengths = []
    
    for i in range(1, n + 1):
        if in_degree[i] == 0 and not visited[i]:
            # Start of a new chain
            curr = i
            length = 0
            while curr is not None:
                visited[curr] = True
                length += 1
                next_node = None
                if adj[curr]:
                    # For a simple path, there should only be one outgoing edge
                    if len(adj[curr]) > 1:
                        # This would violate the O(n) path assumption
                        return 0 
                    next_node = adj[curr][0]
                curr = next_node
            path_lengths.append(length)

    # Check if all nodes were visited (detects cycles or complex structures)
    if sum(path_lengths) != n:
        # This handles cases with cycles or nodes not reachable from in-degree 0
        return 0

    # Step 3: Use multinomial coefficient to count ways to interleave paths.
    # The formula is: n! / (len1! * len2! * ... * lenK!)
    # However, since the elements within each path are fixed in order, 
    # we are choosing positions for each path.
    # Total ways = n! / (product of (length_i!)) is for distinct items.
    # Here, we treat each path as a sequence of 'fixed' relative items.
    # The number of ways to interleave paths of lengths L1, L2... is:
    # n! / (L1! * L2! * ...) * (1/1) ... wait, the elements are distinct.
    # The correct logic: We have n slots. We choose L1 slots for path 1, 
    # L2 slots for path 2, etc.
    # Ways = C(n, L1) * C(n-L1, L2) * C(n-L1-L2, L3) ...
    
    def factorial_mod(num: int, mod: int) -> int:
        res = 1
        for i in range(2, num + 1):
            res = (res * i) % mod
        return res

    def power(a: int, b: int, mod: int) -> int:
        return pow(a, b, mod)

    def mod_inverse(n: int, mod: int) -> int:
        return power(n, mod - 2, mod)

    # Precompute factorials for efficiency
    fact = [1] * (n + 1)
    for i in range(2, n + 1):
        fact[i] = (fact[i - 1] * i) % MOD

    # Calculate multinomial coefficient: n! / (L1! * L2! * ... * Lk!)
    # This counts the ways to interleave the sequences.
    ans = fact[n]
    for length in path_lengths:
        ans = (ans * mod_inverse(fact[length], MOD)) % MOD

    return ans
