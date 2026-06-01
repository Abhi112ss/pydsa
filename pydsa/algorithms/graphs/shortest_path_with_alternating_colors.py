METADATA = {
    "id": 1129,
    "name": "Shortest Path with Alternating Colors",
    "slug": "shortest-path-with-alternating-colors",
    "category": "Graph",
    "aliases": [],
    "tags": ["bfs", "graph", "shortest-path"],
    "difficulty": "medium",
    "time_complexity": "O(V + E)",
    "space_complexity": "O(V + E)",
    "description": "Find the shortest path from node 0 to node n-1 such that the edge colors alternate.",
}

from collections import deque

def solve(n: int, edges: list[list[int]]) -> list[int]:
    """
    Finds the shortest path from node 0 to node n-1 with alternating edge colors.

    Args:
        n: The number of nodes in the graph.
        edges: A list of edges where each edge is [u, v, color]. 
               Color is 0 for red and 1 for blue.

    Returns:
        A list of integers where the i-th element is the shortest distance 
        from node 0 to node i. If no path exists, the distance is -1.

    Examples:
        >>> solve(3, [[0,1,0],[1,2,1],[0,2,1]])
        [0, 1, 1]
        >>> solve(3, [[0,1,1],[1,2,1]])
        [0, 1, -1]
    """
    # Build adjacency list: adj[u] = [(v, color), ...]
    adj = [[] for _ in range(n)]
    for u, v, color in edges:
        adj[u].append((v, color))
        adj[v].append((u, color))

    # distances[node][last_color] stores the shortest distance to 'node' 
    # where the incoming edge had 'last_color'.
    # We use -1 to represent unvisited states.
    distances = [[-1, -1] for _ in range(n)]
    
    # Queue stores (current_node, last_edge_color, current_distance)
    # We start at node 0. Since there's no incoming edge, we can imagine 
    # we arrived via either color to allow the first edge to be either 0 or 1.
    queue = deque([(0, 0, 0), (0, 1, 0)])
    distances[0][0] = 0
    distances[0][1] = 0

    while queue:
        curr_node, last_color, dist = queue.popleft()

        # The next edge must have a color different from the last_color
        next_color = 1 - last_color

        for neighbor, edge_color in adj[curr_node]:
            # Check if the edge matches the alternating color requirement
            if edge_color == next_color:
                # If this node hasn't been visited with this specific incoming color
                if distances[neighbor][next_color] == -1:
                    distances[neighbor][next_color] = dist + 1
                    queue.append((neighbor, next_color, dist + 1))

    # The answer for each node is the minimum distance regardless of the last color
    result = []
    for i in range(n):
        d0 = distances[i][0]
        d1 = distances[i][1]
        
        if d0 == -1 and d1 == -1:
            result.append(-1)
        elif d0 == -1:
            result.append(d1)
        elif d1 == -1:
            result.append(d0)
        else:
            result.append(min(d0, d1))
            
    return result
