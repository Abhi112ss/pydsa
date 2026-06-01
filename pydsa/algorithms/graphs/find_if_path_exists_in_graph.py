METADATA = {
    "id": 1971,
    "name": "Find if Path Exists in Graph",
    "slug": "find-if-path-exists-in-graph",
    "category": "Graph",
    "aliases": [],
    "tags": ["union_find", "dfs", "bfs", "disjoint_set_union"],
    "difficulty": "medium",
    "time_complexity": "O(E * α(V))",
    "space_complexity": "O(V)",
    "description": "Determine if there is a valid path between a source and a destination in an undirected graph using Union-Find.",
}

class UnionFind:
    """An implementation of the Disjoint Set Union (DSU) data structure with path compression and union by rank."""

    def __init__(self, n: int):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, i: int) -> int:
        """Finds the representative of the set containing i, with path compression."""
        if self.parent[i] == i:
            return i
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i: int, j: int) -> bool:
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
            return True
        return False


def solve(n: int, edges: list[list[int]], source: int, destination: int) -> bool:
    """
    Determines if a path exists between source and destination in an undirected graph.

    Args:
        n: The number of vertices in the graph.
        edges: A list of undirected edges where edges[i] = [u, v].
        source: The starting vertex.
        destination: The target vertex.

    Returns:
        True if a path exists, False otherwise.

    Examples:
        >>> solve(3, [[0,1],[1,2],[2,0]], 0, 2)
        True
        >>> solve(6, [[0,1],[0,2],[3,5],[5,4],[4,3]], 0, 5)
        False
    """
    # Edge case: source and destination are the same
    if source == destination:
        return True

    dsu = UnionFind(n)

    # Iterate through all edges and merge connected components
    for u, v in edges:
        dsu.union(u, v)

    # If both source and destination share the same root, a path exists
    return dsu.find(source) == dsu.find(destination)
