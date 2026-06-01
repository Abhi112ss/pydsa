METADATA = {
    "id": 1528,
    "name": "Shuffle String",
    "slug": "shuffle_string",
    "category": "String",
    "aliases": [],
    "tags": ["strings"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Rearrange characters of a string according to a given index mapping.",
}


def solve(s: str, indices: list[int]) -> str:
    """Shuffle a string based on target indices.

    Args:
        s: The original string to be shuffled.
        indices: A list where indices[i] indicates the target position of s[i] in the shuffled string.

    Returns:
        The shuffled string where each character from `s` is placed at its corresponding index.

    Examples:
        >>> solve("abc", [0, 1, 2])
        'abc'
        >>> solve("abc", [1, 2, 0])
        'cab'
        >>> solve("codeleet", [4,5,6,7,0,2,1,3])
        'leetcode'
    """
    # Initialize a list to hold characters at their target positions.
    shuffled: list[str] = [''] * len(s)

    # Place each character from the original string into its new position.
    for original_position, target_position in enumerate(indices):
        shuffled[target_position] = s[original_position]

    # Combine the list into the final shuffled string.
    return ''.join(shuffled)