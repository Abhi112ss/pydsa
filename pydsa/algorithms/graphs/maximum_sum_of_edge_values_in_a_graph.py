METADATA = {
    "id": 3547,
    "name": "Maximum Sum of Edge Values in a Graph",
    "slug": "maximum_sum_of_edge_values_in_a_graph",
    "category": "Greedy",
    "aliases": [],
    "tags": ["greedy", "mst", "graph"],
    "difficulty": "medium",
    "time_complexity": "O(E log E)",
    "space_complexity": "O(V)",
    "description": "Find the maximum sum of edge values such that the selected edges do not form a cycle and satisfy specific connectivity constraints.",
}

class UnionFind:
    """A standard Disjoint Set Union (DSU) implementation with path compression and union by rank."""
    
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.rank = [0] * n

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
            return True
        return False

def solve(n: int, edges: list[list[int]]) -> int:
    """
    Calculates the maximum sum of edge values in a graph without forming cycles.
    
    This is essentially finding the Maximum Spanning Tree (MST) weight.
    We use Kruskal's algorithm, but instead of sorting edges in ascending order,
    we sort them in descending order to maximize the sum.

    Args:
        n: The number of vertices in the graph.
        edges: A list of edges where each edge is [u, v, weight].

    Returns:
        The maximum sum of edge weights that can be selected without forming a cycle.

    Examples:
        >>> solve(3, [[0, 1, 10], [1, 2, 20], [0, 2, 5]])
        30
        >>> solve(4, [[0, 1, 1], [1, 2, 2], [2, 3, 3], [3, 0, 4], [0, 2, 5]])
        10
    """
    # Sort edges by weight in descending order to apply greedy approach
    sorted_edges = sorted(edges, key=lambda x: x[2], reverse=True)
    
    dsu = UnionFind(n)
    max_sum = 0
    edges_count = 0
    
    for u, v, weight in sorted_edges:
        # If u and v are not in the same component, adding this edge won't form a cycle
        if dsu.union(u, v):
            max_sum += weight
            edges_count += 1
            
            # Optimization: If we have connected all nodes (n-1 edges), we can stop
            if edges_count == n - 1:
                break
                
    return max_sum
