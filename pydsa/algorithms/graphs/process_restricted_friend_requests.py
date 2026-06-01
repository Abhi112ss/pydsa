METADATA = {
    "id": 2076,
    "name": "Process Restricted Friend Requests",
    "slug": "process-restricted-friend-requests",
    "category": "Union Find",
    "aliases": [],
    "tags": ["union_find", "graphs", "disjoint set union"],
    "difficulty": "hard",
    "time_complexity": "O(n * alpha(n))",
    "space_complexity": "O(n)",
    "description": "Process friend requests while ensuring no path exists between restricted pairs in the friendship graph.",
}

class UnionFind:
    """Standard Disjoint Set Union (DSU) with path compression and union by rank."""
    
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, i: int) -> int:
        if self.parent[i] == i:
            return i
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i: int, j: int) -> None:
        root_i = self.find(i)
        root_j = self.find(j)
        if root_i != root_j:
            if self.rank[root_i] < self.rank[root_j]:
                self.parent[root_i] = root_j
            elif self.rank[root_i] > self.rank[root_j]:
                self.parent[root_j] = root_i
            else:
                self.parent[root_i] = root_j
                self.rank[root_j] += 1

def solve(n: int, restricted: list[list[int]], friend_requests: list[list[int]]) -> list[bool]:
    """
    Processes friend requests while respecting restrictions.
    
    A request is rejected if it would create a path between any restricted pair.
    
    Args:
        n: The number of users.
        restricted: A list of pairs [u, v] that cannot be in the same connected component.
        friend_requests: A list of pairs [u, v] representing requested friendships.
        
    Returns:
        A list of booleans where True indicates the request was accepted and False rejected.
        
    Examples:
        >>> solve(4, [[0, 3]], [[0, 1], [1, 2], [2, 3]])
        [True, True, False]
    """
    # Use a set for O(1) lookup of restricted pairs. 
    # We store both (u, v) and (v, u) to simplify checking.
    restricted_set = set()
    for u, v in restricted:
        restricted_set.add((u, v))
        restricted_set.add((v, u))

    # adjacency_list tracks current connections to perform BFS/DFS checks
    # However, the core constraint is about connectivity in the DSU.
    # To check if adding (u, v) violates a restriction, we check if any 
    # restricted pair (r1, r2) would end up in the same component.
    
    # Optimization: Instead of checking all restricted pairs, we only care 
    # if the new connection merges two components that contain elements 
    # of a restricted pair.
    
    # Actually, the most efficient way to check if adding (u, v) is valid:
    # For every restricted pair (r1, r2), if r1 is in the same component as u 
    # OR v, and r2 is in the same component as the other, it's a violation.
    # But that's too slow.
    
    # Correct approach: A request (u, v) is invalid if there exists a restricted 
    # pair (r1, r2) such that r1 is connected to u (or v) AND r2 is connected to v (or u).
    # We can pre-calculate which restricted nodes are in which component.
    
    dsu = UnionFind(n)
    results = []
    
    # To optimize the check: for each component, we track which restricted nodes it contains.
    # But since restricted nodes are fixed, we can just check:
    # For a request (u, v), if we merge component(u) and component(v), 
    # does any restricted pair (r1, r2) have r1 in component(u) and r2 in component(v)?
    
    # Let's maintain a mapping: component_root -> set of restricted nodes in it.
    # This is still potentially slow. 
    
    # Alternative: For each restricted pair (r1, r2), if we add (u, v), 
    # we check if find(r1) == find(u) and find(r2) == find(v) (or vice versa).
    # This is still O(len(restricted)).
    
    # Let's refine: A request (u, v) is invalid if there is a restricted pair (r1, r2)
    # such that find(r1) == find(u) and find(r2) == find(v) (or vice versa).
    # To do this efficiently, we can pre-group restricted nodes by their component.
    # But components change.
    
    # Let's use the property: (u, v) is invalid if there exists (r1, r2) in restricted
    # such that (find(r1) == find(u) and find(r2) == find(v)) OR (find(r1) == find(v) and find(r2) == find(u)).
    
    # We can optimize this by iterating through the restricted list.
    # Since len(restricted) is up to 10^5 and len(requests) is up to 10^5, 
    # O(R * Q) is too slow.
    
    # Wait, the constraint is: adding (u, v) creates a path.
    # This means r1 and r2 become connected.
    # This happens if find(r1) == find(u) and find(r2) == find(v) (or vice versa).
    
    # Let's maintain for each component root, a set of restricted nodes in it.
    # component_to_restricted[root] = {r_idx1, r_idx2, ...}
    # When merging components, we merge these sets.
    
    component_to_restricted = [set() for _ in range(n)]
    for i, (r1, r2) in enumerate(restricted):
        component_to_restricted[r1].add(i)
        component_to_restricted[r2].add(i)

    # Actually, the simplest way:
    # For each component root, store which restricted pairs it "partially" satisfies.
    # A restricted pair i=(r1, r2) is "partially satisfied" by root if find(r1)==root or find(r2)==root.
    # This is still complex.
    
    # Let's use the "restricted nodes in component" idea.
    # For each component root, store a set of restricted nodes.
    # When checking (u, v):
    #   root_u = find(u), root_v = find(v)
    #   For each r1 in component_to_restricted[root_u]:
    #     Find its partner r2. If find(r2) == root_v, then REJECT.
    
    # To make this fast, we need to know the partner of r1.
    # partner[r1] = r2
    
    partner = {}
    for r1, r2 in restricted:
        partner[r1] = r2
        partner[r2] = r1
        
    # component_to_restricted[root] stores the set of restricted nodes in that component.
    comp_restricted_nodes = [set() for _ in range(n)]
    for r1, r2 in restricted:
        comp_restricted_nodes[r1].add(r1)
        comp_restricted_nodes[r2].add(r2)
        # Note: we only add the node itself to the set.
        # If a component contains both r1 and r2, it's already invalid (but problem says 
        # we start with no restrictions violated).

    # Wait, the logic is: (u, v) is invalid if there is some (r1, r2) in restricted
    # such that r1 is in component(u) and r2 is in component(v).
    
    # Let's track for each component root, the set of restricted nodes it contains.
    # When checking (u, v):
    #   root_u = find(u), root_v = find(v)
    #   If root_u == root_v, it's already connected, so it can't violate a NEW restriction.
    #   Otherwise, check if any r1 in comp_restricted_nodes[root_u] has its partner r2 in comp_restricted_nodes[root_v].
    
    # To make the check O(min(size_u, size_v)), we use the "smaller to larger" merging.
    # But the check must be done BEFORE merging.
    
    # Let's refine the check:
    # For each r1 in comp_restricted_nodes[root_u]:
    #    if partner[r1] in comp_restricted_nodes[root_v]: return False
    
    # To ensure this is fast, we always iterate over the smaller set.
    
    # Re-initialize comp_restricted_nodes correctly:
    comp_restricted_nodes = [set() for _ in range(n)]
    for r1, r2 in restricted:
        comp_restricted_nodes[r1].add(r1)
        comp_restricted_nodes[r2].add(r2)

    # We need to handle the case where a node is part of multiple restricted pairs.
    # The partner dictionary needs to be a list of partners for each node.
    node_to_partners = [[] for _ in range(n)]
    for r1, r2 in restricted:
        node_to_partners[r1].append(r2)
        node_to_partners[r2].append(r1)

    for u, v in friend_requests:
        root_u = dsu.find(u)
        root_v = dsu.find(v)
        
        if root_u == root_v:
            results.append(True)
            continue
            
        # Check if merging root_u and root_v violates any restriction
        is_valid = True
        # Optimization: iterate over the smaller set of restricted nodes
        if len(comp_restricted_nodes[root_u]) > len(comp_restricted_nodes[root_v]):
            root_u, root_v = root_v, root_u
            
        # Now root_u is the one with fewer restricted nodes
        for r_node in comp_restricted_nodes[root_u]:
            for p in node_to_partners[r_node]:
                if p in comp_restricted_nodes[root_v]:
                    is_valid = False
                    break
            if not is_valid:
                break
        
        if is_valid:
            results.append(True)
            # Perform union and merge the restricted node sets
            dsu.union(root_u, root_v)
            # The new root might be root_u or root_v depending on rank.
            # We must find the actual new root.
            new_root = dsu.find(root_u)
            # We need to merge the sets into the new_root.
            # Since we don't know which one is the new root, let's be careful.
            # Let's use a more robust union that returns the new root.
            
            # Re-implementing union to return the new root for set merging
            def union_and_get_root(root1, root2):
                if root1 == root2: return root1
                if dsu.rank[root1] < dsu.rank[root2]:
                    dsu.parent[root1] = root2
                    return root2
                elif dsu.rank[root1] > dsu.rank[root2]:
                    dsu.parent[root2] = root1
                    return root1
                else:
                    dsu.parent[root1] = root2
                    dsu.rank[root2] += 1
                    return root2
            
            # Wait, the standard union above is fine, we just need to find the new root.
            # Let's just re-calculate it.
            actual_root_u = dsu.find(root_u)
            actual_root_v = dsu.find(root_v)
            # This is slightly redundant but safe.
            # Actually, the union above already changed the parent.
            # Let's just find which one is the parent now.
            
            # Correct way to merge sets:
            # We need to know which root was merged into which.
            # Let's rewrite the union logic inside the loop.
            pass # logic handled below
        else:
            results.append(False)

    # Let's rewrite the loop properly to avoid confusion.
    return _optimized_solve(n, restricted, friend_requests)

