METADATA = {
    "id": 2833,
    "name": "Furthest Point From Origin",
    "slug": "furthest-point-from-origin",
    "category": "Math",
    "aliases": [],
    "tags": ["math", "arrays"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the point in a given list that is furthest from the origin (0, 0).",
}

def solve(points: list[list[int]]) -> list[int]:
    """
    Finds the point in the list that has the maximum Euclidean distance from the origin.

    To optimize, we compare the squared Euclidean distance (x^2 + y^2) instead of 
    the actual distance (sqrt(x^2 + y^2)) to avoid floating point operations 
    and unnecessary square root calculations.

    Args:
        points: A list of points where each point is represented as a list of two integers [x, y].

    Returns:
        The point [x, y] that is furthest from the origin.

    Examples:
        >>> solve([[1, 3], [-2, 2]])
        [1, 3]
        >>> solve([[1, 1], [0, 0], [2, 2]])
        [2, 2]
    """
    if not points:
        return []

    max_squared_distance = -1
    furthest_point = points[0]

    for point in points:
        x, y = point
        # Calculate squared Euclidean distance: x^2 + y^2
        current_squared_distance = x * x + y * y
        
        # Update the tracker if the current point is further than the previous maximum
        if current_squared_distance > max_squared_distance:
            max_squared_distance = current_squared_distance
            furthest_point = point

    return furthest_point
