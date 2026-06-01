METADATA = {
    "id": 1997,
    "name": "First Day Where You Have Been in All the Rooms",
    "slug": "first-day-where-you-have-been-in-all-the-rooms",
    "category": "Graphs",
    "aliases": [],
    "tags": ["graphs", "bfs", "shortest-path"],
    "difficulty": "medium",
    "time_complexity": "O(n + e)",
    "space_complexity": "O(n)",
    "description": "Find the minimum number of days to visit all rooms in a graph starting from room 0.",
}

from collections import deque

def solve(n: int, connections: list[list[int]]) -> int:
    """
    Finds the minimum number of days to visit all rooms in a graph.
    
    Each day, you can move from your current room to any room connected to it.
    The goal is to find the minimum days required to have visited every room at least once.
    This is equivalent to finding the maximum of the shortest paths from room 0 
    to all other reachable rooms.

    Args:
        n: The number of rooms.
        connections: A list of edges where connections[i] = [u, v] means 
                     there is a bidirectional path between room u and room v.

    Returns:
        The minimum number of days to visit all rooms. If not all rooms are 
        reachable, return -1.

    Examples:
        >>> solve(3, [[0, 1], [1, 2]])
        2
        >>> solve(3, [[0, 1]])
        -1
    """
    # Build adjacency list for the undirected graph
    adj: dict[int, list[int]] = {i: [] for i in range(n)}
    for u, v in connections:
        adj[u].append(v)
        adj[v].append(u)

    # distances[i] stores the minimum days to reach room i from room 0
    distances: list[int] = [-1] * n
    distances[0] = 0
    
    # BFS to find shortest path from room 0 to all other rooms
    queue: deque[int] = deque([0])
    visited_count = 1

    while queue:
        current_room = queue.popleft()
        
        for neighbor in adj[current_room]:
            if distances[neighbor] == -1:
                distances[neighbor] = distances[current_room] + 1
                visited_count += 1
                queue.append(neighbor)

    # If we haven't visited all rooms, it's impossible to visit all rooms
    if visited_count < n:
        return -1

    # The answer is the maximum distance found among all rooms
    # because we need to wait until the last room is reached.
    return max(distances)
