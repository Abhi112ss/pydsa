METADATA = {
    "id": 3839,
    "name": "Number of Prefix Connected Groups",
    "slug": "number_of_prefix_connected_groups",
    "category": "Graphs",
    "aliases": [],
    "tags": ["union_find", "graphs", "disjoint_set_union"],
    "difficulty": "medium",
    "time_complexity": "O(n * alpha(n))",
    "space_complexity": "O(n)",
    "description": "Count the number of connected components in a graph as edges are added one by one.",
}

class DisjointSetUnion:
    """A standard implementation of the Disjoint Set Union (DSU) data structure."""

    def __init__(self, n: int):
        self.parent = list(range(n + 1))
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
            self.parent[root_i] = root_j
            self.num_components -= 1
            return True
        return False


def solve(n: int, edges: list[list[int]]) -> list[int]:
    """
    Calculates the number of connected components after adding each edge sequentially.

    Args:
        n: The number of nodes in the graph (labeled 1 to n).
        edges: A list of edges where edges[i] = [u, v] represents an edge between u and v.

    Returns:
        A list of integers where the i-th element is the number of connected components
        after adding the i-th edge.

    Examples:
        >>> solve(4, [[1, 2], [2, 3], [3, 4]])
        [3, 2, 1]
        >>> solve(3, [[1, 2], [1, 2]])
        [2, 2]
    """
    # Initialize DSU with n nodes.
    # Note: We use n + 1 to handle 1-based indexing easily.
    dsu = DisjointSetUnion(n)
    results = []

    for u, v in edges:
        # Perform union operation. If u and v were in different components,
        # the number of components decreases by 1.
        dsu.union(u, v)
        
        # The current number of connected components is stored in the DSU object.
        results.append(dsu.num_components)

    return results
