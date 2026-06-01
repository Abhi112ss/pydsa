METADATA = {
    "id": 709,
    "name": "To Lower Case",
    "slug": "to-lower-case",
    "category": "String",
    "aliases": [],
    "tags": ["string", "ascii"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Convert a given string to lowercase without using built-in library functions.",
}

def solve(s: str) -> str:
    """
    Args:
        s: The input string to be converted.

    Returns:
        The converted lowercase string.
    """
    result_chars = []
    for character in s:
        ascii_value = ord(character)
        if 65 <= ascii_value <= 90:
            result_chars.append(chr(ascii_value + 32))
        else:
            result_chars.append(character)
    return "".join(result_chars)