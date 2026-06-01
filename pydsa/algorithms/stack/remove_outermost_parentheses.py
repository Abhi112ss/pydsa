METADATA = {
    "id": 1021,
    "name": "Remove Outermost Parentheses",
    "slug": "remove-outermost-parentheses",
    "category": "String",
    "aliases": [],
    "tags": ["stack", "string"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Remove the outermost parentheses of every primitive valid parentheses string in a given valid parentheses string.",
}

def solve(s: str) -> str:
    """
    Removes the outermost parentheses of every primitive valid parentheses string.

    A valid parentheses string is primitive if it cannot be split into two 
    non-empty valid parentheses strings.

    Args:
        s: A valid parentheses string.

    Returns:
        A string representing the input string with outermost parentheses removed.

    Examples:
        >>> solve("(()())(())")
        '()()()'
        >>> solve("(()())(())(()(()))")
        '()()()()(())()'
    """
    result_chars: list[str] = []
    depth: int = 0

    for char in s:
        if char == '(':
            # If depth > 0, this '(' is not an outermost parenthesis
            if depth > 0:
                result_chars.append(char)
            depth += 1
        else:
            # If depth > 1, this ')' is not an outermost parenthesis
            depth -= 1
            if depth > 0:
                result_chars.append(char)

    return "".join(result_chars)
