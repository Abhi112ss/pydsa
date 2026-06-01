METADATA = {
    "id": 3884,
    "name": "First Matching Character From Both Ends",
    "slug": "first_matching_character_from_both_ends",
    "category": "String",
    "aliases": [],
    "tags": ["two_pointer", "string_matching"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the first character that appears at the same index from both the beginning and the end of the string.",
}

def solve(s: str) -> str:
    """
    Finds the first character that matches its counterpart from the opposite end.
    
    The function iterates through the string from the start and compares the 
    character at index `i` with the character at index `n - 1 - i`.
    The first time these characters are identical, that character is returned.
    If no such character exists, an empty string is returned.

    Args:
        s: The input string to search through.

    Returns:
        The first matching character found, or an empty string if no match exists.

    Examples:
        >>> solve("abcde")
        ""
        >>> solve("abccba")
        "a"
        >>> solve("racecar")
        "r"
        >>> solve("aba")
        "a"
    """
    n = len(s)
    
    # We only need to iterate up to the middle of the string.
    # If the string has an odd length, the middle character is its own counterpart.
    # However, the problem asks for the 'first' matching character from both ends.
    # In a symmetric sense, the middle character of an odd string always matches itself.
    for i in range(n):
        # Calculate the index from the end
        opposite_index = n - 1 - i
        
        # Check if the character at the current index matches the character 
        # at the mirrored index from the end.
        if s[i] == s[opposite_index]:
            return s[i]
            
    return ""
