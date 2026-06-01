METADATA = {
    "id": 3200,
    "name": "Maximum Height of a Triangle",
    "slug": "maximum-height-of-a-triangle",
    "category": "Math",
    "aliases": [],
    "tags": ["math", "geometry"],
    "difficulty": "medium",
    "time_complexity": "O(1)",
    "space_complexity": "O(1)",
    "description": "Find the maximum possible height of a triangle given three side lengths by choosing the shortest side as the base.",
}

import math

def solve(a: int, b: int, c: int) -> float:
    """
    Calculates the maximum possible height of a triangle given three side lengths.
    
    To maximize the height, we must minimize the base. The height is calculated 
    using the area of the triangle (via Heron's formula) and the formula 
    Area = (base * height) / 2.

    Args:
        a: Length of the first side.
        b: Length of the second side.
        c: Length of the third side.

    Returns:
        The maximum height of the triangle as a float.

    Examples:
        >>> solve(3, 4, 5)
        4.0
        >>> solve(10, 10, 10)
        8.660254037844386
    """
    # Sort sides to easily identify the shortest side as the base
    sides = sorted([a, b, c])
    shortest_side = sides[0]
    
    # Calculate the semi-perimeter for Heron's formula
    semi_perimeter = (a + b + c) / 2.0
    
    # Calculate the area using Heron's formula: sqrt(s * (s-a) * (s-b) * (s-c))
    # We use max(0, ...) to prevent tiny negative numbers due to floating point precision
    area_squared = semi_perimeter * (semi_perimeter - a) * (semi_perimeter - b) * (semi_perimeter - c)
    area = math.sqrt(max(0.0, area_squared))
    
    # Since Area = (base * height) / 2, then height = (2 * Area) / base
    # To maximize height, we use the smallest side as the base
    max_height = (2.0 * area) / shortest_side
    
    return max_height
