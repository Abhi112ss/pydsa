METADATA = {
    "id": 3561,
    "name": "Resulting String After Adjacent Removals",
    "slug": "resulting_string_after_adjacent_removals",
    "category": "String",
    "aliases": [],
    "tags": ["stack", "string_manipulation"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Remove adjacent duplicate characters from a string repeatedly until no more adjacent duplicates exist.",
}

def solve(s: str) -> str:
    """
    Removes adjacent duplicate characters from a string using a stack-based approach.

    Args:
        s: The input string containing characters to be processed.

    Returns:
        The resulting string after all adjacent duplicate pairs have been removed.

    Examples:
        >>> solve("abbaca")
        'ca'
        >>> solve("azxxzy")
        'ay'
    """
    # A stack is used to keep track of characters that haven't been matched with a duplicate
    stack: list[str] = []

    for char in s:
        # If the stack is not empty and the current character matches the top of the stack,
        # we have found an adjacent duplicate pair.
        if stack and stack[-1] == char:
            stack.pop()
        else:
            # Otherwise, push the current character onto the stack.
            stack.append(char)

    # The stack contains the characters that remain after all adjacent removals.
    return "".join(stack)
