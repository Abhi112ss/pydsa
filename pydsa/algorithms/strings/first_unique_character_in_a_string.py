METADATA = {
    "id": 387,
    "name": "First Unique Character in a String",
    "slug": "first_unique_character_in_a_string",
    "category": "String",
    "aliases": ["first_unique_char"],
    "tags": ["hash_map", "counting"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the index of the first non-repeating character in a string.",
}

def solve(s: str) -> int:
    """Find the index of the first non-repeating character in a string.

    Args:
        s: A string of lowercase English letters.

    Returns:
        The index of the first character that appears exactly once, or -1 if none exists.

    Examples:
        >>> solve("leetcode")
        0
        >>> solve("loveleetcode")
        2
        >>> solve("aabb")
        -1
    """
    # Count frequency of each character in the string
    frequency: dict[str, int] = {}
    for char in s:
        frequency[char] = frequency.get(char, 0) + 1

    # Find the first character with a frequency of one
    for index, char in enumerate(s):
        if frequency[char] == 1:
            return index

    return -1