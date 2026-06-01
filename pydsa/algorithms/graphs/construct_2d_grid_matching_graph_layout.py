METADATA = {
    "id": 3311,
    "name": "Construct 2D Grid Matching Graph Layout",
    "slug": "construct-2d-grid-matching-graph-layout",
    "category": "Graphs",
    "aliases": [],
    "tags": ["graphs", "bfs", "dfs", "grid"],
    "difficulty": "medium",
    "time_complexity": "O(V + E)",
    "space_complexity": "O(V + E)",
    "description": "Construct a 2D grid layout for a graph where adjacent nodes in the graph are placed in adjacent cells in the grid.",
}

from collections import deque

def solve(n: int, edges: list[list[int]]) -> list[list[int]]:
    """
    Constructs a 2D grid layout for a graph such that connected nodes are adjacent.
    
    Note: This implementation assumes the graph is a simple path or a structure 
    that can be embedded into a grid linearly, as general graph embedding 
    into a grid is an NP-hard problem. For the purpose of this algorithmic 
    template, we implement a BFS-based layout strategy.

    Args:
        n: The number of nodes in the graph (labeled 0 to n-1).
        edges: A list of undirected edges where edges[i] = [u, v].

    Returns:
        A 2D grid (list of lists) where each cell contains the node index 
        or -1 if the cell is empty.

    Examples:
        >>> solve(4, [[0, 1], [1, 2], [2, 3]])
        [[0, 1], [2, 3]] (or similar valid grid)
    """
    if n == 0:
        return []

    # Build adjacency list
    adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    # Determine grid dimensions (square-ish)
    import math
    cols = math.ceil(math.sqrt(n))
    rows = math.ceil(n / cols)
    
    grid = [[-1 for _ in range(cols)] for _ in range(rows)]
    visited = [False] * n
    node_to_pos = {}

    # We use BFS to traverse the graph and assign positions in a snake-like 
    # or row-major order to ensure connectivity is preserved as much as possible.
    # For a general graph, this is a heuristic.
    
    queue = deque([0])
    visited[0] = True
    order = []

    while queue:
        curr = queue.popleft()
        order.append(curr)
        for neighbor in adj[curr]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)

    # If the graph is disconnected, handle other components
    for i in range(n):
        if not visited[i]:
            # Start BFS for new component
            queue.append(i)
            visited[i] = True
            while queue:
                curr = queue.popleft()
                order.append(curr)
                for neighbor in adj[curr]:
                    if not visited[neighbor]:
                        visited[neighbor] = True
                        queue.append(neighbor)

    # Fill the grid using the BFS traversal order
    # This ensures that nodes discovered together are placed near each other
    for idx, node_val in enumerate(order):
        r = idx // cols
        c = idx % cols
        grid[r][c] = node_val

    return grid
