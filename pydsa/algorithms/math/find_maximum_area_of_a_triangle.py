METADATA = {
    "id": 3588,
    "name": "Find Maximum Area of a Triangle",
    "slug": "find-maximum-area-of-a-triangle",
    "category": "Geometry",
    "aliases": [],
    "tags": ["math", "geometry", "convex-hull"],
    "difficulty": "medium",
    "time_complexity": "O(n^2)",
    "space_complexity": "O(n)",
    "description": "Find the maximum area of a triangle formed by any three points from a given set of points.",
}

def solve(points: list[list[int]]) -> float:
    """
    Finds the maximum area of a triangle that can be formed by any three points 
    from the given list. Uses the Convex Hull to optimize the search space.

    Args:
        points: A list of [x, y] coordinates representing points in a 2D plane.

    Returns:
        The maximum area of a triangle formed by three points.

    Examples:
        >>> solve([[0,0],[0,1],[1,0],[1,1],[0.5,0.5]])
        0.5
        >>> solve([[0,0],[1,0],[0,1]])
        0.5
    """
    n = len(points)
    if n < 3:
        return 0.0

    # Step 1: Compute the Convex Hull using Monotone Chain algorithm.
    # The vertices of the maximum area triangle must lie on the convex hull.
    points.sort()

    def cross_product(o: list[int], a: list[int], b: list[int]) -> int:
        return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

    # Build lower hull
    lower_hull = []
    for p in points:
        while len(lower_hull) >= 2 and cross_product(lower_hull[-2], lower_hull[-1], p) <= 0:
            lower_hull.pop()
        lower_hull.append(p)

    # Build upper hull
    upper_hull = []
    for p in reversed(points):
        while len(upper_hull) >= 2 and cross_product(upper_hull[-2], upper_hull[-1], p) <= 0:
            upper_hull.pop()
        upper_hull.append(p)

    # Concatenate lower and upper hull to get the full hull (remove last point of each because it's repeated)
    hull = lower_hull[:-1] + upper_hull[:-1]
    m = len(hull)

    if m < 3:
        # If hull has fewer than 3 points, the points are collinear
        return 0.0

    max_area_twice = 0

    # Step 2: Find the maximum area triangle using the hull points.
    # While O(m^3) is possible, we can optimize to O(m^2) using a rotating calipers-style approach.
    # For every pair of points (i, j), the point k that maximizes the area moves monotonically.
    for i in range(m):
        k = (i + 2) % m
        for j in range(i + 1, m):
            # Area of triangle (i, j, k) is 0.5 * |cross_product(i, j, k)|
            # We maximize 2 * Area to avoid floating point issues during comparison
            
            # Current area with point k
            current_area_twice = abs(cross_product(hull[i], hull[j], hull[k]))
            
            # Move k forward as long as the area increases
            while True:
                next_k = (k + 1) % m
                if next_k == i or next_k == j:
                    break
                next_area_twice = abs(cross_product(hull[i], hull[j], hull[next_k]))
                if next_area_twice >= current_area_twice:
                    current_area_twice = next_area_twice
                    k = next_k
                else:
                    break
            
            if current_area_twice > max_area_twice:
                max_area_twice = current_area_twice

    return max_area_twice / 2.0
