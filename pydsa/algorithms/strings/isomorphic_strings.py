METADATA = {
    "id": 205,
    "name": "Isomorphic Strings",
    "slug": "isomorphic_strings",
    "category": "Hash Table",
    "aliases": [],
    "tags": ["hash_map", "strings"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Given two strings s and t, determine if they are isomorphic by maintaining a unique one-to-one character mapping between them.",
}


def solve(s: str, t: str) -> bool:
    """Determine if two strings are isomorphic by maintaining a bijective character mapping.

    Two strings are isomorphic if characters in s can be replaced to get t, with a
    one-to-one mapping (no two characters map to the same character).

    Args:
        s: The source string.
        t: The target string.

    Returns:
        True if s and t are isomorphic, False otherwise.

    Examples:
        >>> solve("egg", "add")
        True
        >>> solve("foo", "bar")
        False
        >>> solve("paper", "title")
        True
    """
    if len(s) != len(t):
        return False

    # Build two hash maps for bidirectional one-to-one mapping
    s_to_t: dict[str, str] = {}
    t_to_s: dict[str, str] = {}

    for char_s, char_t in zip(s, t):
        # Check if char_s already maps to a different char_t
        if char_s in s_to_t and s_to_t[char_s] != char_t:
            return False
        # Check if char_t already maps to a different char_s
        if char_t in t_to_s and t_to_s[char_t] != char_s:
            return False
        # Record the bidirectional mapping
        s_to_t[char_s] = char_t
        t_to_s[char_t] = char_s

    return True