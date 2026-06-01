METADATA = {
    "id": 3887,
    "name": "Incremental Even-Weighted Cycle Queries",
    "slug": "incremental_even_weighted_cycle_queries",
    "category": "Graphs",
    "aliases": [],
    "tags": ["graphs", "disjoint_set_union", "bit_manipulation"],
    "difficulty": "hard",
    "time_complexity": "O(q * alpha(n))",
    "space_complexity": "O(n)",
    "description": "Determine if adding an edge creates a cycle with an even total weight using DSU with parity tracking.",
}

class DSUWithParity:
    """
    Disjoint Set Union (DSU) implementation that tracks the parity 
    of the path weight from a node to its parent in the forest.
    """
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.rank = [0] * n
        # parity[i] stores the parity of the edge weight between node i and its parent
        # 0 for even, 1 for odd
        self.parity = [0] * n

    def find(self, i: int) -> tuple[int, int]:
        """
        Finds the root of node i and calculates the parity of the path to the root.
        Uses path compression.
        """
        if self.parent[i] == i:
            return i, 0
        
        root, root_parity = self.find(self.parent[i])
        # Path compression: update parent to root and update parity to be relative to root
        self.parent[i] = root
        self.parity[i] = (self.parity[i] + root_parity) % 2
        return self.parent[i], self.parity[i]

    def union(self, u: int, v: int, weight_parity: int) -> bool:
        """
        Adds an edge between u and v with a given weight parity.
        Returns True if an even-weighted cycle is formed, False otherwise.
        """
        root_u, parity_u = self.find(u)
        root_v, parity_v = self.find(v)

        if root_u != root_v:
            # Union by rank to keep the tree flat
            if self.rank[root_u] < self.rank[root_v]:
                root_u, root_v = root_v, root_u
                parity_u, parity_v = parity_v, parity_u
            
            # Connect root_v to root_u
            # The new edge parity between root_v and root_u must satisfy:
            # (parity_u + new_edge_parity + parity_v) % 2 == weight_parity
            self.parent[root_v] = root_u
            self.parity[root_v] = (parity_u + weight_parity + parity_v) % 2
            
            if self.rank[root_u] == self.rank[root_v]:
                self.rank[root_u] += 1
            return False
        else:
            # If they share a root, a cycle is formed.
            # The cycle weight parity is (parity_u + parity_v + weight_parity) % 2
            # We want to check if this cycle is even (parity == 0)
            cycle_parity = (parity_u + parity_v + weight_parity) % 2
            return cycle_parity == 0

def solve(n: int, queries: list[tuple[int, int, int]]) -> list[bool]:
    """
    Processes incremental edge additions and checks for even-weighted cycles.

    Args:
        n: The number of nodes in the graph.
        queries: A list of tuples (u, v, w) representing an edge between u and v 
                 with weight w.

    Returns:
        A list of booleans where the i-th element is True if the i-th edge 
        creates an even-weighted cycle.

    Examples:
        >>> solve(3, [(0, 1, 1), (1, 2, 1), (0, 2, 2)])
        [False, False, True]
    """
    dsu = DSUWithParity(n)
    results = []

    for u, v, w in queries:
        # We only care about the parity of the weight
        weight_parity = w % 2
        # Check if adding this edge creates an even cycle
        is_even_cycle = dsu.union(u, v, weight_parity)
        results.append(is_even_cycle)

    return results
