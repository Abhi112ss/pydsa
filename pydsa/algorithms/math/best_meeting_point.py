METADATA = {
    "id": 296,
    "name": "Best Meeting Point",
    "slug": "best_meeting_point",
    "category": "Matrix",
    "aliases": [],
    "tags": ["sorting", "median", "matrix"],
    "difficulty": "hard",
    "time_complexity": "O(m*n)",
    "space_complexity": "O(m*n)",
    "description": "Find a point in a grid that minimizes the total Manhattan distance to all given points.",
}

def solve(points: list[list[int]]) -> list[int]:
    """
    Finds the optimal meeting point that minimizes the sum of Manhattan distances.
    
    The Manhattan distance between (x1, y1) and (x2, y2) is |x1 - x2| + |y1 - y2|.
    To minimize the sum of |x_i - x_target| + |y_i - y_target|, we can minimize 
    the x and y components independently. The value that minimizes the sum of 
    absolute differences is the median of the coordinates.

    Args:
        points: A list of points where each point is [x, y].

    Returns:
        A list [x, y] representing the optimal meeting point.

    Examples:
        >>> solve([[1, 1], [4, 4]])
        [1, 1]
        >>> solve([[1, 1], [4, 4], [5, 5]])
        [4, 4]
    """
    if not points:
        return []

    # Extract x and y coordinates into separate lists
    x_coords = []
    y_coords = []
    for x, y in points:
        x_coords.append(x)
        y_coords.append(y)

    # Sort coordinates to find the median
    x_coords.sort()
    y_coords.sort()

    # The median minimizes the sum of absolute differences.
    # For an even number of points, any value between the two middle 
    # elements (inclusive) works. We pick the lower median for consistency.
    n = len(points)
    median_x = x_coords[(n - 1) // 2]
    median_y = y_coords[(n - 1) // 2]

    return [median_x, median_y]
