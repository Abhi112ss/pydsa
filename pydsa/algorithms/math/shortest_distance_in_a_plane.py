METADATA = {
    "id": 612,
    "name": "Shortest Distance in a Plane",
    "slug": "shortest_distance_in_a_plane",
    "category": "Geometry",
    "aliases": [],
    "tags": ["math", "geometry"],
    "difficulty": "easy",
    "time_complexity": "O(n^2)",
    "space_complexity": "O(1)",
    "description": "Find the minimum Euclidean distance between any two points in a given list of coordinates.",
}

import math

def solve(points: list[list[float]]) -> float:
    """
    Calculates the minimum Euclidean distance between any two points in a 2D plane.

    Args:
        points: A list of points where each point is represented as [x, y].

    Returns:
        The minimum Euclidean distance found between any two distinct points.
        Returns infinity if there are fewer than 2 points.

    Examples:
        >>> solve([[0, 0], [1, 1], [2, 2]])
        1.4142135623730951
        >>> solve([[0, 0], [0, 1]])
        1.0
    """
    n = len(points)
    if n < 2:
        return float('inf')

    min_distance_sq = float('inf')

    # Iterate through all unique pairs of points
    for i in range(n):
        x1, y1 = points[i]
        for j in range(i + 1, n):
            x2, y2 = points[j]
            
            # Calculate squared Euclidean distance to avoid unnecessary sqrt calls in the loop
            dx = x1 - x2
            dy = y1 - y2
            dist_sq = dx * dx + dy * dy
            
            if dist_sq < min_distance_sq:
                min_distance_sq = dist_sq

    # Return the square root of the minimum squared distance found
    return math.sqrt(min_distance_sq)
