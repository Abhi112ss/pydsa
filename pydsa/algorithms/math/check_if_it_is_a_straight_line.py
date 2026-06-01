METADATA = {
    "id": 1232,
    "name": "Check If It Is a Straight Line",
    "slug": "check-if-it-is-a-straight-line",
    "category": "Math",
    "aliases": [],
    "tags": ["math", "geometry"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Determine if a given set of coordinates forms a straight line.",
}

def solve(coordinates: list[list[int]]) -> bool:
    """
    Determines if the given points lie on a single straight line.

    The algorithm uses the property of slopes. For three points (x0, y0), (x1, y1), 
    and (xi, yi) to be collinear, the slope between (x0, y0) and (x1, y1) must 
    equal the slope between (x0, y0) and (xi, yi).
    
    To avoid division by zero (vertical lines), we use the cross-multiplication 
    form of the slope equation:
    (y1 - y0) / (x1 - x0) == (yi - y0) / (xi - x0)
    becomes:
    (y1 - y0) * (xi - x0) == (yi - y0) * (x1 - x0)

    Args:
        coordinates: A list of [x, y] integer pairs.

    Returns:
        True if the points form a straight line, False otherwise.

    Examples:
        >>> solve([[1, 2], [2, 3], [3, 4], [4, 5]])
        True
        >>> solve([[1, 2], [2, 3], [3, 4], [4, 6]])
        False
    """
    if len(coordinates) <= 2:
        return True

    # Get the initial differences to define the reference slope
    x0, y0 = coordinates[0]
    x1, y1 = coordinates[1]
    
    delta_x = x1 - x0
    delta_y = y1 - y0

    # Iterate through the rest of the points starting from the third point
    for i in range(2, len(coordinates)):
        xi, yi = coordinates[i]
        
        # Calculate differences for the current point relative to the first point
        current_delta_x = xi - x0
        current_delta_y = yi - y0

        # Use cross-multiplication to check if slopes are equal:
        # delta_y / delta_x == current_delta_y / current_delta_x
        if delta_y * current_delta_x != current_delta_y * delta_x:
            return False

    return True
