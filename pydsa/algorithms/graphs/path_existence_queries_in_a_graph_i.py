METADATA = {
    "id": 3532,
    "name": "Path Existence Queries in a Graph I",
    "slug": "path-existence-queries-in-a-graph-i",
    "category": "Graphs",
    "aliases": [],
    "tags": ["disjoint_set_union", "graphs", "union-find"],
    "difficulty": "medium",
    "time_complexity": "O((n + q) * alpha(n))",
    "space_complexity": "O(n)",
    "description": "Determine if a path exists between two nodes in a graph using Disjoint Set Union.",
}

class DisjointSetUnion:
    """Implementation of a Disjoint Set Union (DSU) with path compression and union by rank."""

    def __init__(self, n: int):
        self.parent = list(range(n + 1))
        self.rank = [0] * (n + 1)

    def find(self, i: int) -> int:
        """Finds the representative of the set containing i with path compression."""
        if self.parent[i] == i:
            return i
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i: int, j: int) -> None:
        """Unites the sets containing i and j using union by rank."""
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

def solve(n: int, edges: list[list[int]], queries: list[list[int]]) -> list[bool]:
    """
    Determines if a path exists between two nodes for multiple queries.

    Args:
        n: The number of nodes in the graph.
        edges: A list of edges where edges[i] = [u, v] represents an undirected edge.
        queries: A list of queries where queries[i] = [u, v] asks if u and v are connected.

    Returns:
        A list of booleans where the i-th element is True if a path exists, False otherwise.

    Examples:
        >>> solve(5, [[1, 2], [2, 3], [4, 5]], [[1, 3], [1, 4]])
        [True, False]
    """
    # Initialize DSU to manage connected components
    dsu = DisjointSetUnion(n)

    # Process all edges to build the connected components
    for u, v in edges:
        dsu.union(u, v)

    results: list[bool] = []
    # For each query, check if both nodes belong to the same component
    for u, v in queries:
        # If the roots of both nodes are the same, they are in the same component
        results.append(dsu.find(u) == dsu.find(v))

    return results
