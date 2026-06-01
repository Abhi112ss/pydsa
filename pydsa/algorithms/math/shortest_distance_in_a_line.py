METADATA = {
    "id": 613,
    "name": "Shortest Distance in a Line",
    "slug": "shortest_distance_in_a_line",
    "category": "Geometry",
    "aliases": [],
    "tags": ["sorting", "math"],
    "difficulty": "easy",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(1)",
    "description": "Find the minimum distance between any two points on a line.",
}


def solve(points: list[int]) -> int:
    """Calculate the shortest distance between any two points on a line.

    Args:
        points: A list of integer coordinates representing points on a number line.

    Returns:
        The smallest absolute difference between any two distinct points. If the list
        contains fewer than two points, returns 0.

    Examples:
        >>> solve([1, 5, 3, 19, 18, 25])
        1
        >>> solve([30, 10, 20])
        10
        >>> solve([5])
        0
    """
    # If there are fewer than two points, no distance can be computed.
    if len(points) < 2:
        return 0

    # Sort the points in-place to enable linear scan of adjacent differences.
    points.sort()

    # Initialize the minimum distance with the first adjacent pair.
    minimum_distance = points[1] - points[0]

    # Scan through sorted points, updating the minimum distance.
    for index in range(1, len(points) - 1):
        current_distance = points[index + 1] - points[index]
        if current_distance < minimum_distance:
            minimum_distance = current_distance

    return minimum_distance