METADATA = {
    "id": 316,
    "name": "Remove Duplicate Letters",
    "slug": "remove-duplicate-letters",
    "category": "String",
    "aliases": [],
    "tags": ["greedy", "monotonic_stack", "string"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Given a string s, remove duplicate letters so that every letter appears once and the result is the smallest in lexicographical order.",
}

def solve(s: str) -> str:
    """
    Removes duplicate letters from a string such that every letter appears once 
    and the resulting string is the smallest in lexicographical order.

    Args:
        s: The input string containing lowercase English letters.

    Returns:
        The lexicographically smallest string containing all unique characters from s.

    Examples:
        >>> solve("bcabc")
        'abc'
        >>> solve("cbacdcbc")
        'acdb'
    """
    # Count the frequency of each character to know if we can discard it later
    last_occurrence = {char: i for i, char in enumerate(s)}
    
    # Track characters currently in our monotonic stack to ensure uniqueness
    visited = set()
    stack = []

    for index, char in enumerate(s):
        # If character is already in our result, skip it to maintain uniqueness
        if char in visited:
            continue

        # While:
        # 1. Stack is not empty
        # 2. Current char is smaller than the top of the stack (greedy choice)
        # 3. The top of the stack appears again later in the string (safety check)
        while stack and char < stack[-1] and last_occurrence[stack[-1]] > index:
            removed_char = stack.pop()
            visited.remove(removed_char)

        # Add the current character to the stack and mark as visited
        stack.append(char)
        visited.add(char)

    return "".join(stack)
