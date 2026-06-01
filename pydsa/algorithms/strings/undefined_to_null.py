METADATA = {
    "id": 2775,
    "name": "Undefined to Null",
    "slug": "undefined-to-null",
    "category": "Strings",
    "aliases": [],
    "tags": ["strings", "regex"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Replace all occurrences of the string 'undefined' with 'null' in a given string.",
}

def solve(s: str) -> str:
    """
    Replaces all occurrences of the substring 'undefined' with 'null'.

    Args:
        s: The input string containing potential 'undefined' substrings.

    Returns:
        A new string where all 'undefined' instances are replaced by 'null'.

    Examples:
        >>> solve("undefined")
        'null'
        >>> solve("null")
        'null'
        >>> solve("undefinedundefined")
        'nullnull'
        >>> solve("abcundefineddef")
        'abcnulldef'
    """
    # The built-in replace method in Python is highly optimized (implemented in C)
    # and performs a single pass over the string, making it O(n).
    # It handles non-overlapping occurrences efficiently.
    return s.replace("undefined", "null")
