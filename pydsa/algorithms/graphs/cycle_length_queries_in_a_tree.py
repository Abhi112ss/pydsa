METADATA = {
    "id": 2509,
    "name": "Cycle Length Queries in a Tree",
    "slug": "cycle-length-queries-in-a-tree",
    "category": "Graphs",
    "aliases": [],
    "tags": ["graphs", "lca", "tree", "binary lifting"],
    "difficulty": "hard",
    "time_complexity": "O((n + q) log n)",
    "space_complexity": "O(n log n)",
    "description": "Calculate the length of a cycle formed by adding an edge between two nodes in a tree, which is the distance between them plus one.",
}

class CycleLengthSolver:
    """
    A solver for finding cycle lengths in a tree when an edge is added between two nodes.
    The cycle length is defined as the distance between the two nodes plus one.
    """

    def __init__(self, n: int, edges: list[list[int]]):
        self.n = n
        self.adj = [[] for _ in range(n)]
        for u, v in edges:
            self.adj[u].append(v)
            self.adj[v].append(u)
        
        # Binary lifting table for LCA and depth array
        self.max_log = n.bit_length()
        self.up = [[-1] * self.max_log for _ in range(n)]
        self.depth = [0] * n
        self._preprocess_lca()

    def _preprocess_lca(self) -> None:
        """Performs BFS to compute depths and the first level of binary lifting table."""
        queue = [0]
        visited = [False] * self.n
        visited[0] = True
        
        # BFS to establish parent-child relationships and depths
        head = 0
        while head < len(queue):
            u = queue[head]
            head += 1
            for v in self.adj[u]:
                if not visited[v]:
                    visited[v] = True
                    self.depth[v] = self.depth[u] + 1
                    self.up[v][0] = u
                    queue.append(v)
        
        # Fill the binary lifting table: up[i][j] is the 2^j-th ancestor of i
        for j in range(1, self.max_log):
            for i in range(self.n):
                if self.up[i][j-1] != -1:
                    self.up[i][j] = self.up[self.up[i][j-1]][j-1]

    def get_lca(self, u: int, v: int) -> int:
        """Finds the Lowest Common Ancestor of nodes u and v using binary lifting."""
        if self.depth[u] < self.depth[v]:
            u, v = v, u
        
        # Lift u up to the same depth as v
        diff = self.depth[u] - self.depth[v]
        for j in range(self.max_log):
            if (diff >> j) & 1:
                u = self.up[u][j]
        
        if u == v:
            return u
        
        # Lift both u and v until their parents are the same
        for j in range(self.max_log - 1, -1, -1):
            if self.up[u][j] != self.up[v][j]:
                u = self.up[u][j]
                v = self.up[v][j]
        
        return self.up[u][0]

    def get_distance(self, u: int, v: int) -> int:
        """Calculates the distance between nodes u and v in the tree."""
        lca = self.get_lca(u, v)
        return self.depth[u] + self.depth[v] - 2 * self.depth[lca]


def solve(n: int, edges: list[list[int]], queries: list[list[int]]) -> list[int]:
    """
    Solves the cycle length queries.

    Args:
        n: The number of nodes in the tree.
        edges: A list of edges representing the tree structure.
        queries: A list of queries, where each query is [u, v].

    Returns:
        A list of integers representing the cycle length for each query.

    Examples:
        >>> solve(3, [[0, 1], [1, 2]], [[0, 2]])
        [3]
        >>> solve(4, [[0, 1], [1, 2], [1, 3]], [[0, 2], [2, 3]])
        [3, 3]
    """
    solver = CycleLengthSolver(n, edges)
    results = []
    for u, v in queries:
        # Cycle length = distance(u, v) + 1
        results.append(solver.get_distance(u, v) + 1)
    return results
