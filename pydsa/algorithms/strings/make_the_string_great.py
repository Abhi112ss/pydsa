METADATA = {
    "id": 1544,
    "name": "Make The String Great",
    "slug": "make_the_string_great",
    "category": "String",
    "aliases": [],
    "tags": ["stack", "string"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Remove adjacent opposite‑case letters until no such pairs remain.",
}


def solve(s: str) -> str:
    """Return the string after repeatedly deleting adjacent opposite‑case pairs.

    Args:
        s: The input string consisting of English letters.

    Returns:
        A string where no two adjacent characters are the same letter in opposite
        cases.

    Examples:
        >>> solve("leEeetcode")
        'leetcode'
        >>> solve("abBAcC")
        ''
        >>> solve("s")
        's'
    """
    stack: list[str] = []
    for current_char in s:
        # If the stack is non‑empty and the top character forms an opposite‑case pair,
        # remove the top character; otherwise, push the current character.
        if stack and current_char.lower() == stack[-1].lower() and current_char != stack[-1]:
            stack.pop()
        else:
            stack.append(current_char)
    return "".join(stack)