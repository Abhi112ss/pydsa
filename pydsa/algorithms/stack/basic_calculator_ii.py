METADATA = {
    "id": 227,
    "name": "Basic Calculator II",
    "slug": "basic_calculator_ii",
    "category": "Math",
    "aliases": [],
    "tags": ["stack", "math", "string"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Evaluate a basic arithmetic expression string containing non-negative integers, +, -, *, / operators, and spaces.",
}


def solve(s: str) -> int:
    """Evaluate a basic arithmetic expression with +, -, *, / operators.

    Processes the expression left to right, using a stack to handle operator
    precedence: multiplication and division are evaluated immediately, while
    addition and subtraction are deferred by pushing values onto the stack.

    Args:
        s: A string containing a valid arithmetic expression with non-negative
           integers, operators (+, -, *, /), and spaces.

    Returns:
        The integer result of the evaluated expression. Division truncates
        toward zero.

    Examples:
        >>> solve("3+2*2")
        7
        >>> solve(" 3/2 ")
        1
        >>> solve(" 3+5 / 2 ")
        5
        >>> solve("14-3/2")
        13
    """
    stack: list[int] = []
    current_number = 0
    # Track the last operator seen; start with '+' so the first number is pushed.
    last_operator = "+"
    # Append a sentinel operator to trigger processing of the final number.
    s = s + "+"

    for char in s:
        if char.isdigit():
            # Build multi-digit numbers by shifting left and adding the new digit.
            current_number = current_number * 10 + int(char)
        elif char == " ":
            continue
        else:
            # Process the completed number based on the previous operator.
            if last_operator == "+":
                stack.append(current_number)
            elif last_operator == "-":
                stack.append(-current_number)
            elif last_operator == "*":
                # Pop the last value, multiply, and push the result back.
                stack.append(stack.pop() * current_number)
            elif last_operator == "/":
                # Pop the last value, divide with truncation toward zero, and push.
                previous_value = stack.pop()
                # Python's // rounds toward negative infinity, so we use int() to truncate toward zero.
                stack.append(int(previous_value / current_number))

            # Reset for the next number and update the operator.
            last_operator = char
            current_number = 0

    # The sum of the stack gives the final result.
    return sum(stack)