METADATA = {
    "id": 3274,
    "name": "Check if Two Chessboard Squares Have the Same Color",
    "slug": "check-if-two-chessboard-squares-have-the-same-color",
    "category": "Math",
    "aliases": [],
    "tags": ["math", "implementation"],
    "difficulty": "easy",
    "time_complexity": "O(1)",
    "space_complexity": "O(1)",
    "description": "Determine if two squares on a chessboard, given by their coordinates, have the same color.",
}

def solve(r1: int, c1: int, r2: int, c2: int) -> bool:
    """
    Determines if two squares on a chessboard have the same color.

    On a standard chessboard, the color of a square (r, c) is determined 
    by the parity of the sum of its row and column indices. If (r + c) 
    is even, it is one color; if odd, it is the other.

    Args:
        r1 (int): Row index of the first square.
        c1 (int): Column index of the first square.
        r2 (int): Row index of the second square.
        c2 (int): Column index of the second square.

    Returns:
        bool: True if both squares have the same color, False otherwise.

    Examples:
        >>> solve(0, 0, 1, 1)
        True
        >>> solve(0, 0, 0, 1)
        False
    """
    # A square's color is defined by whether (row + col) is even or odd.
    # Two squares have the same color if the parity of their sums is identical.
    first_square_parity = (r1 + c1) % 2
    second_square_parity = (r2 + c2) % 2

    # Return True if parities match, False otherwise.
    return first_square_parity == second_square_parity