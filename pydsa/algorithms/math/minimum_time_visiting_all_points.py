METADATA = {
    "id": 1266,
    "name": "Minimum Time Visiting All Points",
    "slug": "minimum-time-visiting-all-points",
    "category": "Geometry",
    "aliases": [],
    "tags": ["geometry", "arrays"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Calculate the minimum time to visit all points in a given order where movement can be horizontal, vertical, or diagonal.",
}

def solve(points: list[list[int]]) -> int:
    """
    Calculates the minimum time to visit all points in the given order.
    
    The movement allows for horizontal, vertical, and diagonal steps. 
    In a 2D grid, the time taken to move from (x1, y1) to (x2, y2) 
    is the Chebyshev distance: max(|x2 - x1|, |y2 - y1|).

    Args:
        points: A list of coordinates where each coordinate is [x, y].

    Returns:
        The minimum total time required to visit all points in sequence.

    Examples:
        >>> solve([[1,1],[3,4],[1,0]])
        6
        >>> solve([[1,1],[5,5]])
        4
    """
    total_time = 0
    
    # Iterate through the points, calculating distance between consecutive pairs
    for i in range(len(points) - 1):
        current_point = points[i]
        next_point = points[i + 1]
        
        # Calculate absolute differences for both dimensions
        delta_x = abs(next_point[0] - current_point[0])
        delta_y = abs(next_point[1] - current_point[1])
        
        # The Chebyshev distance is the maximum of the two differences
        # because diagonal moves cover both x and y simultaneously.
        total_time += max(delta_x, delta_y)
        
    return total_time
