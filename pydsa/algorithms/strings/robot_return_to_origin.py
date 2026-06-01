METADATA = {
    "id": 657,
    "name": "Robot Return to Origin",
    "slug": "robot_return_to_origin",
    "category": "Array",
    "aliases": ["Robot Return to Origin"],
    "tags": ["string", "simulation"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Determine if a robot returns to the origin after a sequence of moves.",
}

def solve(moves: str) -> bool:
    """Determine if a robot returns to the origin after a sequence of moves.

    The robot starts at (0, 0) and moves according to the given string of moves.
    'U' moves up, 'D' moves down, 'L' moves left, 'R' moves right.
    Return True if the robot ends at the origin, False otherwise.

    Args:
        moves: A string of moves consisting of 'U', 'D', 'L', 'R'.

    Returns:
        True if the robot returns to the origin, False otherwise.

    Examples:
        >>> solve("UD")
        True
        >>> solve("LL")
        False
        >>> solve("UDLR")
        True
    """
    # Count vertical and horizontal displacements
    vertical = 0
    horizontal = 0

    # Iterate through each move and update displacements
    for move in moves:
        if move == 'U':
            vertical += 1
        elif move == 'D':
            vertical -= 1
        elif move == 'L':
            horizontal -= 1
        elif move == 'R':
            horizontal += 1

    # Check if both displacements are zero
    return vertical == 0 and horizontal == 0