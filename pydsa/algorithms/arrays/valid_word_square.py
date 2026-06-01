METADATA = {
    "id": 422,
    "name": "Valid Word Square",
    "slug": "valid_word_square",
    "category": "array",
    "aliases": [],
    "tags": ["matrix", "string"],
    "difficulty": "easy",
    "time_complexity": "O(n*m)",
    "space_complexity": "O(1)",
    "description": "Check if a list of strings forms a valid word square.",
}


def solve(words: list[str]) -> bool:
    """Determine whether the given list of strings forms a valid word square.

    A word square is valid when the k-th row and k-th column read the same
    string for all valid indices k.

    Args:
        words: List of strings representing the rows of the square.

    Returns:
        True if the rows and columns match exactly, otherwise False.

    Examples:
        >>> solve(["abcd","bnrt","crmy","dtye"])
        True
        >>> solve(["abcd","bnrt","crm","dt"])
        False
    """
    total_rows: int = len(words)

    # Iterate over each character position (i, j) in the square.
    for row_index in range(total_rows):
        current_row: str = words[row_index]
        for col_index in range(len(current_row)):
            # If the corresponding column is missing or shorter, it's invalid.
            if col_index >= total_rows:
                return False
            corresponding_column: str = words[col_index]
            if row_index >= len(corresponding_column):
                return False
            # Characters must match symmetrically.
            if current_row[col_index] != corresponding_column[row_index]:
                return False

    return True