METADATA = {
    "id": 2687,
    "name": "Bikes Last Time Used",
    "slug": "bikes-last-time-used",
    "category": "Hash Table",
    "aliases": [],
    "tags": ["hash_map", "sorting"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Find the last time each bike was used on a specific route.",
}

def solve(rides: list[list[int]]) -> list[list[int]]:
    """
    Finds the last time each bike was used on a specific route.

    Args:
        rides: A list of lists where each inner list contains [user, bike, route, time].

    Returns:
        A list of lists where each inner list contains [bike, route, last_time],
        sorted by bike ID, then by route ID.

    Examples:
        >>> solve([[1, 1, 1, 1], [2, 2, 2, 2], [1, 2, 1, 3], [2, 1, 1, 4]])
        [[1, 1, 4], [2, 1, 3], [2, 2, 2]]
    """
    # Map key: (bike, route) -> value: max_time
    # Using a dictionary to store the latest timestamp for each unique bike-route pair
    last_used_map: dict[tuple[int, int], int] = {}

    for user, bike, route, time in rides:
        key = (bike, route)
        # If the bike-route pair is new or we found a later time, update the map
        if key not in last_used_map or time > last_used_map[key]:
            last_used_map[key] = time

    # Transform the dictionary into the required list format: [bike, route, last_time]
    result: list[list[int]] = []
    for (bike, route), last_time in last_used_map.items():
        result.append([bike, route, last_time])

    # Sort the result primarily by bike ID and secondarily by route ID
    result.sort(key=lambda x: (x[0], x[1]))

    return result
