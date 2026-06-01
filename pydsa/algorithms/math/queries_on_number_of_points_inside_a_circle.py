METADATA = {
    "id": 1828,
    "name": "Queries on Number of Points Inside a Circle",
    "slug": "queries-on-number-of-points-inside-a-circle",
    "category": "Geometry",
    "aliases": [],
    "tags": ["geometry", "sorting", "math"],
    "difficulty": "medium",
    "time_complexity": "O(n * q)",
    "space_complexity": "O(1)",
    "description": "Given a set of points and queries consisting of a center and a radius, return the number of points inside each circle.",
}

def solve(points: list[list[int]], queries: list[list[int]]) -> list[int]:
    """
    Calculates the number of points inside a circle for each query.

    A point (px, py) is inside a circle with center (cx, cy) and radius r 
    if the Euclidean distance between them is less than or equal to r.
    To avoid floating point precision issues, we compare the squared distance 
    with the squared radius: (px - cx)^2 + (py - cy)^2 <= r^2.

    Args:
        points: A list of [x, y] coordinates representing points.
        queries: A list of [x, y, r] representing circle centers and radii.

    Returns:
        A list of integers where each integer is the count of points inside 
        the corresponding query circle.

    Examples:
        >>> solve([[1,1],[2,2]], [[0,0,1],[0,0,2]])
        [0, 1]
    """
    results = []

    for center_x, center_y, radius in queries:
        count = 0
        # Pre-calculate squared radius to avoid sqrt() and floating point errors
        radius_squared = radius * radius
        
        for point_x, point_y in points:
            # Calculate squared Euclidean distance
            dx = point_x - center_x
            dy = point_y - center_y
            dist_squared = dx * dx + dy * dy
            
            # Check if the point is within the circle boundary
            if dist_squared <= radius_squared:
                count += 1
        
        results.append(count)

    return results
