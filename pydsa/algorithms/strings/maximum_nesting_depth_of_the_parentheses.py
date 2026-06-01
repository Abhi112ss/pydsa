METADATA = {
    "id": 1614,
    "name": "Maximum Nesting Depth of the Parentheses",
    "slug": "maximum-nesting-depth-of-the-parentheses",
    "category": "String",
    "aliases": [],
    "tags": ["stack", "strings", "greedy"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the maximum nesting depth of a valid parentheses string.",
}

def solve(s: str) -> int:
    """
    Calculates the maximum nesting depth of parentheses in a valid string.

    The nesting depth is defined as the maximum number of open parentheses 
    that are currently unmatched at any point while scanning the string.

    Args:
        s: A valid parentheses string containing digits, '+', '-', '*', '/', 
           and parentheses.

    Returns:
        The maximum nesting depth of the parentheses.

    Examples:
        >>> solve("(1+(2*3)+((8)/4))+1")
        3
        >>> solve("(1)")
        1
        >>> solve("1+(2*3)/(2-1)")
        1
    """
    max_depth = 0
    current_depth = 0

    for char in s:
        if char == '(':
            # Increment depth when an opening parenthesis is encountered
            current_depth += 1
            # Update the global maximum depth reached so far
            if current_depth > max_depth:
                max_depth = current_depth
        elif char == ')':
            # Decrement depth when a closing parenthesis is encountered
            current_depth -= 1

    return max_depth
