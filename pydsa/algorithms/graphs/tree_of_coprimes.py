METADATA = {
    "id": 1766,
    "name": "Tree of Coprimes",
    "slug": "tree_of_coprimes",
    "category": "Graph",
    "aliases": [],
    "tags": ["greedy", "graph", "math", "disjoint set union"],
    "difficulty": "hard",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Find the minimum number of edges to add to a graph of n nodes such that the resulting graph is a tree and every connected pair of nodes is coprime.",
}

import math

class DisjointSetUnion:
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

def solve(n: int, edges: list[list[int]]) -> int:
    """
    Calculates the minimum number of edges to add to make the graph a tree 
    where all connected nodes are coprime.

    Args:
        n: The number of nodes in the graph.
        edges: A list of existing edges [u, v].

    Returns:
        The minimum number of edges to add. Returns -1 if impossible.

    Examples:
        >>> solve(5, [[1, 2], [2, 3]])
        2
        >>> solve(4, [[1, 2], [1, 3], [1, 4]])
        0
    """
    dsu = DisjointSetUnion(n)
    
    # First, process existing edges. If any existing edge is not coprime, 
    # it's impossible to satisfy the condition.
    for u, v in edges:
        if math.gcd(u, v) != 1:
            return -1
        dsu.union(u, v)

    # To minimize edges added, we want to maximize the number of connections 
    # made between existing components. We use a greedy approach:
    # Try connecting nodes with the largest values first, as they are 
    # more likely to be coprime with many other numbers.
    # However, a more robust greedy approach is to iterate through all 
    # possible pairs (u, v) in descending order of their values or 
    # simply check all pairs. Since n is up to 1000, O(n^2) is acceptable.
    
    # We iterate through pairs (i, j) where i > j.
    # To maximize connectivity, we prioritize larger values.
    # Actually, the problem asks for a tree. A tree with n nodes always has n-1 edges.
    # We need to reach 1 component.
    
    # Optimization: Pre-calculate coprimality or just use math.gcd.
    # We iterate through all pairs to find potential edges to merge components.
    for i in range(n, 0, -1):
        for j in range(i - 1, 0, -1):
            if dsu.find(i) != dsu.find(j):
                if math.gcd(i, j) == 1:
                    dsu.union(i, j)
        
        # If we already reached 1 component, we can stop early.
        if dsu.num_components == 1:
            break

    # If we cannot connect all nodes into one component, return -1.
    if dsu.num_components > 1:
        return -1

    # The number of edges to add is (number of components before adding new edges) - 1.
    # But we already merged components in the loop. 
    # The logic above is slightly flawed for "minimum edges to add".
    # Let's refine: The number of edges to add is (initial_components - 1).
    # But we must ensure the edges we add are coprime.
    
    # Correct logic:
    # 1. Start with DSU containing existing edges.
    # 2. Count initial components.
    # 3. Try to merge components using coprime pairs.
    # 4. If components > 1 at the end, return -1.
    # 5. Otherwise, the answer is (initial_components - 1).
    
    # Let's re-implement the logic cleanly.
    return _solve_refined(n, edges)

def _solve_refined(n: int, edges: list[list[int]]) -> int:
    dsu = DisjointSetUnion(n)
    for u, v in edges:
        if math.gcd(u, v) != 1:
            return -1
        dsu.union(u, v)
    
    initial_components = dsu.num_components
    
    # Try to merge components using coprime pairs
    # We iterate through all pairs to see if they can bridge components
    for i in range(n, 0, -1):
        for j in range(i - 1, 0, -1):
            if dsu.find(i) != dsu.find(j):
                if math.gcd(i, j) == 1:
                    dsu.union(i, j)
                    
    if dsu.num_components == 1:
        # The number of edges we added is (initial_components - 1)
        return initial_components - 1
    else:
        return -1
