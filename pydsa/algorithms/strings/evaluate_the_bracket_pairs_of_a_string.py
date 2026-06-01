METADATA = {
    "id": 1807,
    "name": "Evaluate the Bracket Pairs of a String",
    "slug": "evaluate-the-bracket-pairs-of-a-string",
    "category": "Stack",
    "aliases": [],
    "tags": ["stack", "strings"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Evaluate the value of a string containing digits and nested bracket pairs by multiplying the values within each pair.",
}

def solve(s: str) -> int:
    """
    Evaluates the value of a string containing digits and nested bracket pairs.

    The evaluation follows the rule that for every pair of brackets (a, b), 
    the result is the product of a and b. This applies recursively to nested brackets.

    Args:
        s: A string containing digits and '(' and ')'.

    Returns:
        The integer result of the evaluation.

    Examples:
        >>> solve("((2)(3))")
        6
        >>> solve("(2)(3)")
        6
        >>> solve("((2)(3)(4))")
        24
    """
    # The stack stores the running product at each nesting level.
    # We initialize with [1] to represent the global product level.
    stack: list[int] = [1]
    current_product: int = 1
    
    i = 0
    n = len(s)
    while i < n:
        char = s[i]
        
        if char == '(':
            # When entering a new bracket, push the current product to the stack
            # and reset the current product for the new scope.
            stack.append(current_product)
            current_product = 1
            i += 1
        elif char == ')':
            # When exiting a bracket, the current_product is the value of the bracketed expression.
            # Multiply it by the product of the outer scope (top of stack).
            outer_product = stack.pop()
            current_product = outer_product * current_product
            i += 1
        else:
            # Parse the full number (though problem constraints usually imply single digits).
            num = 0
            while i < n and s[i].isdigit():
                num = num * 10 + int(s[i])
                i += 1
            
            # Multiply the current scope's product by the parsed number.
            current_product *= num
            
    return current_product
