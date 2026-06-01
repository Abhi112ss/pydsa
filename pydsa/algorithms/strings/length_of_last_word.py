METADATA = {
    "id": 58,
    "name": "Length of Last Word",
    "slug": "length-of-last-word",
    "category": "String",
    "aliases": [],
    "tags": ["string", "simulation"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Return the length of the last word in the string, where a word is a maximal substring consisting of non-space characters only.",
}

def solve(s: str) -> int:
    """
    Calculates the length of the last word in a given string.

    Args:
        s: A string containing words separated by spaces.

    Returns:
        The length of the last word in the string.

    Examples:
        >>> solve("Hello World")
        5
        >>> solve("   fly me to the moon  ")
        4
        >>> solve("luffy is still joyboy")
        6
    """
    length = 0
    index = len(s) - 1

    # Step 1: Skip all trailing spaces at the end of the string
    while index >= 0 and s[index] == ' ':
        index -= 1

    # Step 2: Count characters until we hit a space or the start of the string
    while index >= 0 and s[index] != ' ':
        length += 1
        index -= 1

    return length
