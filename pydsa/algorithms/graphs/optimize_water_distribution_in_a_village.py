METADATA = {
    "id": 1168,
    "name": "Optimize Water Distribution in a Village",
    "slug": "optimize-water-distribution-in-a-village",
    "category": "Graph",
    "aliases": [],
    "tags": ["mst", "union_find", "kruskal"],
    "difficulty": "hard",
    "time_complexity": "O(E log E)",
    "space_complexity": "O(V + E)",
    "description": "Find the minimum cost to supply water to all houses by considering both building wells and laying pipes.",
}

class UnionFind:
    """A standard Disjoint Set Union (DSU) implementation with path compression and union by rank."""
    
    def __init__(self, n: int):
        self.parent = list(range(n + 1))
        self.rank = [0] * (n + 1)

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

def solve(n: int, wells: list[int], pipes: list[list[int]]) -> int:
    """
    Calculates the minimum cost to provide water to all houses using Kruskal's algorithm.
    
    The problem is modeled as finding a Minimum Spanning Tree (MST). We introduce a 
    virtual node (node 0) representing a universal water source. Building a well 
    at house 'i' is equivalent to adding an edge between node 0 and node 'i' 
    with weight 'wells[i-1]'.

    Args:
        n: The number of houses.
        wells: A list where wells[i] is the cost of building a well in house i+1.
        pipes: A list of [house1, house2, cost] representing pipe connections.

    Returns:
        The minimum cost to supply water to all houses.

    Examples:
        >>> solve(1, [1], [])
        1
        >>> solve(2, [1, 2], [[1, 2, 1]])
        2
    """
    # edges will store tuples of (cost, u, v)
    edges: list[tuple[int, int, int]] = []

    # 1. Add virtual edges representing wells. 
    # Node 0 is the virtual source. Connecting node 0 to house i costs wells[i-1].
    for i, cost in enumerate(wells):
        house_index = i + 1
        edges.append((cost, 0, house_index))

    # 2. Add existing pipe connections as edges.
    for house_a, house_b, cost in pipes:
        edges.append((cost, house_a, house_b))

    # 3. Sort all edges by cost to prepare for Kruskal's algorithm.
    edges.sort()

    union_find = UnionFind(n)
    total_min_cost = 0
    edges_count = 0

    # 4. Iterate through sorted edges and add them if they don't form a cycle.
    for cost, u, v in edges:
        if union_find.union(u, v):
            total_min_cost += cost
            edges_count += 1
            # If we have connected all n+1 nodes (0 to n), we have an MST.
            if edges_count == n:
                break

    return total_min_cost
