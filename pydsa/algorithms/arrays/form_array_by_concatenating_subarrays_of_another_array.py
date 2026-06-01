METADATA = {
    "id": 1764,
    "name": "Form Array by Concatenating Subarrays of Another Array",
    "slug": "form_array_by_concatenating_subarrays_of_another_array",
    "category": "array",
    "aliases": [],
    "tags": ["greedy", "array"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(m)",
    "description": "Determine if an array can be formed by concatenating given subarrays in any order.",
}


def solve(arr: list[int], pieces: list[list[int]]) -> bool:
    """Greedy check whether `arr` can be formed by concatenating `pieces` in any order.

    Args:
        arr: The target array to be formed.
        pieces: A list of subarrays that may be reordered and concatenated.

    Returns:
        True if `arr` can be formed by concatenating all subarrays exactly once,
        otherwise False.

    Examples:
        >>> solve([15, 88], [[88], [15]])
        True
        >>> solve([49, 18, 16], [[49, 18], [16, 19]])
        False
    """
    # Map each piece's first element to the piece for O(1) lookup.
    first_to_piece: dict[int, list[int]] = {}
    for piece in pieces:
        if piece:  # ignore empty subarrays, though problem guarantees non‑empty.
            first_to_piece[piece[0]] = piece

    index = 0
    while index < len(arr):
        first_value = arr[index]
        # If no piece starts with the current value, formation is impossible.
        if first_value not in first_to_piece:
            return False

        piece = first_to_piece[first_value]
        # Verify that the piece matches the corresponding segment of `arr`.
        if arr[index : index + len(piece)] != piece:
            return False

        # Move the pointer forward by the length of the matched piece.
        index += len(piece)

    return True