METADATA = {
    "id": 1489,
    "name": "Find Critical and Pseudo-Critical Edges in Minimum Spanning Tree",
    "slug": "find-critical-and-pseudo-critical-edges-in-minimum-spanning-tree",
    "category": "Graph",
    "aliases": [],
    "tags": ["kruskal", "graphs", "union_find"],
    "difficulty": "hard",
    "time_complexity": "O(E^2 * alpha(V))",
    "space_complexity": "O(E + V)",
    "description": "Identify edges that must be in every MST (critical) and edges that can be part of some MST (pseudo-critical).",
}

class UnionFind:
    """Standard Disjoint Set Union (DSU) with path compression and union by rank."""
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

def solve(n: int, edges: list[list[int]]) -> list[list[int]]:
    """
    Finds critical and pseudo-critical edges in the Minimum Spanning Tree.

    Args:
        n: The number of nodes in the graph.
        edges: A list of edges where edges[i] = [u, v, weight].

    Returns:
        A list of two lists: [critical_edges, pseudo_critical_edges].

    Examples:
        >>> solve(4, [[0,1,1],[1,2,1],[2,3,1],[0,3,1]])
        [[[0, 1, 1], [1, 2, 1], [2, 3, 1], [0, 3, 1]], []]
    """
    # Store original index to identify edges after sorting
    # edges_with_index[i] = [u, v, weight, original_index]
    edges_with_index = []
    for i in range(len(edges)):
        edges_with_index.append(edges[i] + [i])

    # Sort edges by weight for Kruskal's algorithm
    edges_with_index.sort(key=lambda x: x[2])

    def get_mst_weight(n_nodes: int, edge_list: list[list[int]], forced_edge_idx: int = -1, 
                       ignored_edge_idx: int = -1) -> float:
        """Calculates MST weight with constraints."""
        uf = UnionFind(n_nodes)
        mst_weight = 0
        edges_count = 0

        # 1. If an edge is forced, add it first
        if forced_edge_idx != -1:
            u, v, w, idx = edge_list[forced_edge_idx]
            uf.union(u, v)
            mst_weight += w
            edges_count += 1

        # 2. Standard Kruskal's for the rest
        for i in range(len(edge_list)):
            if i == forced_edge_idx or i == ignored_edge_idx:
                continue
            
            u, v, w, idx = edge_list[i]
            if uf.union(u, v):
                mst_weight += w
                edges_count += 1
        
        # If we couldn't connect all nodes, return infinity
        return mst_weight if edges_count == n_nodes - 1 else float('inf')

    # Step 1: Calculate the baseline MST weight
    base_mst_weight = get_mst_weight(n, edges_with_index)

    critical = []
    pseudo_critical = []

    for i in range(len(edges_with_index)):
        # Step 2: Check if edge is critical
        # An edge is critical if removing it increases the MST weight
        if get_mst_weight(n, edges_with_index, ignored_edge_idx=i) > base_mst_weight:
            critical.append(edges[edges_with_index[i][3]])
        else:
            # Step 3: Check if edge is pseudo-critical
            # An edge is pseudo-critical if it's not critical but can be part of an MST
            # We check this by forcing the edge into the MST and seeing if weight remains same
            if get_mst_weight(n, edges_with_index, forced_edge_idx=i) == base_mst_weight:
                pseudo_critical.append(edges[edges_with_index[i][3]])

    return [critical, pseudo_critical]
