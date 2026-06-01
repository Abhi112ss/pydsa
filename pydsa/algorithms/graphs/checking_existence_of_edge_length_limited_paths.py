METADATA = {
    "id": 1697,
    "name": "Checking Existence of Edge Length Limited Paths",
    "slug": "checking-existence-of-edge-length-limited-paths",
    "category": "Graph",
    "aliases": [],
    "tags": ["union_find", "sorting", "graphs"],
    "difficulty": "hard",
    "time_complexity": "O(E log E + Q log Q)",
    "space_complexity": "O(N + Q)",
    "description": "Determine if paths exist between given nodes such that all edges in the path are within a specified weight limit using DSU and offline query processing.",
}

class DisjointSetUnion:
    """Implementation of a Disjoint Set Union (DSU) with path compression and union by rank."""
    
    def __init__(self, n: int):
        self.parent = list(range(n + 1))
        self.rank = [0] * (n + 1)

    def find(self, i: int) -> int:
        if self.parent[i] == i:
            return i
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i: int, j: int) -> None:
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
    Checks if paths exist between query nodes using only edges with weight <= limit.

    Args:
        n: The number of nodes in the graph.
        edges: A list of edges where edges[i] = [u, v, w] (u, v are nodes, w is weight).
        queries: A list of queries where queries[i] = [xi, yi, w_i] (xi, yi are nodes, w_i is weight limit).

    Returns:
        A list of booleans indicating if a valid path exists for each query.

    Examples:
        >>> solve(3, [[1,2,1],[2,3,2]], [[1,3,1],[1,3,2]])
        [False, True]
    """
    # Sort edges by weight to process them incrementally
    sorted_edges = sorted(edges, key=lambda x: x[2])
    
    # Sort queries by weight limit to process them offline
    # We store the original index to return results in the correct order
    indexed_queries = []
    for i, query in enumerate(queries):
        indexed_queries.append((query[2], query[0], query[1], i))
    indexed_queries.sort()

    results = [False] * len(queries)
    dsu = DisjointSetUnion(n)
    edge_idx = 0

    # Iterate through sorted queries
    for limit, u, v, original_idx in indexed_queries:
        # Add all edges that satisfy the current query's weight limit
        while edge_idx < len(sorted_edges) and sorted_edges[edge_idx][2] <= limit:
            curr_u, curr_v, _ = sorted_edges[edge_idx]
            dsu.union(curr_u, curr_v)
            edge_idx += 1
        
        # If u and v are in the same component, a valid path exists
        if dsu.find(u) == dsu.find(v):
            results[original_idx] = True

    return results
