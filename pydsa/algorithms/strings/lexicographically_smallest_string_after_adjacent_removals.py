METADATA = {
    "id": 3563,
    "name": "Lexicographically Smallest String After Adjacent Removals",
    "slug": "lexicographically_smallest_string_after_adjacent_removals",
    "category": "String",
    "aliases": [],
    "tags": ["greedy", "string_manipulation", "monotonic_stack"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Find the lexicographically smallest string possible by removing adjacent characters based on specific constraints.",
}

def solve(s: str, k: int) -> str:
    """
    Finds the lexicographically smallest string possible by removing k characters.
    
    The problem asks for the lexicographically smallest string after removing 
    exactly k characters. This is a classic application of a monotonic stack.
    To make a string lexicographically smaller, we want smaller characters 
    to appear as early as possible. We achieve this by removing a character 
    if the next character is smaller than it.

    Args:
        s: The input string.
        k: The number of characters to remove.

    Returns:
        The lexicographically smallest string after k removals.

    Examples:
        >>> solve("cbacba", 2)
        'acba'
        >>> solve("leetcode", 3)
        'ecode'
    """
    stack: list[str] = []
    removals_left = k

    for char in s:
        # While we still have removals left and the current character is smaller 
        # than the last character added to the stack, remove the last character.
        # This maintains a monotonic increasing property as much as possible.
        while removals_left > 0 and stack and stack[-1] > char:
            stack.pop()
            removals_left -= 1
        stack.append(char)

    # If we still need to remove characters (e.g., the string was already 
    # non-decreasing), remove them from the end.
    if removals_left > 0:
        stack = stack[:-removals_left]

    return "".join(stack)
