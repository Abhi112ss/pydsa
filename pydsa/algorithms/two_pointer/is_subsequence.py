METADATA = {
    "id": 392,
    "name": "Is Subsequence",
    "slug": "is_subsequence",
    "category": "String",
    "aliases": [],
    "tags": ["greedy"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Determine if string s is a subsequence of string t using two pointers.",
}

def solve(s: str, t: str) -> bool:
    """Determine if string s is a subsequence of string t using two pointers.

    Args:
        s (str): The potential subsequence string.
        t (str): The main string to search within.

    Returns:
        bool: True if s is a subsequence of t, False otherwise.

    Examples:
        >>> solve("abc", "ahbgdc")
        True
        >>> solve("axc", "ahbgdc")
        False
        >>> solve("", "ahbgdc")
        True
        >>> solve("abc", "")
        False
    """
    # Initialize pointer for string s
    s_pointer = 0
    
    # Iterate through each character in string t
    for char in t:
        # If current character in t matches current character in s, advance s pointer
        if s_pointer < len(s) and char == s[s_pointer]:
            s_pointer += 1
    
    # Check if all characters in s were found in order
    return s_pointer == len(s)