METADATA = {
    "id": 593,
    "name": "Valid Square",
    "slug": "valid-square",
    "category": "Geometry",
    "aliases": [],
    "tags": ["geometry", "hash_set", "math"],
    "difficulty": "medium",
    "time_complexity": "O(1)",
    "space_complexity": "O(1)",
    "description": "Determine if four given points form a valid square.",
}

def solve(points: list[list[int]]) -> bool:
    """
    Determines if four points in a 2D plane form a valid square.

    A valid square must have four equal sides and two equal diagonals. 
    Crucially, the diagonal length must be greater than the side length 
    (to avoid the case where all points are the same).

    Args:
        points: A list of four points, where each point is a list of two integers [x, y].

    Returns:
        True if the points form a valid square, False otherwise.

    Examples:
        >>> solve([[0,0],[1,1],[1,0],[0,1]])
        True
        >>> solve([[0,0],[1,1],[1,0],[0,0]])
        False
    """
    def get_squared_distance(p1: list[int], p2: list[int]) -> int:
        """Calculates the squared Euclidean distance to avoid floating point issues."""
        return (p1[0] - p2[0])**2 + (p1[1] - p2[1])**2

    # Calculate squared distances between all possible pairs of points (6 pairs total)
    distances = []
    for i in range(4):
        for j in range(i + 1, 4):
            distances.append(get_squared_distance(points[i], points[j]))

    # A square must have exactly two distinct distances: 
    # 4 sides (shorter) and 2 diagonals (longer).
    # We use a set to find unique distance values.
    unique_distances = sorted(list(set(distances)))

    # Validation criteria:
    # 1. There must be exactly 2 unique distances (side and diagonal).
    # 2. The distance cannot be 0 (points must be distinct).
    # 3. In a square, there are 4 sides and 2 diagonals. 
    #    Since we sorted unique_distances, unique_distances[0] is side^2 and [1] is diag^2.
    if len(unique_distances) != 2:
        return False

    side_sq = unique_distances[0]
    diag_sq = unique_distances[1]

    # Check if the side length is non-zero and if the Pythagorean theorem holds (a^2 + a^2 = c^2)
    # For a square with side 's', the diagonal is s * sqrt(2), so diag^2 = 2 * s^2.
    return side_sq > 0 and (2 * side_sq == diag_sq)
