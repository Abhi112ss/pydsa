METADATA = {
    "id": 1627,
    "name": "Graph Connectivity With Threshold",
    "slug": "graph-connectivity-with-threshold",
    "category": "Union Find",
    "aliases": [],
    "tags": ["union_find", "graphs", "sorting"],
    "difficulty": "medium",
    "time_complexity": "O(q log q + e log e + q alpha(n))",
    "space_complexity": "O(n + q)",
    "description": "Determine the connectivity of a graph given a set of edges and queries with varying weight thresholds using an offline approach.",
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

def solve(n: int, edges: list[list[int]], queries: list[list[int]]) -> list[int]:
    """
    Solves the graph connectivity problem using an offline approach with Union-Find.

    Args:
        n: The number of nodes in the graph.
        edges: A list of edges where edges[i] = [u, v, w] representing an edge between u and v with weight w.
        queries: A list of queries where queries[i] = [threshold, expected_components].

    Returns:
        A list of integers where result[i] is 1 if the graph has at most expected_components 
        with edges having weight >= threshold, and 0 otherwise.

    Examples:
        >>> solve(4, [[0,1,2],[1,2,3],[2,3,4],[3,0,1]], [[4,4],[2,2],[1,1]])
        [1, 0, 0]
    """
    # Sort edges by weight in descending order to process heaviest edges first
    sorted_edges = sorted(edges, key=lambda x: x[2], reverse=True)
    
    # Sort queries by threshold in descending order to process highest thresholds first
    # We keep track of original indices to return the result in the correct order
    indexed_queries = sorted(enumerate(queries), key=lambda x: x[1][0], reverse=True)
    
    dsu = UnionFind(n)
    results = [0] * len(queries)
    edge_idx = 0
    
    for original_idx, (threshold, expected_components) in indexed_queries:
        # Add all edges that satisfy the current threshold requirement
        while edge_idx < len(sorted_edges) and sorted_edges[edge_idx][2] >= threshold:
            u, v, _ = sorted_edges[edge_idx]
            dsu.union(u, v)
            edge_idx += 1
        
        # If the current number of connected components is <= expected, query is satisfied
        if dsu.num_components <= expected_components:
            results[original_idx] = 1
            
    return results
