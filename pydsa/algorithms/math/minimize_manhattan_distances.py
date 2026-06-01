METADATA = {
    "id": 3102,
    "name": "Minimize Manhattan Distances",
    "slug": "minimize-manhattan-distances",
    "category": "Math",
    "aliases": [],
    "tags": ["median", "math", "greedy"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Find the minimum possible sum of Manhattan distances from a point to a given set of points by choosing the optimal coordinates.",
}

def solve(points: list[list[int]]) -> int:
    """
    Calculates the minimum sum of Manhattan distances from a single point 
    to a set of given points.

    The Manhattan distance between (x1, y1) and (x2, y2) is |x1 - x2| + |y1 - y2|.
    To minimize the sum of distances in a single dimension, the optimal 
    coordinate is the median of the coordinates in that dimension.

    Args:
        points: A list of points where each point is a list of two integers [x, y].

    Returns:
        The minimum sum of Manhattan distances.

    Examples:
        >>> solve([[1, 1], [2, 2], [3, 3]])
        4
        >>> solve([[1, 1], [1, 1]])
        0
    """
    if not points:
        return 0

    x_coords = []
    y_coords = []

    # Separate the coordinates into two independent dimensions
    for x, y in points:
        x_coords.append(x)
        y_coords.append(y)

    # Sort coordinates to find the median
    x_coords.sort()
    y_coords.sort()

    n = len(points)
    # The median minimizes the sum of absolute differences.
    # For an even number of elements, any value between the two middle 
    # elements (inclusive) works. We pick the index n // 2.
    median_x = x_coords[n // 2]
    median_y = y_coords[n // 2]

    total_distance = 0
    # Calculate the sum of absolute differences for both dimensions
    for x in x_coords:
        total_distance += abs(x - median_x)
    for y in y_coords:
        total_distance += abs(y - median_y)

    return total_distance
