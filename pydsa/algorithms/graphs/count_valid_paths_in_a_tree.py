METADATA = {
    "id": 2867,
    "name": "Count Valid Paths in a Tree",
    "slug": "count-valid-paths-in-a-tree",
    "category": "Trees",
    "aliases": [],
    "tags": ["trees", "dfs", "combinatorics", "dynamic programming"],
    "difficulty": "hard",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Count the number of paths in a tree where the sum of node values is a multiple of k.",
}

def solve(n: int, k: int, edges: list[list[int]], values: list[int]) -> int:
    """
    Counts the number of paths in a tree where the sum of node values is divisible by k.

    Args:
        n: The number of nodes in the tree.
        k: The divisor.
        edges: A list of undirected edges [u, v].
        values: A list of node values.

    Returns:
        The total number of valid paths.

    Examples:
        >>> solve(3, 3, [[0, 1], [1, 2]], [1, 2, 3])
        3
        # Paths: [1, 2] sum=3, [3] sum=3, [1, 2, 3] sum=6
    """
    MOD = 10**9 + 7
    adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    total_valid_paths = 0

    def dfs(u: int, p: int) -> dict[int, int]:
        """
        Performs DFS to count paths ending at node u with specific remainders.
        
        Args:
            u: Current node index.
            p: Parent node index.
            
        Returns:
            A dictionary mapping (sum % k) to the count of paths starting from 
            u and going down into its subtree.
        """
        nonlocal total_valid_paths
        
        # current_node_rem is the remainder of the current node's value
        current_node_rem = values[u] % k
        
        # counts[r] stores number of paths starting at u and going down with sum % k == r
        counts: dict[int, int] = {current_node_rem: 1}
        
        # If the node itself is a valid path
        if current_node_rem == 0:
            total_valid_paths = (total_valid_paths + 1) % MOD

        for v in adj[u]:
            if v == p:
                continue
            
            subtree_counts = dfs(v, u)
            
            # For every path in the subtree, try to combine it with paths already found in u
            # A path from subtree (sum_v) and a path from existing u (sum_u)
            # combined path sum = sum_v + sum_u - values[u] (since u is counted in both)
            # However, the DFS returns paths starting AT v. 
            # So a path from subtree is (v_path_sum). 
            # The combined path is (u_path_sum + v_path_sum).
            # We need (u_path_sum + v_path_sum) % k == 0.
            
            for rem_v, count_v in subtree_counts.items():
                # The path from v extended to u has remainder: (rem_v + current_node_rem) % k
                # But wait, the subtree_counts already represent paths starting at v.
                # Let's redefine: subtree_counts[r] is count of paths starting at v with sum % k == r.
                # The path from u through v has remainder: (r + values[u]) % k.
                
                # To avoid double counting and simplify:
                # We match paths from the current subtree with paths from previously visited subtrees.
                # A path from subtree v (rem_v) + a path from previous subtrees (rem_u)
                # must satisfy (rem_v + rem_u) % k == 0.
                # Note: rem_u and rem_v already include values[u] if we define them as paths starting at u.
                # Let's use the logic: path_v is a path starting at v. 
                # Path_u is a path starting at u.
                # Combined path: path_u + path_v.
                # Since path_u includes values[u], and path_v does NOT include values[u],
                # the sum is (rem_u + rem_v).
                
                # Let's adjust: subtree_counts[r] = paths starting at v with sum % k == r.
                # Path from u through v: (r + values[u]) % k.
                
                # To find valid paths passing through u:
                # We need (rem_u + rem_v) % k == 0, where rem_u is a path starting at u
                # and rem_v is a path starting at v.
                # Note: rem_u already includes values[u].
                
                # Target rem_v such that (rem_u + rem_v) % k == 0
                # rem_v = (k - rem_u) % k
                # But we are iterating over rem_v.
                # For a fixed rem_v, we need rem_u = (k - rem_v) % k.
                # Wait, the path from v is extended to u. 
                # Let's say path_v has sum S_v. Path_u has sum S_u.
                # Combined path sum = S_u + S_v.
                # We need (S_u + S_v) % k == 0.
                
                # Let's use the counts of paths starting at u (including u)
                # and paths starting at v (not including u).
                
                # Correct logic:
                # 1. subtree_counts[rem_v] is count of paths starting at v with sum % k == rem_v.
                # 2. We want to combine a path from subtree v with a path from previous subtrees of u.
                # 3. A path from subtree v extended to u has remainder: (rem_v + values[u]) % k.
                # 4. Let's call this extended remainder 'rem_ext'.
                # 5. We need (rem_ext + rem_prev_u_without_u) % k == 0? No.
                
                # Let's simplify:
                # counts[r] = number of paths starting at u with sum % k == r.
                # subtree_counts[r] = number of paths starting at v with sum % k == r.
                # A path starting at v extended to u has remainder: (r + values[u]) % k.
                # Let's call this 'new_rem'.
                # We want to combine 'new_rem' with an existing path in 'counts' that starts at u.
                # But 'counts' already includes values[u].
                # If we combine a path from 'counts' (sum S_u) and a path from 'subtree_counts' (sum S_v),
                # the total sum is S_u + S_v.
                # We need (S_u + S_v) % k == 0.
                # Since S_u includes values[u], and S_v does not, this is correct.
                
                # Wait, the current 'counts' contains paths starting at u.
                # The 'subtree_counts' contains paths starting at v.
                # A path from v extended to u has sum: S_v + values[u].
                # Let's call this 'path_v_to_u'.
                # We want to combine 'path_v_to_u' with a path from 'counts' that *doesn't* include values[u]?
                # No, that's not right.
                
                # Let's use this:
                # counts[r] = number of paths starting at u with sum % k == r.
                # subtree_counts[r] = number of paths starting at v with sum % k == r.
                # For each path in subtree_counts with remainder 'r', 
                # the path extended to u has remainder (r + values[u]) % k.
                # Let's call this 'rem_v_ext'.
                # We want to find a path in 'counts' (which already includes values[u])
                # such that (rem_v_ext + rem_u_existing_without_u) % k == 0.
                # This is getting confusing. Let's use the standard approach:
                # Total paths = paths entirely in subtrees + paths passing through u.
                # Paths passing through u:
                # For each child v:
                #   For each rem_v in subtree_counts:
                #     rem_v_ext = (rem_v + values[u]) % k
                #     We need (rem_v_ext + rem_u_prev_without_u) % k == 0.
                # This is still messy.
                
                # Let's use:
                # counts[r] is the number of paths starting at u with sum % k == r.
                # When processing child v:
                #   For each rem_v, count_v in subtree_counts:
                #     rem_v_ext = (rem_v + values[u]) % k
                #     We need (rem_v_ext + rem_u_prev_without_u) % k == 0.
                #     Wait, if rem_u_prev is a path starting at u, it ALREADY includes values[u].
                #     If we add rem_v_ext, we are adding values[u] twice.
                
                # Let's try again:
                # counts[r] = number of paths starting at u with sum % k == r.
                # For child v:
                #   For each rem_v, count_v in subtree_counts:
                #     rem_v_ext = (rem_v + values[u]) % k
                #     We need (rem_v_ext + rem_u_prev_without_u) % k == 0.
                #     Actually, if we want to combine a path from v (sum S_v) 
                #     with a path from a previous child (sum S_prev_u),
                #     the total sum is S_v + S_prev_u.
                #     S_prev_u already includes values[u].
                #     So we need (rem_v + rem_prev_u) % k == 0.
                #     Wait, S_v does NOT include values[u].
                #     So (rem_v + rem_prev_u) % k == 0 is correct!
                
                # Let's re-verify:
                # Path 1: u -> ... -> node_in_prev_subtree (Sum = S_prev_u)
                # Path 2: v -> ... -> node_in_v_subtree (Sum = S_v)
                # Combined: node_in_prev_subtree -> ... -> u -> v -> ... -> node_in_v_subtree
                # Total Sum = S_prev_u + S_v.
                # We need (S_prev_u + S_v) % k == 0.
                
                # 1. For each rem_v, count_v in subtree_counts:
                #    Target rem_u = (k - rem_v) % k
                #    total_valid_paths += count_v * counts[rem_u]
                # 2. After checking all rem_v, update counts:
                #    For each rem_v, count_v in subtree_counts:
                #    rem_v_ext = (rem_v + values[u]) % k
                #    counts[rem_v_ext] += count_v
                
                pass # logic implemented below

            # Corrected loop logic:
            for rem_v, count_v in subtree_counts.items():
                # Target rem_u such that (rem_v + rem_u) % k == 0
                target_rem_u = (k - rem_v) % k
                if target_rem_u in counts:
                    total_valid_paths = (total_valid_paths + count_v * counts[target_rem_u]) % MOD
            
            # Update counts with paths from this subtree extended to u
            for rem_v, count_v in subtree_counts.items():
                rem_v_ext = (rem_v + values[u]) % k
                counts[rem_v_ext] = counts.get(rem_v_ext, 0) + count_v
                
        return counts

    dfs(0, -1)
    return total_valid_paths

