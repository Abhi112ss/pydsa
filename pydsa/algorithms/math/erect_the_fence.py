METADATA = {
    "id": 587,
    "name": "Erect the Fence",
    "slug": "erect-the-fence",
    "category": "Geometry",
    "aliases": [],
    "tags": ["geometry", "monotone_chain", "convex_hull"],
    "difficulty": "hard",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Find the convex hull of a set of points in a 2D plane, including points on the edges.",
}

def solve(points: list[list[int]]) -> list[list[int]]:
    """
    Finds the convex hull of a set of points using the Monotone Chain algorithm.
    Includes all points that lie on the boundary of the hull.

    Args:
        points: A list of points where each point is represented as [x, y].

    Returns:
        A list of points that form the convex hull, in any order.

    Examples:
        >>> solve([[1,1],[2,2],[2,0],[2,4],[3,3],[4,2]])
        [[1, 1], [2, 0], [4, 2], [3, 3], [2, 4], [2, 2]] (order may vary)
    """
    n = len(points)
    if n <= 2:
        return points

    # Sort points primarily by x-coordinate, secondarily by y-coordinate
    points.sort()

    def cross_product(o: list[int], a: list[int], b: list[int]) -> int:
        """
        Calculates the 2D cross product of vectors OA and OB.
        Returns a positive value if OA to OB is a counter-clockwise turn,
        negative for clockwise, and zero if collinear.
        """
        return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

    # Build the lower hull
    lower_hull = []
    for p in points:
        # Use < 0 to keep collinear points. 
        # If cross_product < 0, it means the turn is clockwise, 
        # which is invalid for a convex hull boundary.
        while len(lower_hull) >= 2 and cross_product(lower_hull[-2], lower_hull[-1], p) < 0:
            lower_hull.pop()
        lower_hull.append(p)

    # Build the upper hull
    upper_hull = []
    for p in reversed(points):
        while len(upper_hull) >= 2 and cross_product(upper_hull[-2], upper_hull[-1], p) < 0:
            upper_hull.pop()
        upper_hull.append(p)

    # Concatenate lower and upper hull to get the full boundary.
    # We use a set to handle duplicate points that appear at the ends of both hulls.
    # Converting to list of lists at the end.
    unique_hull_points = set()
    for p in lower_hull:
        unique_hull_points.add(tuple(p))
    for p in upper_hull:
        unique_hull_points.add(tuple(p))

    return [list(p) for p in unique_hull_points]
