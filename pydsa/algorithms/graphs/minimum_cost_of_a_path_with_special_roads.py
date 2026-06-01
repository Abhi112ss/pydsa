METADATA = {
    "id": 2662,
    "name": "Minimum Cost of a Path With Special Roads",
    "slug": "minimum-cost-of-a-path-with-special-roads",
    "category": "Graph",
    "aliases": [],
    "tags": ["dijkstra", "graph", "priority_queue"],
    "difficulty": "hard",
    "time_complexity": "O(k^2 log k)",
    "space_complexity": "O(k)",
    "description": "Find the minimum cost to travel from (0,0) to (n,n) given a set of special roads with specific costs.",
}

import heapq

def solve(n: int, specialRoads: list[list[int]]) -> int:
    """
    Calculates the minimum cost to travel from (0,0) to (n,n) using special roads.

    The problem is modeled as a shortest path problem on a graph where the nodes 
    are the start and end points of the special roads, plus the destination (n,n).

    Args:
        n: The dimension of the grid (destination is (n, n)).
        specialRoads: A list of roads where each road is [x1, y1, x2, y2, cost].

    Returns:
        The minimum cost to reach (n, n) from (0, 0).

    Examples:
        >>> solve(4, [[0, 0, 1, 1, 4], [0, 2, 3, 3, 2]])
        6
        >>> solve(10, [[0, 0, 10, 10, 10]])
        10
    """
    # The nodes in our graph are the start/end points of special roads and (n, n).
    # We add (0, 0) as the starting point.
    nodes = [(0, 0), (n, n)]
    for r in specialRoads:
        nodes.append((r[0], r[1]))
        nodes.append((r[2], r[3]))
    
    # Remove duplicates to optimize Dijkstra
    nodes = list(set(nodes))
    node_to_idx = {node: i for i, node in enumerate(nodes)}
    num_nodes = len(nodes)
    
    # dist[i] stores the minimum cost to reach nodes[i]
    distances = [float('inf')] * num_nodes
    start_idx = node_to_idx[(0, 0)]
    distances[start_idx] = 0
    
    # Priority queue for Dijkstra: (cost, current_node_index)
    pq = [(0, start_idx)]
    
    while pq:
        current_cost, u_idx = heapq.heappop(pq)
        
        if current_cost > distances[u_idx]:
            continue
            
        u_x, u_y = nodes[u_idx]
        
        # 1. Option: Move to any other node via a standard road (Manhattan distance)
        # This represents traveling without using any special road between these two points.
        for v_idx in range(num_nodes):
            if u_idx == v_idx:
                continue
            v_x, v_y = nodes[v_idx]
            
            # We only care about moving "forward" (increasing x or y) to avoid cycles 
            # and because moving backward is never optimal in this specific grid setup.
            if v_x >= u_x and v_y >= u_y:
                manhattan_dist = abs(v_x - u_x) + abs(v_y - u_y)
                if distances[u_idx] + manhattan_dist < distances[v_idx]:
                    distances[v_idx] = distances[u_idx] + manhattan_dist
                    heapq.heappush(pq, (distances[v_idx], v_idx))
        
        # 2. Option: Use a special road if the current node is the start of one.
        # We iterate through special roads to see if any start at (u_x, u_y).
        for r_x1, r_y1, r_x2, r_y2, r_cost in specialRoads:
            if r_x1 == u_x and r_y1 == u_y:
                # Check if the special road is actually a "forward" move
                if r_x2 >= u_x and r_y2 >= u_y:
                    v_idx = node_to_idx[(r_x2, r_y2)]
                    if distances[u_idx] + r_cost < distances[v_idx]:
                        distances[v_idx] = distances[u_idx] + r_cost
                        heapq.heappush(pq, (distances[v_idx], v_idx))
                        
    return int(distances[node_to_idx[(n, n)]])
