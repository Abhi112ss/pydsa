METADATA = {
    "id": 2351,
    "name": "First Letter to Appear Twice",
    "slug": "first_letter_to_appear_twice",
    "category": "String",
    "aliases": [],
    "tags": ["hash_set", "string_manipulation"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Return the first character that occurs twice when scanning the string from left to right.",
}


def solve(s: str) -> str:
    """Return the first letter that appears twice in the given string.

    Args:
        s: A non‑empty string consisting of lowercase English letters.
            It is guaranteed that at least one letter appears at least twice.

    Returns:
        The first character that is encountered for the second time while scanning
        the string from left to right.

    Examples:
        >>> solve("abccbaacz")
        'c'
        >>> solve("abcdd")
        'd'
        >>> solve("zz")
        'z'
    """
    seen_characters: set[str] = set()
    for character in s:
        # If the character was seen before, it is the first to appear twice.
        if character in seen_characters:
            return character
        seen_characters.add(character)
    # The problem guarantees a repeated character; this line is unreachable.
    return ""