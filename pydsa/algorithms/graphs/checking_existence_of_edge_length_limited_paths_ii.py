METADATA = {
    "id": 1724,
    "name": "Checking Existence of Edge Length Limited Paths II",
    "slug": "checking-existence-of-edge-length-limited-paths-ii",
    "category": "Graph",
    "aliases": [],
    "tags": ["union_find", "sorting", "graphs"],
    "difficulty": "hard",
    "time_complexity": "O(E log E + Q log Q)",
    "space_complexity": "O(E + Q)",
    "description": "Determine if paths between query nodes exist using only edges with weights less than or equal to a given limit, processed offline using DSU.",
}

class DisjointSetUnion:
    """Implementation of a Disjoint Set Union (DSU) with path compression and union by rank."""
    
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, i: int) -> int:
        if self.parent[i] == i:
            return i
        # Path compression
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i: int, j: int) -> bool:
        root_i = self.find(i)
        root_j = self.find(j)
        if root_i != root_j:
            # Union by rank
            if self.rank[root_i] < self.rank[root_j]:
                self.parent[root_i] = root_j
            elif self.rank[root_i] > self.rank[root_j]:
                self.parent[root_j] = root_i
            else:
                self.parent[root_i] = root_j
                self.rank[root_j] += 1
            return True
        return False

def solve(n: int, edges: list[list[int]], queries: list[list[int]]) -> list[bool]:
    """
    Checks if paths exist between query nodes using edges with weights <= query limits.

    Args:
        n: The number of nodes in the graph.
        edges: A list of edges where edges[i] = [u, v, w].
        queries: A list of queries where queries[i] = [u, v, limit].

    Returns:
        A list of booleans indicating if a path exists for each query.

    Examples:
        >>> solve(4, [[0,1,1],[1,2,2],[2,3,3]], [[0,3,3],[0,3,2]])
        [True, False]
    """
    # Sort edges by weight to process them in non-decreasing order
    sorted_edges = sorted(edges, key=lambda x: x[2])
    
    # Store queries with their original indices to return results in correct order
    # Query format: [u, v, limit, original_index]
    indexed_queries = []
    for i, q in enumerate(queries):
        indexed_queries.append((q[0], q[1], q[2], i))
    
    # Sort queries by their weight limit to process them offline
    indexed_queries.sort(key=lambda x: x[2])
    
    dsu = DisjointSetUnion(n)
    results = [False] * len(queries)
    edge_idx = 0
    
    # Process each query
    for u, v, limit, original_idx in indexed_queries:
        # Add all edges that satisfy the current query's weight limit
        while edge_idx < len(sorted_edges) and sorted_edges[edge_idx][2] <= limit:
            u_edge, v_edge, _ = sorted_edges[edge_idx]
            dsu.union(u_edge, v_edge)
            edge_idx += 1
        
        # If u and v are in the same component, a path exists
        if dsu.find(u) == dsu.find(v):
            results[original_idx] = True
            
    return results
