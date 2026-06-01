METADATA = {
    "id": 1957,
    "name": "Delete Characters to Make Fancy String",
    "slug": "delete-characters-to-make-fancy-string",
    "category": "String",
    "aliases": [],
    "tags": ["string_manipulation", "greedy"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Remove characters from a string such that no three consecutive characters are equal.",
}

def solve(s: str) -> str:
    """
    Removes characters from the input string so that no three consecutive 
    characters are identical.

    Args:
        s: The input string containing lowercase English letters.

    Returns:
        A new string where no character appears more than twice consecutively.

    Examples:
        >>> solve("leeetcode")
        'leetcode'
        >>> solve("aaabaaaa")
        'aabaa'
    """
    if len(s) < 3:
        return s

    # Use a list for efficient character appending (O(1) amortized)
    result_chars: list[str] = []
    
    for char in s:
        # Check if the last two characters in the result are the same as the current char
        # This prevents the formation of a triple (e.g., 'aaa')
        if len(result_chars) >= 2 and \
           result_chars[-1] == char and \
           result_chars[-2] == char:
            continue
            
        result_chars.append(char)

    return "".join(result_chars)
