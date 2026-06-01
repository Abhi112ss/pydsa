METADATA = {
    "id": 150,
    "name": "Evaluate Reverse Polish Notation",
    "slug": "evaluate-reverse-polish-notation",
    "category": "Stack",
    "aliases": [],
    "tags": ["stack", "math"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Evaluate the value of an arithmetic expression in Reverse Polish Notation using a stack.",
}

def solve(tokens: list[str]) -> int:
    """
    Evaluates an arithmetic expression in Reverse Polish Notation (RPN).

    In RPN, operators follow their operands. For example, "2 1 + 3 *" 
    is evaluated as (2 + 1) * 3 = 9.

    Args:
        tokens: A list of strings representing the RPN expression.

    Returns:
        The integer result of the evaluation.

    Examples:
        >>> solve(["2", "1", "+", "3", "*"])
        9
        >>> solve(["4", "13", "5", "/", "+"])
        6
        >>> solve(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"])
        22
    """
    stack: list[int] = []
    
    # Define operators and their corresponding lambda functions
    # Note: Integer division in Python (//) behaves differently for negative numbers 
    # than C++/Java (truncation towards zero). We use int(a / b) to ensure 
    # truncation towards zero as required by LeetCode/standard RPN rules.
    operators = {
        "+": lambda a, b: a + b,
        "-": lambda a, b: a - b,
        "*": lambda a, b: a * b,
        "/": lambda a, b: int(a / b)
    }

    for token in tokens:
        if token in operators:
            # Pop the two most recent operands. 
            # The second operand popped is the left-hand side of the operation.
            right_operand = stack.pop()
            left_operand = stack.pop()
            
            # Apply the operator and push the result back onto the stack
            result = operators[token](left_operand, right_operand)
            stack.append(result)
        else:
            # Token is a number, convert to integer and push to stack
            stack.append(int(token))

    # The final remaining element in the stack is the result
    return stack[0]
