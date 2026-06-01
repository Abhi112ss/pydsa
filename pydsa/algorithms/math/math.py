METADATA = {
    "id": 1037,
    "name": "Valid Boomerang",
    "slug": "valid_boomerang",
    "category": "Geometry",
    "aliases": [],
    "tags": ["geometry", "math"],
    "difficulty": "easy",
    "time_complexity": "O(1)",
    "space_complexity": "O(1)",
    "description": "Determine if three given points form a non‑collinear boomerang.",
}


def solve(points: list[list[int]]) -> bool:
    """Determine whether three points form a valid boomerang.

    Args:
        points: A list of three points, each represented as a list of two integers
                [x, y].

    Returns:
        True if the three points are not collinear (i.e., they form a valid boomerang),
        otherwise False.

    Examples:
        >>> solve([[1,1],[2,3],[3,2]])
        True
        >>> solve([[1,1],[2,2],[3,3]])
        False
    """
    # Unpack the three points for clarity
    (x1, y1), (x2, y2), (x3, y3) = points

    # Compute the cross product of vectors (p2 - p1) and (p3 - p1)
    # If the cross product is zero, the points are collinear.
    cross_product = (x2 - x1) * (y3 - y1) - (y2 - y1) * (x3 - x1)

    return cross_product != 0