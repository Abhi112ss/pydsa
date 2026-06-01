METADATA = {
    "id": 3123,
    "name": "Find Edges in Shortest Paths",
    "slug": "find-edges-in-shortest-paths",
    "category": "Graph",
    "aliases": [],
    "tags": ["bfs", "graph", "shortest_path"],
    "difficulty": "medium",
    "time_complexity": "O(V + E)",
    "space_complexity": "O(V + E)",
    "description": "Find all edges that belong to at least one shortest path between a source and a destination in an unweighted graph.",
}

from collections import deque

def solve(n: int, edges: list[list[int]], source: int, destination: int) -> list[int]:
    """
    Finds all edges that are part of at least one shortest path from source to destination.

    Args:
        n: The number of nodes in the graph.
        edges: A list of undirected edges where edges[i] = [u, v].
        source: The starting node.
        destination: The target node.

    Returns:
        A list of edge indices (0-indexed) that lie on a shortest path, sorted in ascending order.

    Examples:
        >>> solve(4, [[0, 1], [1, 2], [2, 3], [0, 2]], 0, 3)
        [0, 1, 3] (Note: actual indices depend on input order)
    """
    # Build adjacency list storing (neighbor, edge_index)
    adj = [[] for _ in range(n)]
    for idx, (u, v) in enumerate(edges):
        adj[u].append((v, idx))
        adj[v].append((u, idx))

    def bfs(start_node: int) -> list[int]:
        """Standard BFS to find shortest distances from start_node to all other nodes."""
        distances = [-1] * n
        distances[start_node] = 0
        queue = deque([start_node])
        
        while queue:
            curr = queue.popleft()
            for neighbor, _ in adj[curr]:
                if distances[neighbor] == -1:
                    distances[neighbor] = distances[curr] + 1
                    queue.append(neighbor)
        return distances

    # Step 1: Calculate distances from source to all nodes
    dist_from_source = bfs(source)
    
    # If destination is unreachable, return empty list
    if dist_from_source[destination] == -1:
        return []

    # Step 2: Calculate distances from destination to all nodes
    dist_from_dest = bfs(destination)

    shortest_path_len = dist_from_source[destination]
    result_edge_indices = []

    # Step 3: An edge (u, v) with index i is on a shortest path if:
    # dist_from_source[u] + 1 + dist_from_dest[v] == shortest_path_len
    # OR dist_from_source[v] + 1 + dist_from_dest[u] == shortest_path_len
    for i, (u, v) in enumerate(edges):
        # Check if u is closer to source and v is closer to destination
        condition_1 = (dist_from_source[u] != -1 and dist_from_dest[v] != -1 and 
                       dist_from_source[u] + 1 + dist_from_dest[v] == shortest_path_len)
        
        # Check if v is closer to source and u is closer to destination
        condition_2 = (dist_from_source[v] != -1 and dist_from_dest[u] != -1 and 
                       dist_from_source[v] + 1 + dist_from_dest[u] == shortest_path_len)
        
        if condition_1 or condition_2:
            result_edge_indices.append(i)

    return sorted(result_edge_indices)
