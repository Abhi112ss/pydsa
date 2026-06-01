METADATA = {
    "id": 815,
    "name": "Bus Routes",
    "slug": "bus-routes",
    "category": "Graph",
    "aliases": [],
    "tags": ["bfs", "hash_map", "breadth-first-search"],
    "difficulty": "hard",
    "time_complexity": "O(N + sum(routes))",
    "space_complexity": "O(N + sum(routes))",
    "description": "Find the minimum number of buses to take to travel from a source stop to a destination stop.",
}

from collections import deque, defaultdict

def solve(routes: list[list[int]], source: int, target: int) -> int:
    """
    Finds the minimum number of buses required to travel from source to target.

    Args:
        routes: A list of lists where routes[i] is a list of stops on the i-th bus route.
        source: The starting stop index.
        target: The destination stop index.

    Returns:
        The minimum number of buses to take, or -1 if the target is unreachable.

    Examples:
        >>> solve([[1, 2, 7], [3, 6, 7]], 1, 6)
        2
        >>> solve([[1, 2, 7], [3, 6, 7]], 6, 7)
        1
        >>> solve([[1, 2, 7], [3, 6, 7]], 1, 9)
        -1
    """
    if source == target:
        return 0

    # Map each stop to the list of bus routes that pass through it
    stop_to_routes = defaultdict(list)
    for route_index, route in enumerate(routes):
        for stop in route:
            stop_to_routes[stop].append(route_index)

    # BFS queue stores (current_stop, bus_count)
    # However, to optimize, we BFS through bus routes rather than individual stops
    # to avoid redundant processing of stops within the same route.
    queue = deque([(source, 0)])
    
    # Keep track of visited stops and visited bus routes to prevent cycles/redundancy
    visited_stops = {source}
    visited_routes = set()

    while queue:
        current_stop, bus_count = queue.popleft()

        # For the current stop, check all bus routes passing through it
        for route_index in stop_to_routes[current_stop]:
            if route_index in visited_routes:
                continue
            
            visited_routes.add(route_index)
            
            # Explore all stops reachable via this specific bus route
            for next_stop in routes[route_index]:
                if next_stop == target:
                    return bus_count + 1
                
                if next_stop not in visited_stops:
                    visited_stops.add(next_stop)
                    queue.append((next_stop, bus_count + 1))

    return -1
