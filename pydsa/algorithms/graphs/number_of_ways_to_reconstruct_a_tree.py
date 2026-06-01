METADATA = {
    "id": 1719,
    "name": "Number Of Ways To Reconstruct A Tree",
    "slug": "number-of-ways-to-reconstruct-a-tree",
    "category": "Backtracking",
    "aliases": [],
    "tags": ["backtracking", "graphs", "degree"],
    "difficulty": "hard",
    "time_complexity": "O(2^n)",
    "space_complexity": "O(n)",
    "description": "Find the number of ways to reconstruct a tree such that the degree sequence of the reconstructed tree matches the given degree sequence.",
}

def solve(degree: list[int]) -> int:
    """
    Args:
        degree: A list of integers representing the required degree of each node.

    Returns:
        The number of ways to reconstruct the tree.
    """
    n = len(degree)
    if n == 1:
        return 1 if degree[0] == 0 else 0

    adj = [set() for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            if degree[i] > 0 and degree[j] > 0:
                adj[i].add(j)
                adj[j].add(i)

    def backtrack(remaining_degrees: list[int], current_adj: list[set[int]]) -> int:
        if not remaining_degrees:
            return 1

        max_deg = -1
        candidates = []
        for i in range(n):
            if remaining_degrees[i] > max_deg:
                max_deg = remaining_degrees[i]
                candidates = [i]
            elif remaining_degrees[i] == max_deg and max_deg > 0:
                candidates.append(i)

        if max_deg <= 0:
            return 1

        ways = 0
        for u in candidates:
            possible_neighbors = []
            for v in range(n):
                if u != v and remaining_degrees[v] > 0 and v in current_adj[u]:
                    possible_neighbors.append(v)

            if len(possible_neighbors) < max_deg:
                continue

            import itertools
            for neighbors in itertools.combinations(possible_neighbors, max_deg):
                valid = True
                for v in neighbors:
                    if remaining_degrees[v] == 0:
                        valid = False
                        break
                
                if not valid:
                    continue

                for v in neighbors:
                    remaining_degrees[u] -= 1
                    remaining_degrees[v] -= 1
                    current_adj[u].remove(v)
                    current_adj[v].remove(u)

                ways += backtrack(remaining_degrees, current_adj)

                for v in neighbors:
                    current_adj[u].add(v)
                    current_adj[v].add(u)
                    remaining_degrees[v] += 1
                    remaining_degrees[u] += 1
        
        return ways

    # The backtracking approach above is conceptually correct but needs careful 
    # implementation of the state to avoid redundant work and handle the 
    # specific constraints of the problem.
    
    # Re-implementing with a more efficient state management
    
    def solve_recursive(current_degrees: list[int], current_adj: list[set[int]]) -> int:
        max_val = max(current_degrees)
        if max_val == 0:
            return 1
        
        target_nodes = [i for i, d in enumerate(current_degrees) if d == max_val]
        
        total_ways = 0
        for u in target_nodes:
            neighbors = [v for v in current_adj[u] if current_degrees[v] > 0]
            if len(neighbors) < max_val:
                continue
            
            import itertools
            for combo in itertools.combinations(neighbors, max_val):
                # Check if this combination is valid (all neighbors must have degree > 0)
                # and we must ensure we don't pick a neighbor that would become degree 0 
                # unless it's the last connection needed.
                
                # To avoid overcounting, we only process the first node in target_nodes
                # that can satisfy the condition.
                
                # Actually, the standard way to solve this is to pick the FIRST node 
                # that has the maximum degree and try all combinations of its neighbors.
                pass

        return 0

    # Corrected logic:
    def backtrack_optimized(curr_deg: list[int], curr_adj: list[set[int]]) -> int:
        max_d = 0
        u = -1
        for i in range(n):
            if curr_deg[i] > max_d:
                max_d = curr_deg[i]
                u = i
        
        if max_d == 0:
            return 1
        
        # Find all nodes with max_d
        candidates = [i for i in range(n) if curr_deg[i] == max_d]
        
        # We only need to pick ONE node with max_d to branch on
        u = candidates[0]
        
        # Potential neighbors for u
        potential = [v for v in curr_adj[u] if curr_deg[v] > 0]
        
        if len(potential) < max_d:
            return 0
        
        import itertools
        res = 0
        for combo in itertools.combinations(potential, max_d):
            # Check if any neighbor in combo has degree 1 and is not the only neighbor
            # This is a heuristic to prune, but the core is the degree reduction
            
            # Apply
            for v in combo:
                curr_deg[u] -= 1
                curr_deg[v] -= 1
                curr_adj[u].remove(v)
                curr_adj[v].remove(u)
            
            res += backtrack_optimized(curr_deg, curr_adj)
            
            # Backtrack
            for v in combo:
                curr_adj[u].add(v)
                curr_adj[v].add(u)
                curr_deg[v] += 1
                curr_deg[u] += 1
        return res

    # The problem requires finding the number of ways. 
    # The logic above is slightly flawed due to the "pick one node" rule.
    # If multiple nodes have max_d, picking any one of them and trying all 
    # combinations of its neighbors will cover all valid trees.
    
    # Let's use a cleaner version.
    
    def solve_final(d: list[int], adj: list[set[int]]) -> int:
        max_d = max(d)
        if max_d == 0:
            return 1
        
        u = -1
        for i in range(n):
            if d[i] == max_d:
                u = i
                break
        
        neighbors = [v for v in adj[u] if d[v] > 0]
        if len(neighbors) < max_d:
            return 0
        
        import itertools
        count = 0
        for combo in itertools.combinations(neighbors, max_d):
            # Check if any neighbor in combo has degree 1 and is not the only neighbor
            # This is actually handled by the recursion.
            
            for v in combo:
                d[u] -= 1
                d[v] -= 1
                adj[u].remove(v)
                adj[v].remove(u)
            
            count += solve_final(d, adj)
            
            for v in combo:
                adj[u].add(v)
                adj[v].add(u)
                d[v] += 1
                d[u] += 1
        return count

    # Re-initialize for the final call
    adj_list = [set() for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            if degree[i] > 0 and degree[j] > 0:
                adj_list[i].add(j)
                adj_list[j].add(i)
                
    return solve_final(list(degree), adj_list)