METADATA = {
    "id": 685,
    "name": "Redundant Connection II",
    "slug": "redundant-connection-ii",
    "category": "Graph",
    "aliases": [],
    "tags": ["union_find", "graph", "dfs"],
    "difficulty": "hard",
    "time_complexity": "O(n * alpha(n))",
    "space_complexity": "O(n)",
    "description": "Find an edge that, when removed, results in a tree structure in a directed graph.",
}

class UnionFind:
    """Standard Disjoint Set Union (DSU) implementation with path compression and union by rank."""
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

def solve(edges: list[list[int]]) -> list[int]:
    """
    Finds the edge that makes the directed graph not a tree.
    
    A directed graph is a tree if:
    1. Every node has exactly one parent (except the root).
    2. There are no cycles.

    Args:
        edges: A list of directed edges where edges[i] = [u, v] means u -> v.

    Returns:
        The edge that, when removed, makes the graph a tree.

    Examples:
        >>> solve([[1,2],[1,3],[2,3]])
        [2,3]
        >>> solve([[1,2],[2,3],[3,4],[1,4],[1,5]])
        [1,4]
        >>> solve([[1,2],[2,3],[3,4],[4,1],[1,5]])
        [4,1]
    """
    n = len(edges)
    parent_map = {}
    candidate_edge = None

    # Step 1: Check for a node with two parents
    for u, v in edges:
        if v in parent_map:
            # If v already has a parent, the current edge or the existing edge is a candidate
            candidate_edge = [parent_map[v], v]
            duplicate_edge = [u, v]
            # We will test these two candidates later
            # But for now, we store the 'bad' edge to try removing it
            # We'll use a logic: try removing candidate_edge, if cycle remains, remove duplicate_edge
            # However, a simpler way: if we find a double parent, we try removing [parent_map[v], v]
            # and if that doesn't fix the cycle, we remove [u, v].
            # To keep it clean, let's identify the two edges involved in the double-parent conflict.
            # We'll handle this by trying to remove the edge that causes the double parent.
            pass 
        parent_map[v] = u

    # Refined logic for double parent:
    # If there's a node with two parents, one of the two edges pointing to it must be removed.
    # Let's find which one.
    
    # Re-run to find the specific edges
    parent_map = {}
    double_parent_edge = None
    for u, v in edges:
        if v in parent_map:
            double_parent_edge = [u, v]
            # The edge that was already there
            # We'll store the existing one to compare
            existing_edge = [parent_map[v], v]
            
            # Case A: Try removing the existing edge. If no cycle, existing_edge is the answer.
            # Case B: If removing existing edge still leaves a cycle, then double_parent_edge is the answer.
            
            # Helper to check for cycle without a specific edge
            def has_cycle(edges_to_use: list[list[int]]) -> bool:
                uf = UnionFind(n)
                for edge in edges_to_use:
                    if not uf.union(edge[0], edge[1]):
                        return True
                return False

            # Try removing existing_edge
            remaining_edges_a = [e for e in edges if e != existing_edge]
            if not has_cycle(remaining_edges_a):
                return existing_edge
            else:
                return double_parent_edge
        parent_map[v] = u

    # Step 2: If no node has two parents, there must be a cycle.
    # Use Union-Find to find the edge that completes the cycle.
    uf = UnionFind(n)
    for u, v in edges:
        if not uf.union(u, v):
            return [u, v]

    return []
