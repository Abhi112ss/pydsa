METADATA = {
    "id": 610,
    "name": "Triangle Judgement",
    "slug": "triangle_judgement",
    "category": "Database",
    "aliases": [],
    "tags": ["math_logic", "conditional"],
    "difficulty": "easy",
    "time_complexity": "O(1)",
    "space_complexity": "O(1)",
    "description": "Determine if three side lengths can form a valid triangle using the triangle inequality theorem.",
}

def solve(x: int, y: int, z: int) -> str:
    """Determine if three side lengths can form a valid triangle.

    Applies the triangle inequality theorem: the sum of any two sides must be
    strictly greater than the third side.

    Args:
        x: Length of the first side.
        y: Length of the second side.
        z: Length of the third side.

    Returns:
        'Yes' if the sides form a valid triangle, 'No' otherwise.

    Examples:
        >>> solve(3, 4, 5)
        'Yes'
        >>> solve(1, 2, 3)
        'No'
        >>> solve(1, 1, 1)
        'Yes'
    """
    # Check all three triangle inequality conditions simultaneously
    if x + y > z and x + z > y and y + z > x:
        return 'Yes'
    else:
        return 'No'