METADATA = {
    "id": 921,
    "name": "Minimum Add to Make Parentheses Valid",
    "slug": "minimum-add-to-make-parentheses-valid",
    "category": "String",
    "aliases": [],
    "tags": ["stack", "greedy", "string"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the minimum number of parentheses needed to make a given string of parentheses valid.",
}

def solve(s: str) -> int:
    """
    Calculates the minimum number of parentheses to add to make the string valid.

    A string is valid if every opening parenthesis '(' has a corresponding 
    closing parenthesis ')' and they are correctly nested.

    Args:
        s: A string consisting only of '(' and ')'.

    Returns:
        The minimum number of parentheses required to make the string valid.

    Examples:
        >>> solve("())")
        1
        >>> solve("(((")
        3
        >>> solve("()")
        0
        >>> solve("()))((")
        4
    """
    # unmatched_open tracks '(' that haven't found a closing ')' yet
    unmatched_open = 0
    # unmatched_close tracks ')' that appeared without a preceding '('
    unmatched_close = 0

    for char in s:
        if char == '(':
            # We found a potential start of a valid pair
            unmatched_open += 1
        else:
            # We found a closing parenthesis
            if unmatched_open > 0:
                # This ')' matches an existing '('
                unmatched_open -= 1
            else:
                # No '(' available to match this ')', so this ')' is unmatched
                unmatched_close += 1

    # The total additions needed is the sum of unmatched '(' and unmatched ')'
    return unmatched_open + unmatched_close