# The above logic in the loop was slightly flawed in the draft. 
# Let's rewrite the solve function cleanly.

def solve_final(n: int, k: int, edges: list[list[int]], values: list[int]) -> int:
    """
    Correct implementation of the path counting algorithm.
    """
    MOD = 10**9 + 7
    adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    total_valid_paths = 0

    def dfs(u: int, p: int) -> dict[int, int]:
        nonlocal total_valid_paths
        
        u_val_rem = values[u] % k
        # counts[r] stores number of paths starting at u with sum % k == r
        counts: dict[int, int] = {u_val_rem: 1}
        
        # If the single node u is a valid path
        if u_val_rem == 0:
            total_valid_paths = (total_valid_paths + 1) % MOD

        for v in adj[u]:
            if v == p:
                continue
            
            subtree_counts = dfs(v, u)
            
            # 1. Combine paths from current subtree with paths from previous subtrees
            # A path from subtree v has sum S_v.
            # A path from previous subtrees (starting at u) has sum S_u.
            # Combined path sum = S_v + S_u.
            # We need (S_v + S_u) % k == 0.
            for rem_v, count_v in subtree_counts.items():
                target_rem_u = (k - rem_v) % k
                if target_rem_u in counts:
                    total_valid_paths = (total_valid_paths + count_v * counts[target_rem_u]) % MOD
            
            # 2. Extend paths from subtree v to include u and add to counts
            for rem_v, count_v in subtree_counts.items():
                rem_v_ext = (rem_v + u_val_rem) % k
                counts[rem_v_ext] = counts.get(rem_v_ext, 0) + count_v
                
        return counts

    dfs(0, -1)
    return total_valid_paths

# Re-assigning to solve for the final structure
solve = solve_final
