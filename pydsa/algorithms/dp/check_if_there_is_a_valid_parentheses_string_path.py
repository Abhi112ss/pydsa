METADATA = {
    "id": 2267,
    "name": "Check if There Is a Valid Parentheses String Path",
    "slug": "check-if-there-is-a-valid-parentheses-string-path",
    "category": "String",
    "aliases": [],
    "tags": ["greedy", "string", "stack"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Determine if a string containing '(', ')', and '*' can form a valid parentheses sequence by treating '*' as any of the three characters.",
}

def solve(s: str) -> bool:
    """
    Determines if the given string can form a valid parentheses sequence.
    
    The algorithm uses a greedy approach by maintaining the range of possible 
    counts of open parentheses '(' that could exist at any given point.

    Args:
        s: A string consisting of '(', ')', and '*'.

    Returns:
        True if a valid parentheses sequence can be formed, False otherwise.

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
    # min_open represents the minimum number of open parentheses we must have.
    # max_open represents the maximum number of open parentheses we could have.
    min_open = 0
    max_open = 0

    for char in s:
        if char == '(':
            # We must increment both bounds.
            min_open += 1
            max_open += 1
        elif char == ')':
            # We must decrement both bounds.
            min_open -= 1
            max_open -= 1
        else:  # char == '*'
            # '*' can be '(', so max_open increases.
            # '*' can be ')', so min_open decreases.
            # '*' can be empty, so min_open/max_open stay within bounds.
            min_open -= 1
            max_open += 1

        # If max_open is negative, even using all '*' as '(' cannot balance the ')'.
        if max_open < 0:
            return False
        
        # min_open cannot be less than 0 because we can't have negative open parentheses.
        # If it drops below 0, we treat the '*' as an empty string or '(' instead of ')'.
        if min_open < 0:
            min_open = 0

    # A valid sequence must end with exactly 0 open parentheses.
    # min_open <= 0 <= max_open ensures that 0 is a reachable state.
    return min_open == 0
