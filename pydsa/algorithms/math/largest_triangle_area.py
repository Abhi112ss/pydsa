METADATA = {
    "id": 812,
    "name": "Largest Triangle Area",
    "slug": "largest_triangle_area",
    "category": "Geometry",
    "aliases": [],
    "tags": ["geometry", "brute_force"],
    "difficulty": "medium",
    "time_complexity": "O(n^3)",
    "space_complexity": "O(1)",
    "description": "Find the maximum area of a triangle formed by any three points.",
}


def solve(points: list[list[int]]) -> float:
    """Calculate the largest possible triangle area from a set of points.

    Args:
        points: A list of [x, y] integer coordinates representing distinct points.

    Returns:
        The maximum triangle area as a float. Returns 0.0 if fewer than three points are provided.

    Examples:
        >>> solve([[0,0],[0,1],[1,0],[0,2],[2,0]])
        2.0
        >>> solve([[1,0],[0,0],[0,1]])
        0.5
    """
    number_of_points = len(points)
    if number_of_points < 3:
        return 0.0

    max_area = 0.0
    # Iterate over all unordered triplets of points (i < j < k)
    for i in range(number_of_points - 2):
        x1, y1 = points[i]
        for j in range(i + 1, number_of_points - 1):
            x2, y2 = points[j]
            for k in range(j + 1, number_of_points):
                x3, y3 = points[k]
                # Shoelace formula for the area of a triangle
                double_area = abs(
                    x1 * (y2 - y3) +
                    x2 * (y3 - y1) +
                    x3 * (y1 - y2)
                )
                current_area = double_area / 2.0
                if current_area > max_area:
                    max_area = current_area
    return max_area