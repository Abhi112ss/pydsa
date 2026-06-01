METADATA = {
    "id": 459,
    "name": "Repeated Substring Pattern",
    "slug": "repeated_substring_pattern",
    "category": "String",
    "aliases": [],
    "tags": ["string_matching", "kmp"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Given a string s, check if it can be constructed by taking a substring of it and appending multiple copies of the substring together.",
}


def solve(s: str) -> bool:
    """Check if a string can be constructed by repeating a substring pattern.

    Uses the KMP-based approach: if s has a repeated pattern, it will appear
    as a substring in (s + s) with the first and last characters removed.

    Args:
        s: The input string to check.

    Returns:
        True if s can be constructed by repeating a substring, False otherwise.

    Examples:
        >>> solve("abab")
        True
        >>> solve("aba")
        False
        >>> solve("abcabcabcabc")
        True
    """
    if not s:
        return False

    # Concatenate s with itself and remove first and last character
    doubled = s + s
    # Check if s appears in the middle of the doubled string
    return s in doubled[1:-1]