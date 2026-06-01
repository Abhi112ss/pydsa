METADATA = {
    "id": 3807,
    "name": "Minimum Cost to Repair Edges to Traverse a Graph",
    "slug": "minimum-cost-to-repair-edges-to-traverse-a-graph",
    "category": "Greedy",
    "aliases": [],
    "tags": ["disjoint_set_union", "greedy", "kruskal"],
    "difficulty": "medium",
    "time_complexity": "O(E log E)",
    "space_complexity": "O(V)",
    "description": "Find the minimum cost to connect components in a graph using Kruskal's algorithm.",
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
    Calculates the minimum cost to repair edges to connect all nodes in a graph.
    
    Args:
        n: The number of nodes in the graph (labeled 0 to n-1).
        edges: A list of edges where each edge is [u, v, cost].
        
    Returns:
        The minimum cost to connect all nodes. Returns -1 if it's impossible 
        to connect all nodes.
        
    Examples:
        >>> solve(4, [[0, 1, 1], [1, 2, 2], [2, 3, 3]])
        6
        >>> solve(4, [[0, 1, 1], [2, 3, 1]])
        -1
    """
    # Sort edges by cost to satisfy the greedy property of Kruskal's algorithm
    edges.sort(key=lambda edge: edge[2])
    
    dsu = DisjointSetUnion(n)
    total_min_cost = 0
    edges_count = 0
    
    for u, v, cost in edges:
        # If u and v are not in the same component, connect them
        if dsu.union(u, v):
            total_min_cost += cost
            edges_count += 1
            
            # If we have connected all nodes, we can stop early
            if edges_count == n - 1:
                break
                
    # If the number of edges used is less than n-1, the graph is not fully connected
    return total_min_cost if edges_count == n - 1 else -1
