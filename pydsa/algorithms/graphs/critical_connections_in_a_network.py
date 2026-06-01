METADATA = {
    "id": 1192,
    "name": "Critical Connections in a Network",
    "slug": "critical-connections-in-a-network",
    "category": "Graph",
    "aliases": [],
    "tags": ["dfs", "tarjan", "graph", "bridges"],
    "difficulty": "hard",
    "time_complexity": "O(V + E)",
    "space_complexity": "O(V + E)",
    "description": "Find all bridges in an undirected graph using Tarjan's bridge-finding algorithm.",
}

def solve(n: int, connections: list[list[int]]) -> list[list[int]]:
    """
    Finds all critical connections (bridges) in an undirected graph.
    
    A critical connection is an edge that, if removed, increases the number 
    of connected components in the graph.

    Args:
        n: The number of nodes in the network.
        connections: A list of edges where connections[i] = [u, v].

    Returns:
        A list of edges that are critical connections.

    Examples:
        >>> solve(4, [[0,1],[1,2],[2,0],[1,3]])
        [[1, 3]]
    """
    # Build adjacency list
    adj: dict[int, list[int]] = {i: [] for i in range(n)}
    for u, v in connections:
        adj[u].append(v)
        adj[v].append(u)

    # discovery_time[i] stores the time at which node i was first visited
    discovery_time: list[int] = [-1] * n
    # low_link[i] stores the lowest discovery time reachable from node i 
    # (including itself) in the DFS tree using back-edges.
    low_link: list[int] = [-1] * n
    
    bridges: list[list[int]] = []
    timer = 0

    def dfs(current_node: int, parent_node: int) -> None:
        nonlocal timer
        discovery_time[current_node] = low_link[current_node] = timer
        timer += 1

        for neighbor in adj[current_node]:
            if neighbor == parent_node:
                continue
            
            if discovery_time[neighbor] == -1:
                # Node not visited, recurse
                dfs(neighbor, current_node)
                
                # Upon return, update low_link of current node based on child
                low_link[current_node] = min(low_link[current_node], low_link[neighbor])
                
                # If the lowest node reachable from neighbor is still "after" 
                # current_node in DFS traversal, then (current, neighbor) is a bridge.
                if low_link[neighbor] > discovery_time[current_node]:
                    bridges.append([current_node, neighbor])
            else:
                # Neighbor already visited, this is a back-edge
                # Update low_link based on the discovery time of the neighbor
                low_link[current_node] = min(low_link[current_node], discovery_time[neighbor])

    # Start DFS from node 0 (assuming graph is connected as per problem constraints)
    dfs(0, -1)
    
    return bridges
