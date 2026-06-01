METADATA = {
    "id": 20,
    "name": "Valid Parentheses",
    "slug": "valid-parentheses",
    "category": "Stack",
    "aliases": [],
    "tags": ["stack", "string", "hash-table"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Determine if an input string containing only the characters '(', ')', '{', '}', '[' and ']' is valid based on correct nesting and matching.",
}

def solve(s: str) -> bool:
    """
    Determines if the input string of parentheses is valid.

    A string is valid if:
    1. Open brackets are closed by the same type of brackets.
    2. Open brackets are closed in the correct order.
    3. Every close bracket has a corresponding open bracket of the same type.

    Args:
        s: A string containing only '(', ')', '{', '}', '[' and ']'.

    Returns:
        True if the string is valid, False otherwise.

    Examples:
        >>> solve("()")
        True
        >>> solve("()[]{}")
        True
        >>> solve("(]")
        False
        >>> solve("([)]")
        False
    """
    # Map closing brackets to their corresponding opening brackets for O(1) lookup
    bracket_map = {
        ")": "(",
        "}": "{",
        "]": "[",
    }
    
    stack: list[str] = []

    for character in s:
        # If the character is a closing bracket
        if character in bracket_map:
            # Pop the top element if stack is not empty, else use a dummy value
            top_element = stack.pop() if stack else "#"
            
            # If the popped element doesn't match the required opening bracket, it's invalid
            if bracket_map[character] != top_element:
                return False
        else:
            # If it's an opening bracket, push it onto the stack
            stack.append(character)

    # If the stack is empty, all brackets were matched correctly
    return not stack
