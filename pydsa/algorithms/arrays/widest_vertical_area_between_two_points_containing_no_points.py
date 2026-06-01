METADATA = {
    "id": 1637,
    "name": "Widest Vertical Area Between Two Points Containing No Points",
    "slug": "widest-vertical-area-between-two-points-containing-no-points",
    "category": "Array",
    "aliases": [],
    "tags": ["sorting", "arrays"],
    "difficulty": "easy",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(1)",
    "description": "Find the maximum distance between two adjacent x-coordinates in a set of points.",
}

def solve(points: list[list[int]]) -> int:
    """
    Calculates the widest vertical area between two points that contains no other points.

    Args:
        points: A list of points where each point is represented as [x, y].

    Returns:
        The maximum distance between two adjacent x-coordinates.

    Examples:
        >>> solve([[1,1],[3,2],[3,3]])
        2
        >>> solve([[1,1],[2,2],[3,3]])
        1
    """
    # Extract only the x-coordinates as the y-coordinates do not affect vertical width
    x_coordinates = [point[0] for point in points]
    
    # Sort the x-coordinates to easily find adjacent points
    x_coordinates.sort()
    
    max_width = 0
    
    # Iterate through the sorted list and find the maximum gap between neighbors
    for i in range(len(x_coordinates) - 1):
        current_gap = x_coordinates[i + 1] - x_coordinates[i]
        if current_gap > max_width:
            max_width = current_gap
            
    return max_width
