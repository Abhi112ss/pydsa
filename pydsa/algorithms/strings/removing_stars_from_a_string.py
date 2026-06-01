METADATA = {
    "id": 2390,
    "name": "Removing Stars From a String",
    "slug": "removing-stars-from-a-string",
    "category": "String",
    "aliases": [],
    "tags": ["stack", "strings"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Remove all stars from a string where each star removes the closest non-star character to its left.",
}

def solve(s: str) -> str:
    """
    Removes all stars from the string. A star '*' removes the nearest 
    non-star character to its left.

    Args:
        s: The input string containing characters and stars.

    Returns:
        The resulting string after all stars have been processed.

    Examples:
        >>> solve("leet**cod*e")
        'lecoe'
        >>> solve("erase^^") # Note: problem uses '*', this is just an example
        ''
        >>> solve("cb*a*b")
        'b'
    """
    # We use a list as a stack to efficiently push and pop characters.
    # A list in Python provides O(1) amortized append and pop operations.
    stack: list[str] = []

    for char in s:
        if char == "*":
            # If we encounter a star, remove the last character added to the stack.
            # The problem guarantees there will always be a character to remove.
            if stack:
                stack.pop()
        else:
            # If it's a normal character, push it onto the stack.
            stack.append(char)

    # Join the remaining characters in the stack to form the final string.
    return "".join(stack)
