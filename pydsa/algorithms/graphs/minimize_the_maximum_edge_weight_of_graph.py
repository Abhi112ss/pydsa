METADATA = {
    "id": 3419,
    "name": "Minimize the Maximum Edge Weight of Graph",
    "slug": "minimize-the-maximum-edge-weight-of-graph",
    "category": "Graph",
    "aliases": [],
    "tags": ["binary_search", "disjoint_set_union", "graphs"],
    "difficulty": "medium",
    "time_complexity": "O(E log E)",
    "space_complexity": "O(V)",
    "description": "Find the minimum possible value of the maximum edge weight such that all nodes in the graph are connected.",
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

def solve(n: int, edges: list[list[int]]) -> int:
    """
    Finds the minimum maximum edge weight required to connect all nodes.

    Args:
        n: The number of nodes in the graph (labeled 0 to n-1).
        edges: A list of edges where edges[i] = [u, v, weight].

    Returns:
        The minimum maximum edge weight required to make the graph connected. 
        Returns -1 if it is impossible to connect all nodes.

    Examples:
        >>> solve(3, [[0, 1, 1], [1, 2, 2], [0, 2, 3]])
        2
        >>> solve(4, [[0, 1, 10], [2, 3, 5]])
        -1
    """
    # Sort edges by weight to facilitate Kruskal's-like approach or binary search
    # Sorting allows us to efficiently check connectivity for a given weight threshold
    sorted_edges = sorted(edges, key=lambda x: x[2])
    
    # First, check if the graph can even be connected using all edges
    dsu_check = DisjointSetUnion(n)
    for u, v, w in sorted_edges:
        dsu_check.union(u, v)
    
    if dsu_check.num_components > 1:
        return -1

    # Binary search on the index of the sorted edges
    # The answer will be the weight of the edge at some index in the sorted list
    low = 0
    high = len(sorted_edges) - 1
    ans = -1

    while low <= high:
        mid = (low + high) // 2
        threshold_weight = sorted_edges[mid][2]
        
        # Check if the graph is connected using only edges with weight <= threshold_weight
        dsu = DisjointSetUnion(n)
        for u, v, w in sorted_edges:
            if w <= threshold_weight:
                dsu.union(u, v)
            else:
                # Since edges are sorted, we can break early
                break
        
        if dsu.num_components == 1:
            # If connected, try a smaller maximum weight
            ans = threshold_weight
            high = mid - 1
        else:
            # If not connected, we need larger weights
            low = mid + 1

    return ans
