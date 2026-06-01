METADATA = {
    "id": 856,
    "name": "Score of Parentheses",
    "slug": "score-of-parentheses",
    "category": "Stack",
    "aliases": [],
    "tags": ["string_manipulation", "math", "stack"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Calculate the score of a balanced parentheses string based on specific nesting rules.",
}

def solve(s: str) -> int:
    """
    Calculates the score of a balanced parentheses string.
    
    The rules are:
    - "()" has score 1.
    - AB has score A + B, where A and B are balanced parentheses strings.
    - (A) has score 2 * A, where A is a balanced parentheses string.

    Args:
        s: A balanced parentheses string.

    Returns:
        The total score of the string.

    Examples:
        >>> solve("()")
        1
        >>> solve("(())")
        2
        >>> solve("()()")
        2
        >>> solve("(()(()))")
        6
    """
    # We use a stack to keep track of the score at each nesting level.
    # stack[i] represents the score accumulated at the current depth.
    stack: list[int] = [0]

    for char in s:
        if char == '(':
            # Entering a new nesting level, push a new score tracker.
            stack.append(0)
        else:
            # Closing a parenthesis.
            # Pop the score of the inner level.
            inner_score = stack.pop()
            
            # Calculate the score contributed by this level:
            # If inner_score is 0, it means we just closed a "()", which is worth 1.
            # Otherwise, it's a "(A)" structure, which is worth 2 * A.
            current_contribution = max(2 * inner_score, 1)
            
            # Add this contribution to the score of the parent level.
            stack[-1] += current_contribution

    return stack[0]
