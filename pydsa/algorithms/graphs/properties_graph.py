METADATA = {
    "id": 3493,
    "name": "Properties Graph",
    "slug": "properties_graph",
    "category": "Graphs",
    "aliases": [],
    "tags": ["graphs", "dfs", "bfs", "connectivity"],
    "difficulty": "medium",
    "time_complexity": "O(V + E)",
    "space_complexity": "O(V + E)",
    "description": "Determine if a graph satisfies specific structural properties such as connectivity or bipartiteness using graph traversal.",
}

class PropertiesGraphSolver:
    """
    A solver class to analyze graph properties such as connectivity and bipartiteness.
    """

    def solve(self, n: int, edges: list[list[int]]) -> dict[str, bool]:
        """
        Analyzes the graph to check for connectivity and bipartiteness.

        Args:
            n: The number of nodes in the graph (labeled 0 to n-1).
            edges: A list of undirected edges where edges[i] = [u, v].

        Returns:
            A dictionary containing two boolean keys:
            - 'is_connected': True if all nodes are reachable from node 0.
            - 'is_bipartite': True if the graph can be colored with 2 colors.

        Examples:
            >>> solver = PropertiesGraphSolver()
            >>> solver.solve(4, [[0, 1], [1, 2], [2, 3], [3, 0]])
            {'is_connected': True, 'is_bipartite': True}
            >>> solver.solve(4, [[0, 1], [1, 2], [2, 0], [2, 3]])
            {'is_connected': True, 'is_bipartite': False}
        """
        if n == 0:
            return {"is_connected": True, "is_bipartite": True}

        # Build adjacency list
        adj: dict[int, list[int]] = {i: [] for i in range(n)}
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        # 1. Check Connectivity using BFS
        visited_connectivity = [False] * n
        queue = [0]
        visited_connectivity[0] = True
        visited_count = 0
        
        head = 0
        while head < len(queue):
            curr = queue[head]
            head += 1
            visited_count += 1
            for neighbor in adj[curr]:
                if not visited_connectivity[neighbor]:
                    visited_connectivity[neighbor] = True
                    queue.append(neighbor)
        
        is_connected = (visited_count == n)

        # 2. Check Bipartiteness using BFS (2-coloring)
        # Note: A graph is bipartite if every connected component is bipartite.
        # Even if not connected, we must check all components.
        colors = {}  # node -> color (0 or 1)
        is_bipartite = True

        for start_node in range(n):
            if start_node not in colors:
                # Start BFS for a new component
                colors[start_node] = 0
                comp_queue = [start_node]
                comp_head = 0
                
                while comp_head < len(comp_queue):
                    u = comp_queue[comp_head]
                    comp_head += 1
                    
                    for v in adj[u]:
                        if v not in colors:
                            # Assign opposite color to neighbor
                            colors[v] = 1 - colors[u]
                            comp_queue.append(v)
                        elif colors[v] == colors[u]:
                            # Found an edge between nodes of same color
                            is_bipartite = False
                            break
                    if not is_bipartite:
                        break
            if not is_bipartite:
                break

        return {
            "is_connected": is_connected,
            "is_bipartite": is_bipartite
        }

def solve(n: int, edges: list[list[int]]) -> dict[str, bool]:
    """
    Entry point for the solver.
    """
    solver = PropertiesGraphSolver()
    return solver.solve(n, edges)
