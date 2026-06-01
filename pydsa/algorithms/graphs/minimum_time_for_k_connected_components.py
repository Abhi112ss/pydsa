METADATA = {
    "id": 3608,
    "name": "Minimum Time for K Connected Components",
    "slug": "minimum-time-for-k-connected-components",
    "category": "Greedy",
    "aliases": [],
    "tags": ["disjoint_set", "greedy", "graph"],
    "difficulty": "medium",
    "time_complexity": "O(E log E)",
    "space_complexity": "O(V)",
    "description": "Find the minimum time required to reduce the number of connected components to at most K using edges sorted by time.",
}

class DisjointSetUnion:
    """A standard Disjoint Set Union (DSU) implementation with path compression and union by rank."""
    
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.rank = [0] * n
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

def solve(n: int, k: int, edges: list[list[int]]) -> int:
    """
    Finds the minimum time such that the number of connected components is at most K.
    
    Args:
        n: The number of nodes in the graph (labeled 0 to n-1).
        k: The target number of connected components.
        edges: A list of edges where edges[i] = [u, v, time].

    Returns:
        The minimum time required to reach at most K components. 
        Returns 0 if the initial number of components is already <= K.
        Returns -1 if it is impossible to reach K components even with all edges.

    Examples:
        >>> solve(4, 2, [[0, 1, 1], [1, 2, 5], [2, 3, 10]])
        5
        >>> solve(4, 4, [[0, 1, 1]])
        0
        >>> solve(4, 1, [[0, 1, 1]])
        -1
    """
    # If we already have k or fewer components (each node is its own component initially)
    if n <= k:
        return 0

    # Sort edges by time to apply a greedy approach (Kruskal-like)
    # We want to use the smallest time edges first to reduce components
    sorted_edges = sorted(edges, key=lambda x: x[2])
    
    dsu = DisjointSetUnion(n)
    max_time_used = 0

    for u, v, time in sorted_edges:
        # If union is successful, it means we merged two previously separate components
        if dsu.union(u, v):
            max_time_used = time
            
            # Check if we have reached the target number of components
            if dsu.num_components <= k:
                return max_time_used

    # If we exhausted all edges and still have more than k components
    return -1 if dsu.num_components > k else max_time_used
