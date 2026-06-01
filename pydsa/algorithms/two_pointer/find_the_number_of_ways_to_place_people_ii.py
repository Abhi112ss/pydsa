METADATA = {
    "id": 3027,
    "name": "Find the Number of Ways to Place People II",
    "slug": "find-the-number-of-ways-to-place-people-ii",
    "category": "Array",
    "aliases": [],
    "tags": ["sorting", "two_pointer", "geometry"],
    "difficulty": "hard",
    "time_complexity": "O(n^2)",
    "space_complexity": "O(1)",
    "description": "Count pairs of points that can form a rectangle containing no other points.",
}

def solve(points: list[list[int]]) -> int:
    """
    Finds the number of ways to choose two points such that they form a rectangle
    where the first point is the top-left and the second is the bottom-right,
    and no other points are inside or on the boundary of this rectangle.

    Args:
        points: A list of [x, y] coordinates.

    Returns:
        The number of valid pairs of points.

    Examples:
        >>> solve([[1, 1], [2, 2], [3, 3]])
        2
        >>> solve([[6, 2], [4, 4], [2, 6]])
        2
    """
    # Sort points primarily by x ascending.
    # For points with the same x, sort by y descending.
    # This ensures that when we pick a point as top-left, 
    # any subsequent point in the sorted list is to its right or below it.
    points.sort(key=lambda p: (p[0], -p[1]))
    
    n = len(points)
    count = 0
    
    for i in range(n):
        x1, y1 = points[i]
        
        # We need to find a point (x2, y2) such that x2 >= x1 and y2 <= y1.
        # Because of our sorting, all points j > i satisfy x2 >= x1.
        # We only need to track the maximum y-coordinate seen so far that is <= y1.
        # However, the condition is that no point is INSIDE the rectangle.
        # This means for a fixed top-left (x1, y1), as we move right (increasing x2),
        # the y2 of the bottom-right point must be the largest y seen so far that is <= y1.
        
        max_y_seen = float('-inf')
        
        for j in range(i + 1, n):
            x2, y2 = points[j]
            
            # Check if the current point can be a bottom-right corner relative to (x1, y1).
            # Condition: y2 must be <= y1.
            if y2 <= y1:
                # To ensure no point is inside the rectangle, the current y2 
                # must be strictly greater than the y-coordinate of any 
                # previously valid bottom-right point encountered in this loop.
                if y2 > max_y_seen:
                    count += 1
                    max_y_seen = y2
                    
    return count
