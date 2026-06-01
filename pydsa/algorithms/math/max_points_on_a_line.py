METADATA = {
    "id": 149,
    "name": "Max Points on a Line",
    "slug": "max-points-on-a-line",
    "category": "Geometry",
    "aliases": [],
    "tags": ["geometry", "hash_map", "math"],
    "difficulty": "hard",
    "time_complexity": "O(n^2)",
    "space_complexity": "O(n)",
    "description": "Given an array of points on a 2D plane, find the maximum number of points that lie on the same straight line.",
}

import math

def solve(points: list[list[int]]) -> int:
    """
    Calculates the maximum number of points that lie on the same straight line.

    Args:
        points: A list of coordinates where points[i] = [xi, yi].

    Returns:
        The maximum number of points on a single line.

    Examples:
        >>> solve([[1,1],[2,2],[3,3]])
        3
        >>> solve([[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]])
        4
    """
    n = len(points)
    if n <= 2:
        return n

    max_points_on_line = 0

    for i in range(n):
        # Dictionary to store the frequency of slopes from the current point i
        # Key: (dx, dy) reduced by GCD to represent the slope uniquely
        # Value: count of points sharing that slope
        slopes_count: dict[tuple[int, int], int] = {}
        current_max = 0
        
        x1, y1 = points[i]

        for j in range(i + 1, n):
            x2, y2 = points[j]
            
            dx = x2 - x1
            dy = y2 - y1

            # Calculate the greatest common divisor to normalize the slope
            # This avoids floating point precision issues
            common_divisor = math.gcd(dx, dy)
            
            # Normalize the slope vector
            slope_key = (dx // common_divisor, dy // common_divisor)
            
            # Update the count for this specific slope
            slopes_count[slope_key] = slopes_count.get(slope_key, 0) + 1
            
            # Track the maximum points found for the current anchor point i
            if slopes_count[slope_key] > current_max:
                current_max = slopes_count[slope_key]

        # The total points on a line through point i is current_max + 1 (the anchor itself)
        max_points_on_line = max(max_points_on_line, current_max + 1)

    return max_points_on_line