def _optimized_solve(n: int, restricted: list[list[int]], friend_requests: list[list[int]]) -> list[bool]:
    dsu = UnionFind(n)
    node_to_partners = [[] for _ in range(n)]
    for r1, r2 in restricted:
        node_to_partners[r1].append(r2)
        node_to_partners[r2].append(r1)
        
    comp_restricted_nodes = [set() for _ in range(n)]
    for r1, r2 in restricted:
        comp_restricted_nodes[r1].add(r1)
        comp_restricted_nodes[r2].add(r2)
        
    results = []
    for u, v in friend_requests:
        root_u = dsu.find(u)
        root_v = dsu.find(v)
        
        if root_u == root_v:
            results.append(True)
            continue
            
        is_valid = True
        # Check if any restricted node in root_u has a partner in root_v
        if len(comp_restricted_nodes[root_u]) > len(comp_restricted_nodes[root_v]):
            root_u, root_v = root_v, root_u
            
        for r_node in comp_restricted_nodes[root_u]:
            for p in node_to_partners[r_node]:
                if p in comp_restricted_nodes[root_v]:
                    is_valid = False
                    break
            if not is_valid:
                break
        
        if is_valid:
            results.append(True)
            # Union by rank and merge sets
            if dsu.rank[root_u] < dsu.rank[root_v]:
                dsu.parent[root_u] = root_v
                comp_restricted_nodes[root_v].update(comp_restricted_nodes[root_u])
                comp_restricted_nodes[root_u] = set() # Clear to save memory
            elif dsu.rank[root_u] > dsu.rank[root_v]:
                dsu.parent[root_v] = root_u
                comp_restricted_nodes[root_u].update(comp_restricted_nodes[root_v])
                comp_restricted_nodes[root_v] = set()
            else:
                dsu.parent[root_u] = root_v
                dsu.rank[root_v] += 1
                comp_restricted_nodes[root_v].update(comp_restricted_nodes[root_u])
                comp_restricted_nodes[root_u] = set()
        else:
            results.append(False)
            
    return results

# The solve function is actually the wrapper for the optimized logic.
# Let's clean up the final structure.

def solve_final(n: int, restricted: list[list[int]], friend_requests: list[list[int]]) -> list[bool]:
    """
    Processes friend requests while respecting restrictions.
    """
    return _optimized_solve(n, restricted, friend_requests)

# Re-assigning for the required interface
solve = solve_final