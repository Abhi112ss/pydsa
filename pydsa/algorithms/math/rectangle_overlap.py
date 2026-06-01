METADATA = {
    "id": 836,
    "name": "Rectangle Overlap",
    "slug": "rectangle_overlap",
    "category": "Geometry",
    "aliases": [],
    "tags": ["geometry", "math"],
    "difficulty": "easy",
    "time_complexity": "O(1)",
    "space_complexity": "O(1)",
    "description": "Determine if two axis-aligned rectangles overlap.",
}


def solve() -> None:
    """Read two rectangles and output whether they overlap.

    Args:
        None. The function reads from standard input. Each of the first two
        lines should contain four integers ``x1 y1 x2 y2`` representing the
        bottom‑left and top‑right corners of a rectangle.

    Returns:
        None. Prints ``true`` if the rectangles overlap, otherwise ``false``.

    Examples:
        >>> # Input
        >>> # 0 0 2 2
        >>> # 1 1 3 3
        >>> # Output
        >>> # true
        >>> # Explanation: The rectangles share a common area.
        >>> # Input
        >>> # 0 0 1 1
        >>> # 1 0 2 1
        >>> # Output
        >>> # false
        >>> # Explanation: They only touch at the edge, which is not considered overlap.
    """
    import sys

    # Read and parse the two rectangle definitions
    lines = [line.strip() for line in sys.stdin.readlines() if line.strip()]
    if len(lines) < 2:
        return
    rect1 = [int(value) for value in lines[0].split()]
    rect2 = [int(value) for value in lines[1].split()]

    # Unpack coordinates for readability
    left1, bottom1, right1, top1 = rect1
    left2, bottom2, right2, top2 = rect2

    # Check overlap on both axes: intervals must intersect with positive length
    x_overlap = left1 < right2 and left2 < right1
    y_overlap = bottom1 < top2 and bottom2 < top1

    result = x_overlap and y_overlap
    print("true" if result else "false")
