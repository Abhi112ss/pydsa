METADATA = {
    "id": 1401,
    "name": "Circle and Rectangle Overlapping",
    "slug": "circle-and-rectangle-overlapping",
    "category": "Geometry",
    "aliases": [],
    "tags": ["geometry", "math"],
    "difficulty": "medium",
    "time_complexity": "O(1)",
    "space_complexity": "O(1)",
    "description": "Determine if a circle and a rectangle overlap by finding the closest point on the rectangle to the circle's center.",
}

def solve(x_center: int, y_center: int, r: int, x1: int, y1: int, x2: int, y2: int) -> bool:
    """
    Determines if a circle and a rectangle overlap.

    The algorithm finds the point (closest_x, closest_y) within the rectangle 
    that is closest to the center of the circle. If the distance between 
    this point and the circle's center is less than or equal to the radius, 
    the shapes overlap.

    Args:
        x_center: X-coordinate of the circle's center.
        y_center: Y-coordinate of the circle's center.
        r: Radius of the circle.
        x1: Left boundary of the rectangle.
        y1: Bottom boundary of the rectangle.
        x2: Right boundary of the rectangle.
        y2: Top boundary of the rectangle.

    Returns:
        True if the circle and rectangle overlap, False otherwise.

    Examples:
        >>> solve(1, 1, 1, 0, 0, 2, 2)
        True
        >>> solve(1, 1, 1, 2, 2, 3, 3)
        False
    """
    # Find the closest x-coordinate on the rectangle to the circle's center.
    # If center is left of rectangle, closest is x1.
    # If center is right of rectangle, closest is x2.
    # Otherwise, the center's x is already within the rectangle's x-range.
    closest_x = max(x1, min(x_center, x2))

    # Find the closest y-coordinate on the rectangle to the circle's center.
    # If center is below rectangle, closest is y1.
    # If center is above rectangle, closest is y2.
    # Otherwise, the center's y is already within the rectangle's y-range.
    closest_y = max(y1, min(y_center, y2))

    # Calculate the squared Euclidean distance between the circle's center 
    # and the closest point found above.
    distance_squared = (x_center - closest_x) ** 2 + (y_center - closest_y) ** 2

    # The shapes overlap if the distance is less than or equal to the radius.
    # We compare squared distance to squared radius to avoid expensive sqrt() calls.
    return distance_squared <= r ** 2
