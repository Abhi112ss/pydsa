METADATA = {
    "id": 3047,
    "name": "Find the Largest Area of Square Inside Two Rectangles",
    "slug": "find-the-largest-area-of-square-inside-two-rectangles",
    "category": "Math",
    "aliases": [],
    "tags": ["geometry", "math"],
    "difficulty": "medium",
    "time_complexity": "O(1)",
    "space_complexity": "O(1)",
    "description": "Find the largest area of a square that can fit within the intersection of two given rectangles.",
}

def solve(rect1: list[int], rect2: list[int]) -> int:
    """
    Calculates the largest area of a square that can fit inside the intersection 
    of two rectangles.

    Args:
        rect1: A list of four integers [x1, y1, x2, y2] representing the first rectangle.
        rect2: A list of four integers [x1, y1, x2, y2] representing the second rectangle.

    Returns:
        The area of the largest square that fits in the intersection. Returns 0 if no intersection exists.

    Examples:
        >>> solve([0, 0, 2, 2], [1, 1, 3, 3])
        1
        >>> solve([0, 0, 1, 1], [2, 2, 3, 3])
        0
    """
    # Extract coordinates for clarity
    # rect = [x_start, y_start, x_end, y_end]
    rect1_x1, rect1_y1, rect1_x2, rect1_y2 = rect1
    rect2_x1, rect2_y1, rect2_x2, rect2_y2 = rect2

    # The intersection rectangle's boundaries are defined by:
    # The maximum of the starting coordinates and the minimum of the ending coordinates.
    inter_x1 = max(rect1_x1, rect2_x1)
    inter_y1 = max(rect1_y1, rect2_y1)
    inter_x2 = min(rect1_x2, rect2_x2)
    inter_y2 = min(rect1_y2, rect2_y2)

    # Calculate the width and height of the intersection rectangle
    inter_width = inter_x2 - inter_x1
    inter_height = inter_y2 - inter_y1

    # If width or height is non-positive, there is no intersection
    if inter_width <= 0 or inter_height <= 0:
        return 0

    # The largest square that fits in a rectangle has a side length 
    # equal to the minimum of the rectangle's width and height.
    side_length = min(inter_width, inter_height)

    return side_length * side_length
