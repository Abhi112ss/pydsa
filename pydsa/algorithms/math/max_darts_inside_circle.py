METADATA = {
    "id": 1453,
    "name": "Maximum Number of Darts Inside of a Circular Dartboard",
    "slug": "maximum-number-of-darts-inside-of-a-circular-dartboard",
    "category": "Geometry",
    "aliases": [],
    "tags": ["geometry", "math", "math-geometry"],
    "difficulty": "hard",
    "time_complexity": "O(n^3)",
    "space_complexity": "O(1)",
    "description": "Find the maximum number of points that can be enclosed by a circle of a given radius.",
}

import math

def solve(points: list[list[int]], radius: int) -> int:
    """
    Finds the maximum number of points that can be enclosed by a circle of a given radius.
    
    The optimal circle will either have one point at its center (if n=1) or 
    at least two points on its boundary. We iterate through all pairs of points 
    to find potential centers of circles that have these two points on their boundary.

    Args:
        points: A list of [x, y] coordinates representing dart positions.
        radius: The radius of the circular dartboard.

    Returns:
        The maximum number of points that can be contained within the circle.

    Examples:
        >>> solve([[0,0],[0,2],[2,0],[2,2]], 1)
        2
        >>> solve([[0,0],[1,1],[2,2]], 1)
        2
    """
    n = len(points)
    if n <= 1:
        return n

    max_points = 1
    diameter_sq = (2 * radius) ** 2
    # Use a small epsilon for floating point comparisons
    epsilon = 1e-7

    for i in range(n):
        for j in range(i + 1, n):
            x1, y1 = points[i]
            x2, y2 = points[j]
            
            # Calculate squared distance between points i and j
            dist_sq = (x1 - x2)**2 + (y1 - y2)**2
            
            # If distance between points is greater than diameter, 
            # no circle of given radius can pass through both.
            if dist_sq > diameter_sq + epsilon:
                continue
            
            # Calculate the center(s) of the circle(s) that have points i and j on the boundary.
            # Midpoint of the chord
            mid_x = (x1 + x2) / 2
            mid_y = (y1 + y2) / 2
            
            # Distance from midpoint to the center of the circle
            # h^2 + (dist/2)^2 = radius^2
            h = math.sqrt(max(0, radius**2 - dist_sq / 4))
            
            # Unit vector perpendicular to the chord (x1,y1)-(x2,y2)
            # Chord vector: (dx, dy) = (x2-x1, y2-y1)
            # Perpendicular vector: (-dy, dx)
            dx = x2 - x1
            dy = y2 - y1
            chord_len = math.sqrt(dist_sq)
            
            # There are two possible centers for the circle passing through i and j
            # Center 1
            c1_x = mid_x - h * dy / chord_len
            c1_y = mid_y + h * dx / chord_len
            
            # Center 2
            c2_x = mid_x + h * dy / chord_len
            c2_y = mid_y - h * dx / chord_len
            
            # Check both candidate centers
            for cx, cy in [(c1_x, c1_y), (c2_x, c2_y)]:
                count = 0
                for k in range(n):
                    # Check if point k is inside the circle using squared distance
                    # to avoid unnecessary sqrt calls
                    pk_x, pk_y = points[k]
                    d_sq = (pk_x - cx)**2 + (pk_y - cy)**2
                    if d_sq <= radius**2 + epsilon:
                        count += 1
                
                if count > max_points:
                    max_points = count
                    
    return max_points
