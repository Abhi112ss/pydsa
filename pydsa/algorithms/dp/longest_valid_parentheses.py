METADATA = {
    "id": 32,
    "name": "Longest Valid Parentheses",
    "slug": "longest-valid-parentheses",
    "category": "String",
    "aliases": [],
    "tags": ["stack", "dp", "strings"],
    "difficulty": "hard",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Find the length of the longest valid (well-formed) parentheses substring.",
}

def solve(s: str) -> int:
    """
    Finds the length of the longest valid (well-formed) parentheses substring.

    Args:
        s: A string consisting of '(' and ')'.

    Returns:
        The length of the longest valid parentheses substring.

    Examples:
        >>> solve("(()")
        2
        >>> solve(")()())")
        4
        >>> solve("")
        0
    """
    # We use a stack to store the indices of the characters.
    # We initialize the stack with -1 to act as a boundary for the 
    # calculation of the length of the first valid substring.
    stack: list[int] = [-1]
    max_length: int = 0

    for index, character in enumerate(s):
        if character == '(':
            # Push the index of the opening parenthesis onto the stack.
            stack.append(index)
        else:
            # If we encounter a closing parenthesis, pop the last element.
            stack.pop()
            
            if not stack:
                # If the stack is empty, it means the current ')' is a mismatch.
                # We push the current index to serve as the new boundary for 
                # future valid substrings.
                stack.append(index)
            else:
                # If the stack is not empty, the current substring is valid.
                # The length is the current index minus the index of the 
                # element currently at the top of the stack.
                current_length = index - stack[-1]
                if current_length > max_length:
                    max_length = current_length

    return max_length
