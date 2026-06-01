METADATA = {
    "id": 1579,
    "name": "Remove Max Number of Edges to Keep Graph Fully Traversable",
    "slug": "remove-max-number-of-edges-to-keep-graph-fully-traversable",
    "category": "Graph",
    "aliases": [],
    "tags": ["union_find", "greedy", "graph"],
    "difficulty": "hard",
    "time_complexity": "O(E * α(N))",
    "space_complexity": "O(N)",
    "description": "Maximize the number of edges removed while ensuring both Alice and Bob can traverse all nodes in their respective graphs.",
}

class UnionFind:
    """Standard Disjoint Set Union (DSU) with path compression and union by rank."""
    
    def __init__(self, n: int):
        self.parent = list(range(n + 1))
        self.rank = [0] * (n + 1)
        self.num_components = n

    def find(self, i: int) -> int:
        if self.parent[i] == i:
            return i
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i: int, j: int) -> bool:
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
            self.num_components -= 1
            return True
        return False

def solve(n: int, edges: list[list[int]]) -> list[int]:
    """
    Finds the maximum number of edges that can be removed while keeping both 
    Alice's and Bob's graphs fully connected.

    Args:
        n: The number of nodes in the graph.
        edges: A list of edges where each edge is [type, u, v].
               Type 3: Both Alice and Bob.
               Type 1: Alice only.
               Type 2: Bob only.

    Returns:
        A list of three integers [removed_alice, removed_bob, removed_both].
        If it's impossible to make both graphs connected, returns [-1, -1, -1].

    Examples:
        >>> solve(4, [[3,1,2],[3,2,3],[1,1,3],[2,2,4]])
        [0, 0, 1]
        >>> solve(4, [[1,1,2],[2,2,3],[3,3,4]])
        [-1, -1, -1]
    """
    # DSU for Alice and Bob to track connectivity
    alice_dsu = UnionFind(n)
    bob_dsu = UnionFind(n)
    
    edges_used_alice = 0
    edges_used_bob = 0
    edges_used_both = 0
    
    # Step 1: Prioritize Type 3 edges (both Alice and Bob)
    # Using these edges is most efficient as one edge serves both users.
    for edge_type, u, v in edges:
        if edge_type == 3:
            # If this edge connects two previously unconnected components for either,
            # it is useful for both.
            if alice_dsu.union(u, v):
                bob_dsu.union(u, v)
                edges_used_both += 1
                edges_used_alice += 1
                edges_used_bob += 1

    # Step 2: Add Type 1 (Alice) and Type 2 (Bob) edges
    for edge_type, u, v in edges:
        if edge_type == 1:
            if alice_dsu.union(u, v):
                edges_used_alice += 1
        elif edge_type == 2:
            if bob_dsu.union(u, v):
                edges_used_bob += 1

    # Check if both Alice and Bob have a single connected component (all nodes connected)
    # num_components should be 1 (excluding the 0-th index if nodes are 1-indexed)
    # Since our UnionFind initializes with n components, we check if components == 1.
    if alice_dsu.num_components != 1 or bob_dsu.num_components != 1:
        return [-1, -1, -1]

    # Calculate removed edges: Total edges of type X - edges used of type X
    # We need to count total available edges per type first.
    total_type1 = sum(1 for e in edges if e[0] == 1)
    total_type2 = sum(1 for e in edges if e[0] == 2)
    total_type3 = sum(1 for e in edges if e[0] == 3)

    # Note: edges_used_alice includes edges_used_both.
    # To find removed_alice, we subtract the edges Alice actually used from her total pool.
    # Alice's pool = total_type1 + total_type3
    # Bob's pool = total_type2 + total_type3
    
    # However, the problem asks for removed_alice, removed_bob, removed_both.
    # removed_both = total_type3 - edges_used_both
    # removed_alice = total_type1 - (edges_used_alice - edges_used_both)
    # removed_bob = total_type2 - (edges_used_bob - edges_used_both)
    
    # Let's simplify:
    # Alice used: (edges_used_alice - edges_used_both) of Type 1 AND (edges_used_both) of Type 3.
    # Total Alice edges available: total_type1 + total_type3.
    # But the question asks for removed_alice specifically from the perspective of 
    # "how many Type 1 edges were removed".
    
    # Correct logic:
    # Alice's removed = total_type1 - (edges_used_alice - edges_used_both)
    # Bob's removed = total_type2 - (edges_used_bob - edges_used_both)
    # Both removed = total_type3 - edges_used_both
    
    # Wait, the problem defines:
    # Alice's removed: edges of type 1 not used.
    # Bob's removed: edges of type 2 not used.
    # Both removed: edges of type 3 not used.
    
    # Let's re-calculate based on the specific counts of edges used per type.
    # We need to track how many Type 1, Type 2, and Type 3 were actually used.
    
    # Re-running logic with explicit counters for clarity:
    alice_dsu = UnionFind(n)
    bob_dsu = UnionFind(n)
    used_t1 = 0
    used_t2 = 0
    used_t3 = 0
    
    # Pass 1: Type 3
    for edge_type, u, v in edges:
        if edge_type == 3:
            if alice_dsu.union(u, v):
                bob_dsu.union(u, v)
                used_t3 += 1
                
    # Pass 2: Type 1 and 2
    for edge_type, u, v in edges:
        if edge_type == 1:
            if alice_dsu.union(u, v):
                used_t1 += 1
        elif edge_type == 2:
            if bob_dsu.union(u, v):
                used_t2 += 1
                
    if alice_dsu.num_components != 1 or bob_dsu.num_components != 1:
        return [-1, -1, -1]
        
    total_t1 = sum(1 for e in edges if e[0] == 1)
    total_t2 = sum(1 for e in edges if e[0] == 2)
    total_t3 = sum(1 for e in edges if e[0] == 3)
    
    return [total_t1 - used_t1, total_t2 - used_t2, total_t3 - used_t3]

# The solve function above was redefined inside itself for clarity. 
# Let's provide the final clean version.

def solve_final(n: int, edges: list[list[int]]) -> list[int]:
    alice_dsu = UnionFind(n)
    bob_dsu = UnionFind(n)
    
    used_t1 = 0
    used_t2 = 0
    used_t3 = 0
    
    # 1. Use Type 3 edges first
    for edge_type, u, v in edges:
        if edge_type == 3:
            if alice_dsu.union(u, v):
                bob_dsu.union(u, v)
                used_t3 += 1
                
    # 2. Use Type 1 and Type 2 edges
    for edge_type, u, v in edges:
        if edge_type == 1:
            if alice_dsu.union(u, v):
                used_t1 += 1
        elif edge_type == 2:
            if bob_dsu.union(u, v):
                used_t2 += 1
                
    if alice_dsu.num_components != 1 or bob_dsu.num_components != 1:
        return [-1, -1, -1]
        
    total_t1 = 0
    total_t2 = 0
    total_t3 = 0
    for edge_type, u, v in edges:
        if edge_type == 1: total_t1 += 1
        elif edge_type == 2: total_t2 += 1
        elif edge_type == 3: total_t3 += 1
        
    return [total_t1 - used_t1, total_t2 - used_t2, total_t3 - used_t3]

# Replace the solve function with the correct implementation
solve = solve_final