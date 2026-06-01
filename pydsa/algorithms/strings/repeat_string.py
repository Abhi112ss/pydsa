METADATA = {
    "id": 2796,
    "name": "Repeat String",
    "slug": "repeat-string",
    "category": "String",
    "aliases": [],
    "tags": ["string", "math"],
    "difficulty": "easy",
    "time_complexity": "O(n * k)",
    "space_complexity": "O(n * k)",
    "description": "Construct a new string by repeating a given string k times.",
}

def solve(s: str, k: int) -> str:
    """
    Constructs a new string by repeating the input string 's' exactly 'k' times.

    Args:
        s: The base string to be repeated.
        k: The number of times to repeat the string.

    Returns:
        A string consisting of 's' concatenated 'k' times.

    Examples:
        >>> solve("abc", 3)
        'abcabcabc'
        >>> solve("a", 0)
        ''
        >>> solve("", 5)
        ''
    """
    # In Python, string multiplication is highly optimized in C
    # and handles the concatenation in O(n * k) time.
    # If k is 0 or negative, it returns an empty string.
    return s * k
