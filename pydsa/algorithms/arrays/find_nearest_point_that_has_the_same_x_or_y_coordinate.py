METADATA = {
    "id": 1779,
    "name": "Find Nearest Point That Has the Same X or Y Coordinate",
    "slug": "find-nearest-point-that-has-the-same-x-or-y-coordinate",
    "category": "Array",
    "aliases": [],
    "tags": ["array", "math"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the point with the minimum Manhattan distance to the origin that shares at least one coordinate with the origin.",
}

def solve(points: list[list[int]]) -> list[int]:
    """
    Finds the point with the minimum Manhattan distance to the origin (0, 0) 
    that has at least one coordinate equal to zero.

    Args:
        points: A list of points where each point is represented as [x, y].

    Returns:
        The point [x, y] that satisfies the condition and has the minimum 
        Manhattan distance.

    Examples:
        >>> solve([[1,1],[1,0],[-2,-1],[2,0]])
        [1, 0]
        >>> solve([[0,0],[1,1]])
        [0, 0]
    """
    min_distance = float('inf')
    nearest_point = [0, 0]

    for x, y in points:
        # Check if the point lies on the X-axis or Y-axis
        if x == 0 or y == 0:
            # Manhattan distance to (0,0) is |x - 0| + |y - 0|
            # Since one coordinate is 0, it simplifies to |x| + |y|
            current_distance = abs(x) + abs(y)
            
            # Update if we found a closer point
            if current_distance < min_distance:
                min_distance = current_distance
                nearest_point = [x, y]
                
    return nearest_point
