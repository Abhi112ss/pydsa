METADATA = {
    "id": 796,
    "name": "Rotate String",
    "slug": "rotate_string",
    "category": "String",
    "aliases": ["rotate_string", "string_rotation"],
    "tags": ["string_matching", "kmp"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Determine if one string is a rotation of another by checking if it is a substring of the doubled string.",
}

def solve(s: str, goal: str) -> bool:
    """Check if goal is a rotation of s using KMP substring search.

    Args:
        s (str): The original string.
        goal (str): The string to check if it is a rotation of s.

    Returns:
        bool: True if goal is a rotation of s, False otherwise.

    Examples:
        >>> solve("abcde", "cdeab")
        True
        >>> solve("abcde", "abced")
        False
    """
    if len(s) != len(goal):
        return False

    # Concatenate s with itself to form the text for KMP search
    text = s + s
    pattern = goal

    # Build the KMP failure function (partial match table)
    failure = [0] * len(pattern)
    j = 0
    for i in range(1, len(pattern)):
        while j > 0 and pattern[i] != pattern[j]:
            j = failure[j - 1]
        if pattern[i] == pattern[j]:
            j += 1
        failure[i] = j

    # Search for pattern in text using KMP
    j = 0
    for i in range(len(text)):
        while j > 0 and text[i] != pattern[j]:
            j = failure[j - 1]
        if text[i] == pattern[j]:
            j += 1
        if j == len(pattern):
            return True

    return False