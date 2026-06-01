METADATA = {
    "id": 2957,
    "name": "Remove Adjacent Almost-Equal Characters",
    "slug": "remove-adjacent-almost-equal-characters",
    "category": "String",
    "aliases": [],
    "tags": ["stack", "strings"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Remove adjacent characters that are either identical or differ by at most one in their ASCII values.",
}

def solve(s: str) -> str:
    """
    Removes adjacent characters that are 'almost-equal'.
    Two characters are almost-equal if |ord(c1) - ord(c2)| <= 1.
    
    Args:
        s: The input string.

    Returns:
        The resulting string after removing all adjacent almost-equal characters.

    Examples:
        >>> solve("abccba")
        ""
        >>> solve("abc")
        "abc"
        >>> solve("aab")
        ""
    """
    stack: list[str] = []

    for char in s:
        # Check if the stack is not empty and the current character 
        # is 'almost-equal' to the character at the top of the stack.
        if stack and abs(ord(stack[-1]) - ord(char)) <= 1:
            # If they are almost-equal, remove the top of the stack
            # and do not add the current character (effectively removing both).
            stack.pop()
        else:
            # Otherwise, push the current character onto the stack.
            stack.append(char)

    return "".join(stack)
