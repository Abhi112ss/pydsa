METADATA = {
    "id": 1184,
    "name": "Distance Between Bus Stops",
    "slug": "distance_between_bus_stops",
    "category": "array",
    "aliases": [],
    "tags": ["array", "prefix_sum"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Compute the shortest distance between two bus stops on a circular route.",
}


def solve(distance: list[int], start: int, destination: int) -> int:
    """Return the minimum distance between two bus stops on a circular route.

    Args:
        distance: A list where distance[i] is the distance between stop i and (i+1) % n.
        start: Index of the starting bus stop.
        destination: Index of the destination bus stop.

    Returns:
        The shortest possible travel distance between start and destination.

    Examples:
        >>> solve([1,2,3,4], 0, 1)
        1
        >>> solve([1,2,3,4], 0, 2)
        3
        >>> solve([1,2,3,4], 3, 1)
        3
    """
    total_distance = sum(distance)  # total length of the circular route

    # Ensure we always move clockwise from start to destination
    if start <= destination:
        clockwise_distance = sum(distance[i] for i in range(start, destination))
    else:
        # wrap around the end of the list
        clockwise_distance = sum(distance[i] for i in range(start, len(distance)))
        clockwise_distance += sum(distance[i] for i in range(0, destination))

    # The counter‑clockwise distance is the remainder of the total distance
    counter_clockwise_distance = total_distance - clockwise_distance

    # Return the shorter of the two possible paths
    return clockwise_distance if clockwise_distance < counter_clockwise_distance else counter_clockwise_distance