METADATA = {
    "id": 223,
    "name": "Rectangle Area",
    "slug": "rectangle_area",
    "category": "Math",
    "aliases": [],
    "tags": ["math", "geometry"],
    "difficulty": "medium",
    "time_complexity": "O(1)",
    "space_complexity": "O(1)",
    "description": "Compute the total area covered by two rectilinear rectangles in a 2D plane.",
}

def solve(
    ax1: int, ay1: int, ax2: int, ay2: int,
    bx1: int, by1: int, bx2: int, by2: int,
) -> int:
    """Compute the total area covered by two rectilinear rectangles.

    Each rectangle is defined by its bottom-left and top-right corners.
    The total area is the sum of both rectangle areas minus their overlap.

    Args:
        ax1: Bottom-left x-coordinate of rectangle A.
        ay1: Bottom-left y-coordinate of rectangle A.
        ax2: Top-right x-coordinate of rectangle A.
        ay2: Top-right y-coordinate of rectangle A.
        bx1: Bottom-left x-coordinate of rectangle B.
        by1: Bottom-left y-coordinate of rectangle B.
        bx2: Top-right x-coordinate of rectangle B.
        by2: Top-right y-coordinate of rectangle B.

    Returns:
        The total area covered by the two rectangles.

    Examples:
        >>> solve(-3, 0, 3, 4, 0, -1, 9, 2)
        45
        >>> solve(-2, -2, 2, 2, -2, -2, 2, 2)
        16
        >>> solve(0, 0, 0, 0, -1, -1, 1, 1)
        4
    """
    # Calculate the area of each rectangle individually.
    area_a = (ax2 - ax1) * (ay2 - ay1)
    area_b = (bx2 - bx1) * (by2 - by1)

    # Compute the overlap width and height using intersection of intervals.
    overlap_width = max(0, min(ax2, bx2) - max(ax1, bx1))
    overlap_height = max(0, min(ay2, by2) - max(ay1, by1))

    # Subtract the overlapping area to avoid double-counting.
    overlap_area = overlap_width * overlap_height

    return area_a + area_b - overlap_area