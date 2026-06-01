METADATA = {
    "id": 492,
    "name": "Construct the Rectangle",
    "slug": "construct-the-rectangle",
    "category": "Math",
    "aliases": [],
    "tags": ["math", "iteration"],
    "difficulty": "easy",
    "time_complexity": "O(sqrt(n))",
    "space_complexity": "O(1)",
    "description": "Given an integer area, construct a rectangle such that the length is the largest possible integer and the width is the smallest possible integer, where length >= width.",
}

def solve(area: int) -> list[int]:
    """
    Constructs a rectangle with the given area such that length >= width,
    length is maximized, and width is minimized.

    The strategy is to find the largest integer 'width' such that 'width' 
    is a divisor of 'area' and 'width' <= sqrt(area). This automatically 
    ensures 'length' (area / width) is the largest possible integer.

    Args:
        area: A positive integer representing the area of the rectangle.

    Returns:
        A list of two integers [length, width] where length * width == area
        and length >= width.

    Examples:
        >>> solve(1)
        [1, 1]
        >>> solve(4)
        [2, 2]
        >>> solve(8)
        [4, 2]
        >>> solve(10)
        [5, 2]
    """
    # Start searching from the integer square root downwards.
    # The first divisor we find will be the largest possible width 
    # that satisfies width <= sqrt(area), which in turn makes 
    # length = area / width the largest possible length.
    current_width = int(area**0.5)

    while current_width > 0:
        # Check if current_width is a divisor of the area
        if area % current_width == 0:
            length = area // current_width
            return [length, current_width]
        
        current_width -= 1

    # Fallback (mathematically, current_width will always hit 1)
    return [area, 1]
