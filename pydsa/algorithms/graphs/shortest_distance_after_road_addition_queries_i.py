METADATA = {
    "id": 3243,
    "name": "Shortest Distance After Road Addition Queries I",
    "slug": "shortest-distance-after-road-addition-queries-i",
    "category": "Graphs",
    "aliases": [],
    "tags": ["graphs", "bfs", "shortest_path"],
    "difficulty": "medium",
    "time_complexity": "O(q * (n + m))",
    "space_complexity": "O(n + m)",
    "description": "Find the shortest distance between two nodes in a graph after multiple edge additions using BFS.",
}

from collections import deque

def solve(n: int, edges: list[list[int]], queries: list[list[int]]) -> list[int]:
    """
    Calculates the shortest distance between two nodes after each road addition.

    Args:
        n: The number of nodes in the graph (nodes are 0-indexed).
        edges: A list of edges where edges[i] = [u, v] representing an undirected edge.
        queries: A list of queries where queries[i] = [u, v] representing a new edge to add.

    Returns:
        A list of integers representing the shortest distance for each query.

    Examples:
        >>> solve(3, [[0, 1]], [[1, 2], [0, 2]])
        [2, 1]
    """
    # Build the initial adjacency list
    adj: list[list[int]] = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    results: list[int] = []

    for u_new, v_new in queries:
        # Add the new edge to the graph for this query
        adj[u_new].append(v_new)
        adj[v_new].append(u_new)

        # Perform BFS to find the shortest path from u_new to v_new
        # Since all edges have weight 1, BFS is optimal for shortest path
        distances: list[int] = [-1] * n
        queue: deque[int] = deque([u_new])
        distances[u_new] = 0
        
        found_dist = -1
        while queue:
            curr = queue.popleft()
            
            if curr == v_new:
                found_dist = distances[curr]
                break
                
            for neighbor in adj[curr]:
                if distances[neighbor] == -1:
                    distances[neighbor] = distances[curr] + 1
                    queue.append(neighbor)
        
        results.append(found_dist)
        
        # Note: The problem implies queries are cumulative (road additions persist).
        # If the problem meant queries are independent, we would remove the edge here.
        # Based on "Shortest Distance After Road Addition Queries", additions are permanent.

    return results
