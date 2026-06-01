METADATA = {
    "id": 1812,
    "name": "Determine Color of a Chessboard Square",
    "slug": "determine_color_of_a_chessboard_square",
    "category": "math",
    "aliases": [],
    "tags": ["math"],
    "difficulty": "easy",
    "time_complexity": "O(1)",
    "space_complexity": "O(1)",
    "description": "Determine if a given chessboard coordinate corresponds to a white square.",
}


def solve(coordinates: str) -> bool:
    """Determine whether the given chessboard square is white.

    Args:
        coordinates: A two‑character string where the first character is a column
            letter from 'a' to 'h' and the second character is a row digit from '1' to '8'.

    Returns:
        True if the square is white, False otherwise.

    Examples:
        >>> solve("a1")
        False
        >>> solve("c3")
        True
        >>> solve("h8")
        False
    """
    # Convert column letter to a 1‑based index (a -> 1, b -> 2, ...)
    column_index: int = ord(coordinates[0].lower()) - ord('a') + 1
    # Convert row character to integer (e.g., '1' -> 1)
    row_index: int = int(coordinates[1])

    # A square is white when the sum of its row and column indices is odd.
    return (column_index + row_index) % 2 == 1