METADATA = {
    "id": 3376,
    "name": "Minimum Time to Break Locks I",
    "slug": "minimum-time-to-break-locks-i",
    "category": "Graph",
    "aliases": [],
    "tags": ["bfs", "graphs", "shortest-path"],
    "difficulty": "medium",
    "time_complexity": "O(N)",
    "space_complexity": "O(N)",
    "description": "Find the minimum time to reach a target lock starting from an initial lock using BFS.",
}

from collections import deque

def solve(n: int, connections: list[list[int]], start: int, target: int) -> int:
    """
    Finds the minimum number of steps to reach the target lock from the start lock.

    Args:
        n: The total number of locks (labeled 1 to n).
        connections: A list of pairs [u, v] representing a connection between lock u and lock v.
        start: The starting lock index.
        target: The target lock index.

    Returns:
        The minimum number of steps to reach the target, or -1 if the target is unreachable.

    Examples:
        >>> solve(4, [[1, 2], [2, 3], [3, 4]], 1, 4)
        3
        >>> solve(4, [[1, 2], [2, 3], [3, 4]], 1, 1)
        0
        >>> solve(3, [[1, 2]], 1, 3)
        -1
    """
    if start == target:
        return 0

    # Build adjacency list for the graph
    adj: dict[int, list[int]] = {i: [] for i in range(1, n + 1)}
    for u, v in connections:
        adj[u].append(v)
        adj[v].append(u)

    # BFS initialization
    # queue stores tuples of (current_node, current_distance)
    queue: deque[tuple[int, int]] = deque([(start, 0)])
    visited: set[int] = {start}

    while queue:
        current_node, distance = queue.popleft()

        # Explore all connected locks
        for neighbor in adj[current_node]:
            if neighbor == target:
                return distance + 1
            
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, distance + 1))

    return -1
