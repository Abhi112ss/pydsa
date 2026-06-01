METADATA = {
    "id": 2710,
    "name": "Remove Trailing Zeros From a String",
    "slug": "remove-trailing-zeros-from-a-string",
    "category": "Strings",
    "aliases": [],
    "tags": ["strings", "two_pointer"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Remove all trailing zeros from a given string.",
}

def solve(s: str) -> str:
    """
    Removes all trailing zeros from the input string.

    Args:
        s: The input string containing characters and potentially trailing zeros.

    Returns:
        A new string with all trailing '0' characters removed.

    Examples:
        >>> solve("102")
        '102'
        >>> solve("100")
        '1'
        >>> solve("000")
        ''
    """
    # Start from the end of the string and move backwards
    index = len(s) - 1
    
    # Decrement the index as long as we encounter '0'
    while index >= 0 and s[index] == '0':
        index -= 1
        
    # Return the substring from the start up to the last non-zero character
    # If all characters were '0', index will be -1, resulting in an empty string
    return s[:index + 1]
