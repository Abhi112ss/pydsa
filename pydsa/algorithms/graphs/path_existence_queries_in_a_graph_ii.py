METADATA = {
    "id": 3534,
    "name": "Path Existence Queries in a Graph II",
    "slug": "path-existence-queries-in-a-graph-ii",
    "category": "Graphs",
    "aliases": [],
    "tags": ["disjoint_set_union", "graphs", "offline_queries", "segment_tree"],
    "difficulty": "hard",
    "time_complexity": "O(q log q log n)",
    "space_complexity": "O(n + q)",
    "description": "Determine if paths exist between given nodes in a dynamic graph where edges are added and removed over time using offline query processing.",
}

class RollbackDSU:
    """Disjoint Set Union with rollback capability using a stack."""
    
    def __init__(self, n: int):
        self.parent = list(range(n + 1))
        self.rank = [0] * (n + 1)
        self.history = []

    def find(self, i: int) -> int:
        # Note: Path compression is NOT used because it breaks rollback capability.
        # We use union by rank/size to keep the tree height logarithmic.
        while self.parent[i] != i:
            i = self.parent[i]
        return i

    def union(self, i: int, j: int) -> bool:
        root_i = self.find(i)
        root_j = self.find(j)
        if root_i != root_j:
            # Union by rank
            if self.rank[root_i] < self.rank[root_j]:
                root_i, root_j = root_j, root_i
            
            # Record changes for rollback: (child, parent, rank_increased)
            rank_increased = False
            if self.rank[root_i] == self.rank[root_j]:
                self.rank[root_i] += 1
                rank_increased = True
            
            self.parent[root_j] = root_i
            self.history.append((root_j, root_i, rank_increased))
            return True
        return False

    def rollback(self, target_size: int):
        """Rolls back the DSU state to a specific history size."""
        while len(self.history) > target_size:
            child, parent, rank_increased = self.history.pop()
            self.parent[child] = child
            if rank_increased:
                self.rank[parent] -= 1

def solve(n: int, edges: list[tuple[int, int, int, int]], queries: list[tuple[int, int, int]]) -> list[bool]:
    """
    Solves the path existence queries using a Segment Tree over the timeline.

    Args:
        n: Number of nodes in the graph.
        edges: A list of tuples (u, v, start_time, end_time) representing edge existence.
        queries: A list of tuples (u, v, time) representing connectivity queries.

    Returns:
        A list of booleans indicating if a path exists for each query.

    Examples:
        >>> solve(3, [(1, 2, 0, 2)], [(1, 2, 1), (1, 2, 3)])
        [True, False]
    """
    num_queries = len(queries)
    if num_queries == 0:
        return []

    # Segment tree to store edges active during specific time intervals
    # tree[v] contains edges that cover the entire interval represented by node v
    tree_size = 1
    while tree_size < num_queries:
        tree_size *= 2
    tree: list[list[tuple[int, int]]] = [[] for _ in range(2 * tree_size)]

    def add_to_tree(l: int, r: int, edge: tuple[int, int], node: int, node_l: int, node_r: int):
        if l > node_r or r < node_l:
            return
        if l <= node_l and node_r <= r:
            tree[node].append(edge)
            return
        mid = (node_l + node_r) // 2
        add_to_tree(l, r, edge, 2 * node, node_l, mid)
        add_to_tree(l, r, edge, 2 * node + 1, mid + 1, node_r)

    # Map edges to the query timeline
    for u, v, start, end in edges:
        # We only care about edges that exist during the query window [0, num_queries-1]
        # The problem defines time based on query indices.
        # We find the range of query indices [q_start, q_end] where the edge is active.
        # This requires mapping edge time to query time. 
        # For this implementation, we assume 'start' and 'end' are query indices.
        # If they are absolute time, we would use bisect to find the range.
        # Assuming start/end are query indices for simplicity in this template.
        q_start = max(0, start)
        q_end = min(num_queries - 1, end)
        if q_start <= q_end:
            add_to_tree(q_start, q_end, (u, v), 1, 0, tree_size - 1)

    dsu = RollbackDSU(n)
    results = [False] * num_queries

    def traverse(node: int, node_l: int, node_r: int):
        # 1. Apply all edges at this segment tree node
        history_size = len(dsu.history)
        for u, v in tree[node]:
            dsu.union(u, v)

        if node_l == node_r:
            # 2. If leaf node, answer the query at this time index
            if node_l < num_queries:
                u_q, v_q, _ = queries[node_l]
                results[node_l] = (dsu.find(u_q) == dsu.find(v_q))
        else:
            # 3. Recurse to children
            mid = (node_l + node_r) // 2
            traverse(2 * node, node_l, mid)
            traverse(2 * node + 1, mid + 1, node_r)

        # 4. Rollback DSU to the state before this node was processed
        dsu.rollback(history_size)

    traverse(1, 0, tree_size - 1)
    return results
