METADATA = {
    "id": 3174,
    "name": "Clear Digits",
    "slug": "clear-digits",
    "category": "String",
    "aliases": [],
    "tags": ["string", "stack"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Remove all digit characters from a given string.",
}

def solve(s: str) -> str:
    """
    Removes all numeric digit characters from the input string.

    Args:
        s: The input string containing alphanumeric characters.

    Returns:
        A new string containing only the non-digit characters from the original string.

    Examples:
        >>> solve("leet123code")
        'leetcode'
        >>> solve("a1b2c3d4")
        'abcd'
        >>> solve("12345")
        ''
    """
    # Use a list to collect characters to avoid O(n^2) string concatenation overhead
    result_chars: list[str] = []

    for char in s:
        # Check if the character is not a digit
        if not char.isdigit():
            result_chars.append(char)

    # Join the list into a single string for the final result
    return "".join(result_chars)
