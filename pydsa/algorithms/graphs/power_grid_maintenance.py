METADATA = {
    "id": 3607,
    "name": "Power Grid Maintenance",
    "slug": "power_grid_maintenance",
    "category": "Graph",
    "aliases": [],
    "tags": ["kruskal", "prim", "disjoint_set", "mst"],
    "difficulty": "medium",
    "time_complexity": "O(E log E)",
    "space_complexity": "O(V + E)",
    "description": "Find the minimum cost to connect all power stations in a grid using a Minimum Spanning Tree algorithm.",
}

class DisjointSetUnion:
    """A standard Disjoint Set Union (DSU) with path compression and union by rank."""

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
    Calculates the minimum cost to connect all n power stations using Kruskal's algorithm.

    Args:
        n: The number of power stations (nodes).
        edges: A list of edges where each edge is [u, v, cost].

    Returns:
        The minimum cost to connect all stations. Returns -1 if it is impossible 
        to connect all stations.

    Examples:
        >>> solve(4, [[0, 1, 10], [0, 2, 6], [0, 3, 5], [1, 3, 15], [2, 3, 4]])
        19
        >>> solve(4, [[0, 1, 10], [2, 3, 5]])
        -1
    """
    # Sort edges by cost to satisfy the greedy property of Kruskal's algorithm
    sorted_edges = sorted(edges, key=lambda edge: edge[2])
    
    dsu = DisjointSetUnion(n)
    total_min_cost = 0
    edges_count = 0

    for u, v, cost in sorted_edges:
        # Attempt to unite the two components connected by this edge
        if dsu.union(u, v):
            total_min_cost += cost
            edges_count += 1
            
            # If we have connected n-1 edges, the MST is complete
            if edges_count == n - 1:
                break

    # If the number of edges in MST is less than n-1, the graph is not connected
    if edges_count < n - 1:
        return -1

    return total_min_cost
