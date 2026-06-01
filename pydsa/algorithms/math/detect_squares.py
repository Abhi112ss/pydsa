METADATA = {
    "id": 2013,
    "name": "Detect Squares",
    "slug": "detect-squares",
    "category": "Hash Table",
    "aliases": [],
    "tags": ["hash_map", "math", "geometry"],
    "difficulty": "medium",
    "time_complexity": "O(n^2)",
    "space_complexity": "O(n)",
    "description": "Given a list of points, count the number of axis-aligned squares that can be formed.",
}

def solve(points: list[list[int]]) -> int:
    """
    Counts the number of axis-aligned squares that can be formed from the given points.

    Args:
        points: A list of [x, y] coordinates representing points on a 2D plane.

    Returns:
        The total number of axis-aligned squares found.

    Examples:
        >>> solve([[1,1],[2,2],[2,0],[1,0],[2,1]])
        1
        >>> solve([[1,1],[1,0],[1,-1],[0,1],[0,0],[0,-1],[-1,1],[-1,0],[-1,-1]])
        4
    """
    # Use a set of tuples for O(1) lookup of point existence
    point_set: set[tuple[int, int]] = set()
    for x, y in points:
        point_set.add((x, y))

    square_count = 0

    # Iterate through all pairs of points to treat them as a potential diagonal
    # A diagonal is defined by two points (x1, y1) and (x2, y2)
    for i in range(len(points)):
        x1, y1 = points[i]
        for j in range(i + 1, len(points)):
            x2, y2 = points[j]

            # To form an axis-aligned square via a diagonal:
            # 1. The points must not be on the same horizontal or vertical line.
            # 2. The absolute difference in x must equal the absolute difference in y.
            dx = abs(x1 - x2)
            dy = abs(y1 - y2)

            if dx == dy and dx > 0:
                # If (x1, y1) and (x2, y2) are diagonal corners, 
                # the other two corners must be (x1, y2) and (x2, y1).
                if (x1, y2) in point_set and (x2, y1) in point_set:
                    square_count += 1

    # Each square is counted twice because each square has two diagonals.
    # We divide by 2 to get the unique count.
    return square_count // 2
