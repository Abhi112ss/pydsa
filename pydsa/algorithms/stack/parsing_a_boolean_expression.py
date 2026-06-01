METADATA = {
    "id": 1106,
    "name": "Parsing A Boolean Expression",
    "slug": "parsing-a-boolean-expression",
    "category": "Stack",
    "aliases": [],
    "tags": ["stack", "string", "parsing"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Evaluate a boolean expression string containing '!', '&', '|', and parentheses.",
}

def solve(expression: str) -> bool:
    """
    Evaluates a boolean expression string containing '!', '&', '|', and parentheses.

    The expression follows a specific format where operators precede their operands,
    and operands can be single characters ('t', 'f') or nested expressions.

    Args:
        expression: A string representing the boolean expression.

    Returns:
        The boolean result of the evaluated expression.

    Examples:
        >>> solve("!(t)")
        False
        >>> solve("|(&(t,f,t),!(t))")
        True
    """
    stack: list[str] = []

    for char in expression:
        # Skip commas as they are just delimiters in the expression format
        if char == ',':
            continue
        
        # When we hit a closing parenthesis, we evaluate the sub-expression
        if char == ')':
            operands: list[bool] = []
            
            # Pop elements until we find the matching opening parenthesis
            while stack and stack[-1] != '(':
                val = stack.pop()
                operands.append(True if val == 't' else False)
            
            # Remove the '(' from the stack
            if stack and stack[-1] == '(':
                stack.pop()
            
            # The character before '(' is the operator for this sub-expression
            operator = stack.pop()
            
            # Evaluate based on the operator type
            if operator == '!':
                # NOT operator: invert the single operand
                result = not operands[0]
            elif operator == '&':
                # AND operator: all operands must be True
                result = all(operands)
            elif operator == '|':
                # OR operator: at least one operand must be True
                result = any(operands)
            else:
                raise ValueError(f"Unknown operator: {operator}")
            
            # Push the result back onto the stack as a character
            stack.append('t' if result else 'f')
        else:
            # Push operators, operands, and '(' onto the stack
            stack.append(char)

    # The final result is the last remaining element in the stack
    return True if stack[0] == 't' else False
