METADATA = {
    "id": 1640,
    "name": "Check Array Formation Through Concatenation",
    "slug": "check_array_formation_through_concatenation",
    "category": "Array",
    "aliases": [],
    "tags": ["arrays"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(m)",
    "description": "Determine if an array can be formed by concatenating given subarrays.",
}


def solve(arr: list[int], pieces: list[list[int]]) -> bool:
    """Check if ``arr`` can be formed by concatenating the subarrays in ``pieces``.

    Args:
        arr: The target array to be formed.
        pieces: A list of subarrays that can be concatenated in any order.
                Each subarray is used at most once.

    Returns:
        True if ``arr`` can be formed by concatenating all subarrays in some order,
        otherwise False.

    Examples:
        >>> solve([85, 92, 86, 81], [[85, 92], [86, 81]])
        True
        >>> solve([85, 92, 86, 81], [[85, 92], [81, 86]])
        False
    """
    # Map the first element of each piece to the piece itself for O(1) lookup.
    first_to_piece: dict[int, list[int]] = {piece[0]: piece for piece in pieces}

    index: int = 0
    while index < len(arr):
        # The current value must start a piece; otherwise formation is impossible.
        if arr[index] not in first_to_piece:
            return False

        current_piece = first_to_piece[arr[index]]
        piece_length = len(current_piece)

        # Verify that the slice of ``arr`` matches the expected piece.
        if arr[index:index + piece_length] != current_piece:
            return False

        # Move the index forward by the length of the matched piece.
        index += piece_length

    return True