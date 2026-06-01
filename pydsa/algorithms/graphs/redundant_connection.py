METADATA = {
    "id": 684,
    "name": "Redundant Connection",
    "slug": "redundant-connection",
    "category": "Graph",
    "aliases": [],
    "tags": ["union_find", "graph", "disjoint_set"],
    "difficulty": "medium",
    "time_complexity": "O(n * alpha(n))",
    "space_complexity": "O(n)",
    "description": "Find an edge that can be removed so that the resulting graph is a tree.",
}

class UnionFind:
    """Implementation of the Disjoint Set Union (DSU) data structure with path compression and union by rank."""

    def __init__(self, n: int):
        """Initializes the DSU structure with n elements."""
        self.parent = list(range(n + 1))
        self.rank = [0] * (n + 1)

    def find(self, node: int) -> int:
        """Finds the representative of the set containing 'node' with path compression."""
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def union(self, node_a: int, node_b: int) -> bool:
        """
        Unites the sets containing node_a and node_b.
        Returns True if they were in different sets, False if they were already in the same set.
        """
        root_a = self.find(node_a)
        root_b = self.find(node_b)

        if root_a == root_b:
            return False

        # Union by rank to keep the tree flat
        if self.rank[root_a] < self.rank[root_b]:
            self.parent[root_a] = root_b
        elif self.rank[root_a] > self.rank[root_b]:
            self.parent[root_b] = root_a
        else:
            self.parent[root_b] = root_a
            self.rank[root_a] += 1
        
        return True

def solve(edges: list[list[int]]) -> list[int]:
    """
    Finds the redundant edge in a graph that forms a cycle.

    Args:
        edges: A list of edges where edges[i] = [u, v] represents an undirected edge.

    Returns:
        The last edge in the input list that completes a cycle.

    Examples:
        >>> solve([[1,2],[1,3],[2,3]])
        [2, 3]
        >>> solve([[1,2],[2,3],[3,4],[1,4],[1,5]])
        [1, 4]
    """
    # The number of nodes is equal to the number of edges in a graph with exactly one cycle
    num_nodes = len(edges)
    dsu = UnionFind(num_nodes)

    for u, v in edges:
        # If union returns False, it means u and v are already connected
        # via some other path, making this edge the redundant one that forms a cycle.
        if not dsu.union(u, v):
            return [u, v]

    return []
