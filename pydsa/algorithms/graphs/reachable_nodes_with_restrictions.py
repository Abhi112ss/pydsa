METADATA = {
    "id": 2368,
    "name": "Reachable Nodes With Restrictions",
    "slug": "reachable-nodes-with-restrictions",
    "category": "Graph",
    "aliases": [],
    "tags": ["bfs", "dfs", "graph", "traversal"],
    "difficulty": "medium",
    "time_complexity": "O(V + E)",
    "space_complexity": "O(V)",
    "description": "Find the number of nodes reachable from node 0 in a graph, excluding nodes present in a restricted set.",
}

from collections import deque

def solve(n: int, edges: list[list[int]], restricted: list[int]) -> int:
    """
    Calculates the number of reachable nodes from node 0 given a set of restricted nodes.

    Args:
        n: The total number of nodes in the graph (nodes are 0 to n-1).
        edges: A list of undirected edges where edges[i] = [u, v].
        restricted: A list of nodes that cannot be visited.

    Returns:
        The count of reachable nodes that are not in the restricted set.

    Examples:
        >>> solve(4, [[0,1],[1,2],[2,3]], [2])
        2
        >>> solve(4, [[0,1],[1,2],[2,3]], [1])
        1
    """
    # Convert restricted list to a set for O(1) lookup time
    restricted_set = set(restricted)
    
    # Build the adjacency list for the graph
    adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
        
    # If the starting node is restricted, no nodes are reachable
    if 0 in restricted_set:
        return 0
        
    visited = set()
    queue = deque([0])
    visited.add(0)
    reachable_count = 0
    
    while queue:
        current_node = queue.popleft()
        reachable_count += 1
        
        for neighbor in adj[current_node]:
            # Only visit if the neighbor hasn't been visited and isn't restricted
            if neighbor not in visited and neighbor not in restricted_set:
                visited.add(neighbor)
                queue.append(neighbor)
                
    return reachable_count
