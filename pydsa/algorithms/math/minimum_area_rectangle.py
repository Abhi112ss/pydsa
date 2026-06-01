METADATA = {
    "id": 939,
    "name": "Minimum Area Rectangle",
    "slug": "minimum-area-rectangle",
    "category": "Geometry",
    "aliases": [],
    "tags": ["hash_map", "geometry", "hash_set"],
    "difficulty": "medium",
    "time_complexity": "O(n^2)",
    "space_complexity": "O(n)",
    "description": "Find the minimum area of a rectangle formed by four points from a given set of points in a 2D plane, where the sides are parallel to the X and Y axes.",
}

def solve(points: list[list[int]]) -> int:
    """
    Finds the minimum area of a rectangle formed by four points from the input.
    The sides of the rectangle must be parallel to the X and Y axes.

    Args:
        points: A list of [x, y] coordinates representing points in a 2D plane.

    Returns:
        The minimum area of a rectangle. Returns 0 if no such rectangle exists.

    Examples:
        >>> solve([[1,1],[1,3],[3,1],[3,3],[4,1],[4,3]])
        4
        >>> solve([[1,1],[1,3],[3,1]])
        0
    """
    # Use a set for O(1) lookup of point existence
    point_set: set[tuple[int, int]] = set()
    for x, y in points:
        point_set.add((x, y))

    min_area = float('inf')
    n = len(points)

    # Iterate through all pairs of points to treat them as potential diagonal corners
    for i in range(n):
        x1, y1 = points[i]
        for j in range(i + 1, n):
            x2, y2 = points[j]

            # To form a rectangle with sides parallel to axes, the diagonal 
            # points must not share the same x or y coordinate.
            if x1 == x2 or y1 == y2:
                continue

            # If (x1, y1) and (x2, y2) are diagonal corners, 
            # the other two corners must be (x1, y2) and (x2, y1).
            if (x1, y2) in point_set and (x2, y1) in point_set:
                # Calculate area using the absolute difference of coordinates
                current_area = abs(x1 - x2) * abs(y1 - y2)
                if current_area < min_area:
                    min_area = current_area

    return int(min_area) if min_area != float('inf') else 0
