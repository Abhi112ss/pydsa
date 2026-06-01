METADATA = {
    "id": 356,
    "name": "Line Reflection",
    "slug": "line-reflection",
    "category": "Math",
    "aliases": [],
    "tags": ["hash_set", "math"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Determine if there exists a vertical line such that the set of points is symmetric across it.",
}

def solve(points: list[list[int]]) -> bool:
    """
    Determines if there is a vertical line such that the set of points is symmetric.

    Args:
        points: A list of points where each point is represented as [x, y].

    Returns:
        True if a reflection line exists, False otherwise.

    Examples:
        >>> solve([[0, 0], [1, 1], [2, 2]])
        True
        >>> solve([[0, 0], [1, 1], [3, 3]])
        False
    """
    if not points:
        return True

    # Use a set of tuples for O(1) average-case lookup.
    # We store points as (x, y) to handle duplicates and facilitate symmetry checks.
    point_set = set()
    min_x = float('inf')
    max_x = float('-inf')

    for x, y in points:
        point_set.add((x, y))
        if x < min_x:
            min_x = x
        if x > max_x:
            max_x = x

    # The potential reflection line must be at the midpoint of the extreme x-coordinates.
    # To avoid floating point issues, we work with the sum (2 * midpoint).
    # If a point (x, y) is reflected across line x = S/2, the new x' is S - x.
    target_sum = min_x + max_x

    for x, y in points:
        # For every point (x, y), there must exist a point (target_sum - x, y) in the set.
        # This ensures symmetry across the vertical line x = target_sum / 2.
        if (target_sum - x, y) not in point_set:
            return False

    return True
