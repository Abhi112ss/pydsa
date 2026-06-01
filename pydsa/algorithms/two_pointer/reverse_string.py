METADATA = {
    "id": 344,
    "name": "Reverse String",
    "slug": "reverse_string",
    "category": "String",
    "aliases": [],
    "tags": ["two_pointer", "string"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Reverses a list of characters in-place using two-pointer swapping.",
}


def solve(s: list[str]) -> None:
    """Reverse a list of characters in-place.

    Args:
        s: A list of single-character strings to be reversed.

    Returns:
        None. The input list is modified directly.

    Examples:
        >>> chars = ["h", "e", "l", "l", "o"]
        >>> solve(chars)
        >>> chars
        ['o', 'l', 'l', 'e', 'h']

        >>> chars = ["A"]
        >>> solve(chars)
        >>> chars
        ['A']
    """
    left_index: int = 0
    right_index: int = len(s) - 1

    # Swap characters moving inward until the two pointers meet or cross.
    while left_index < right_index:
        s[left_index], s[right_index] = s[right_index], s[left_index]
        left_index += 1
        right_index -= 1