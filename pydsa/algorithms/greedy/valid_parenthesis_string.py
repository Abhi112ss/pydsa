METADATA = {
    "id": 678,
    "name": "Valid Parenthesis String",
    "slug": "valid-parenthesis-string",
    "category": "String",
    "aliases": [],
    "tags": ["greedy", "stack", "dynamic_programming"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Determine if a string containing '(', ')', and '*' is valid, where '*' can be treated as '(', ')', or an empty string.",
}

def solve(s: str) -> bool:
    """
    Determines if the given string containing '(', ')', and '*' is valid.
    
    The algorithm uses a greedy approach by maintaining the range of possible 
    counts of open parentheses. 'min_open' tracks the minimum possible open 
    parentheses (treating '*' as ')' or empty), and 'max_open' tracks the 
    maximum possible (treating '*' as '(').

    Args:
        s: The input string containing '(', ')', and '*'.

    Returns:
        True if the string is valid, False otherwise.

    Examples:
        >>> solve("()")
        True
        >>> solve("(*)")
        True
        >>> solve("(*))")
        True
        >>> solve(")(")
        False
    """
    # min_open represents the lower bound of open parentheses we must have.
    # max_open represents the upper bound of open parentheses we could have.
    min_open = 0
    max_open = 0

    for char in s:
        if char == '(':
            min_open += 1
            max_open += 1
        elif char == ')':
            min_open -= 1
            max_open -= 1
        elif char == '*':
            # If '*', it could be '(', ')', or empty.
            # To minimize open count, treat as ')'
            min_open -= 1
            # To maximize open count, treat as '('
            max_open += 1

        # If max_open is negative, even with all '*' as '(', 
        # we have too many ')' to ever be valid.
        if max_open < 0:
            return False
        
        # min_open cannot be negative because we can't have "negative" 
        # required open parentheses. If it drops below 0, we reset it to 0
        # (effectively treating some '*' as empty or '(' instead of ')').
        if min_open < 0:
            min_open = 0

    # For the string to be valid, we must be able to end with exactly 0 open parentheses.
    # This is possible if 0 falls within our [min_open, max_open] range.
    return min_open == 0