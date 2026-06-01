METADATA = {
    "id": 1047,
    "name": "Remove All Adjacent Duplicates In String",
    "slug": "remove_all_adjacent_duplicates_in_string",
    "category": "String",
    "aliases": [],
    "tags": ["stack", "string_manipulation"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Remove all adjacent duplicate characters from a string using a stack.",
}


def solve(s: str) -> str:
    """Remove all adjacent duplicate characters from the given string.

    Args:
        s: The input string consisting of lowercase English letters.

    Returns:
        A new string after repeatedly deleting any pair of adjacent equal characters.

    Examples:
        >>> solve("abbaca")
        'ca'
        >>> solve("azxxzy")
        'ay'
        >>> solve("")
        ''
    """
    # Use a list as a stack to store characters that have not been cancelled.
    stack: list[str] = []
    for character in s:
        if stack and stack[-1] == character:
            # Current character matches the top of the stack → remove the duplicate pair.
            stack.pop()
        else:
            # No duplicate, keep the character.
            stack.append(character)
    # Join the remaining characters to form the result string.
    return "".join(stack)