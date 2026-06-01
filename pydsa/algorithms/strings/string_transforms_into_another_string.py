METADATA = {
    "id": 1153,
    "name": "String Transforms Into Another String",
    "slug": "string-transforms-into-another-string",
    "category": "Hash Table",
    "aliases": [],
    "tags": ["hash_map", "graphs", "string"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Determine if string s1 can be transformed into s2 by mapping each character to another unique character.",
}

def solve(s1: str, s2: str) -> bool:
    """
    Determines if s1 can be transformed into s2 by mapping each character 
    to exactly one other unique character.

    Args:
        s1: The source string.
        s2: The target string.

    Returns:
        True if the transformation is possible, False otherwise.

    Examples:
        >>> solve("abc", "def")
        True
        >>> solve("abb", "cdd")
        True
        >>> solve("abc", "abc")
        False
        >>> solve("a", "b")
        True
        >>> solve("ab", "ca")
        True
    """
    if len(s1) != len(s2):
        return False

    if s1 == s2:
        return False

    # Maps to track character relationships
    # char_to_target tracks where a char in s1 maps to in s2
    # target_to_char tracks which char in s1 maps to a specific char in s2
    char_to_target: dict[str, str] = {}
    target_to_char: dict[str, str] = {}

    # Count unique characters in the alphabet (26 lowercase English letters)
    # to check if we have enough 'spare' characters to break cycles.
    unique_chars_in_s1 = set(s1)
    unique_chars_in_s2 = set(s2)
    
    # The number of unique characters used in the mapping
    num_unique_mappings = len(unique_chars_in_s1)

    for char1, char2 in zip(s1, s2):
        # If s1[i] is already mapped to something else, transformation is impossible
        if char1 in char_to_target:
            if char_to_target[char1] != char2:
                return False
        else:
            char_to_target[char1] = char2

        # If s2[i] is already mapped from something else, transformation is impossible
        if char2 in target_to_char:
            if target_to_char[char2] != char1:
                return False
        else:
            target_to_char[char2] = char1

    # A transformation is possible if:
    # 1. The mapping is a valid bijection (handled by the loops above).
    # 2. We have at least one character in the alphabet not used in the mapping
    #    to break potential cycles (e.g., 'a' -> 'b' and 'b' -> 'a').
    # Since there are 26 letters, we need num_unique_mappings < 26.
    return num_unique_mappings < 26
