METADATA = {
    "id": 1924,
    "name": "Erect the Fence II",
    "slug": "erect-the-fence-ii",
    "category": "Geometry",
    "aliases": [],
    "tags": ["geometry", "convex_hull", "monotone_chain"],
    "difficulty": "hard",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Find the points that form the convex hull of a given set of points, including points on the edges.",
}

def solve(points: list[list[int]]) -> list[list[int]]:
    """
    Finds the points that form the convex hull of a given set of points.
    This implementation uses the Monotone Chain algorithm modified to include 
    collinear points on the boundary.

    Args:
        points: A list of [x, y] coordinates representing points in a 2D plane.

    Returns:
        A list of [x, y] coordinates that form the convex hull, in any order.

    Examples:
        >>> solve([[1,1],[2,2],[2,0],[2,4],[3,3],[4,2]])
        [[1, 1], [2, 0], [4, 2], [3, 3], [2, 4], [2, 2]] (order may vary)
    """
    n = len(points)
    if n <= 2:
        return points

    # Sort points lexicographically by x, then by y
    points.sort()

    def cross_product(o: list[int], a: list[int], b: list[int]) -> int:
        """
        Calculates the 2D cross product of vectors OA and OB.
        Returns a positive value if O->A->B is a counter-clockwise turn,
        negative for clockwise, and zero if collinear.
        """
        return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

    # Build the lower hull
    lower = []
    for p in points:
        # While the last two points and the current point make a clockwise turn,
        # pop the last point. We use < 0 to keep collinear points (where cross product == 0).
        while len(lower) >= 2 and cross_product(lower[-2], lower[-1], p) < 0:
            lower.pop()
        lower.append(p)

    # Build the upper hull
    upper = []
    for p in reversed(points):
        # While the last two points and the current point make a clockwise turn,
        # pop the last point.
        while len(upper) >= 2 and cross_product(upper[-2], upper[-1], p) < 0:
            upper.pop()
        upper.append(p)

    # Concatenate lower and upper hull to get the full boundary.
    # We use a set to remove duplicates caused by the start and end points of the hulls.
    # Converting to list of lists at the end.
    unique_hull_points = set()
    for p in lower:
        unique_hull_points.add(tuple(p))
    for p in upper:
        unique_hull_points.add(tuple(p))

    return [list(p) for p in unique_hull_points]
