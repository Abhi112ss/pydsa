METADATA = {
    "id": 3749,
    "name": "Evaluate Valid Expressions",
    "slug": "evaluate-valid-expressions",
    "category": "Stack",
    "aliases": [],
    "tags": ["stack", "parsing", "expression-evaluation"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Evaluate a mathematical expression containing numbers, basic operators, and parentheses using a stack-based approach.",
}

def solve(expression: str) -> int:
    """
    Evaluates a mathematical expression containing integers, '+', '-', '*', '/', and '()'.

    Args:
        expression: A string representing the mathematical expression.

    Returns:
        The integer result of the evaluated expression.

    Examples:
        >>> solve("3 + (2 * 4) - 5")
        6
        >>> solve("10 / (2 + 3)")
        2
    """
    # Helper to perform arithmetic operations
    def apply_operator(operators: list[str], values: list[int]) -> None:
        if len(values) < 2:
            return
        right = values.pop()
        left = values.pop()
        op = operators.pop()
        
        if op == '+':
            values.append(left + right)
        elif op == '-':
            values.append(left - right)
        elif op == '*':
            values.append(left * right)
        elif op == '/':
            # Using integer division as per standard LeetCode expression problems
            values.append(int(left / right))

    # Precedence mapping
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2}
    
    values: list[int] = []
    operators: list[str] = []
    i = 0
    n = len(expression)

    while i < n:
        char = expression[i]

        if char == ' ':
            i += 1
            continue

        # Parse multi-digit integers
        if char.isdigit():
            num = 0
            while i < n and expression[i].isdigit():
                num = num * 10 + int(expression[i])
                i += 1
            values.append(num)
            continue

        # Handle opening parenthesis
        elif char == '(':
            operators.append(char)
        
        # Handle closing parenthesis: evaluate everything inside
        elif char == ')':
            while operators and operators[-1] != '(':
                apply_operator(operators, values)
            operators.pop()  # Remove '('
        
        # Handle operators
        elif char in precedence:
            # While top of stack has higher or equal precedence, evaluate it
            while (operators and operators[-1] in precedence and 
                   precedence[operators[-1]] >= precedence[char]):
                apply_operator(operators, values)
            operators.append(char)
        
        i += 1

    # Final evaluation for remaining operators in stack
    while operators:
        apply_operator(operators, values)

    return values[0]
