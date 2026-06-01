METADATA = {
    "id": 772,
    "name": "Basic Calculator III",
    "slug": "basic-calculator-iii",
    "category": "Stack",
    "aliases": [],
    "tags": ["stack", "recursion", "math", "parsing"],
    "difficulty": "hard",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Evaluate a mathematical expression string containing non-negative integers, '+', '-', '*', '/', and parentheses.",
}

def solve(expression: str) -> int:
    """
    Evaluates a mathematical expression string with '+', '-', '*', '/', and '()'.

    Args:
        expression: A string representing the mathematical expression.

    Returns:
        The integer result of the evaluation.

    Examples:
        >>> solve("1 + 1")
        2
        >>> solve(" 2 * (5 + 5 * 2) / 3 ")
        6
        >>> solve("(1+(4+5+2)-3)+(6+8)")
        23
    """
    # Pointer to track current position in the string across recursive calls
    index = 0

    def compute() -> int:
        nonlocal index
        stack: list[int] = []
        current_number = 0
        last_operator = '+'

        while index < len(expression):
            char = expression[index]

            # Handle digits: build the multi-digit integer
            if char.isdigit():
                current_number = current_number * 10 + int(char)

            # Handle nested expressions: recurse when encountering '('
            elif char == '(':
                index += 1
                current_number = compute()

            # Handle operators or end of expression/sub-expression
            if char in "+-*/)" or index == len(expression) - 1:
                # If it's the last char and a digit, we must process it
                if index == len(expression) - 1 and char.isdigit():
                    pass 
                
                # Apply precedence: multiplication and division happen immediately
                if last_operator == '+':
                    stack.append(current_number)
                elif last_operator == '-':
                    stack.append(-current_number)
                elif last_operator == '*':
                    stack.append(stack.pop() * current_number)
                elif last_operator == '/':
                    # Python's // operator behaves differently for negative numbers
                    # (e.g., -3 // 2 is -2, but we need -1 for truncation towards zero)
                    prev_val = stack.pop()
                    if prev_val < 0:
                        stack.append(-(-prev_val // current_number))
                    else:
                        stack.append(prev_val // current_number)

                # Reset for next number
                last_operator = char
                current_number = 0

                # If we hit a closing parenthesis, return the sum of the current stack
                if char == ')':
                    return sum(stack)

            index += 1
        
        return sum(stack)

    # Clean whitespace to simplify parsing logic
    expression = expression.replace(" ", "")
    return compute()
