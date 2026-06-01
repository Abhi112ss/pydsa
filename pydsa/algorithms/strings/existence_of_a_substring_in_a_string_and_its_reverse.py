METADATA = {
    "id": 3083,
    "name": "Existence of a Substring in a String and Its Reverse",
    "slug": "existence-of-a-substring-in-a-string-and-its-reverse",
    "category": "Strings",
    "aliases": [],
    "tags": ["strings", "string-searching"],
    "difficulty": "easy",
    "time_complexity": "O(n * m)",
    "space_complexity": "O(m)",
    "description": "Determine if a given substring or its reverse exists within a target string.",
}

def solve(word: str, s: str) -> bool:
    """
    Checks if the given word or its reverse is a substring of s.

    Args:
        word: The substring to search for.
        s: The target string to search within.

    Returns:
        True if word or reversed(word) is in s, False otherwise.

    Examples:
        >>> solve("abc", "abccba")
        True
        >>> solve("abc", "def")
        False
        >>> solve("abc", "cba")
        True
    """
    # Check if the original word exists in the target string
    if word in s:
        return True
    
    # Create the reversed version of the word
    # Slicing [::-1] is an efficient O(m) way to reverse a string in Python
    reversed_word = word[::-1]
    
    # Check if the reversed word exists in the target string
    return reversed_word in s
