METADATA = {
    "id": 2608,
    "name": "Shortest Cycle in a Graph",
    "slug": "shortest-cycle-in-a-graph",
    "category": "Graphs",
    "aliases": [],
    "tags": ["bfs", "graphs"],
    "difficulty": "medium",
    "time_complexity": "O(V * (V + E))",
    "space_complexity": "O(V)",
    "description": "Find the length of the shortest cycle in an undirected graph, or -1 if no cycle exists.",
}

from collections import deque

def solve(n: int, edges: list[list[int]]) -> int:
    """
    Finds the length of the shortest cycle in an undirected graph.

    Args:
        n: The number of nodes in the graph.
        edges: A list of undirected edges where edges[i] = [u, v].

    Returns:
        The length of the shortest cycle, or -1 if no cycle exists.

    Examples:
        >>> solve(4, [[0, 1], [1, 2], [2, 3], [3, 0]])
        4
        >>> solve(3, [[0, 1], [1, 2]])
        -1
    """
    # Build adjacency list
    adj: list[list[int]] = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)

    min_cycle_length = float('inf')

    # Perform BFS starting from each node to find the shortest cycle containing that node
    for start_node in range(n):
        # distances[i] stores the shortest distance from start_node to i
        distances: list[int] = [-1] * n
        # parent[i] stores the predecessor of i in the BFS tree to avoid immediate backtracking
        parent: list[int] = [-1] * n
        
        queue: deque[int] = deque([start_node])
        distances[start_node] = 0
        
        while queue:
            current_node = queue.popleft()
            
            for neighbor in adj[current_node]:
                if distances[neighbor] == -1:
                    # Standard BFS: neighbor not visited, update distance and parent
                    distances[neighbor] = distances[current_node] + 1
                    parent[neighbor] = current_node
                    queue.append(neighbor)
                elif parent[current_node] != neighbor:
                    # If neighbor is visited and is NOT the parent of current_node, 
                    # we found a cycle. The cycle length is dist(start, u) + dist(start, v) + 1.
                    cycle_len = distances[current_node] + distances[neighbor] + 1
                    min_cycle_length = min(min_cycle_length, cycle_len)
                    
                    # Optimization: If we found a cycle of length 3, it's the smallest possible
                    if min_cycle_length == 3:
                        return 3
                    
                    # Note: We don't break the BFS immediately because a different neighbor 
                    # might yield an even shorter cycle within this BFS run.
                    # However, since BFS explores level by level, the first cycle found 
                    # involving start_node is likely the shortest for this start_node.

    return int(min_cycle_length) if min_cycle_length != float('inf') else -1
