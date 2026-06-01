METADATA = {
    "id": 224,
    "name": "Basic Calculator",
    "slug": "basic_calculator",
    "category": "Stack",
    "aliases": [],
    "tags": ["stack", "math", "recursion"],
    "difficulty": "hard",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Evaluate a basic expression string containing non-negative integers, +, -, (, ), and spaces.",
}


def solve(s: str) -> int:
    """Evaluate a basic expression string with +, -, (, ), integers, and spaces.

    Uses a stack to save the current accumulated result and sign before
    entering a parenthesis, then restores them when the parenthesis closes.

    Args:
        s: A valid expression string containing non-negative integers,
           ``+``, ``-``, ``(``, ``)``, and spaces.

    Returns:
        The integer result of evaluating the expression.

    Examples:
        >>> solve("1 + 1")
        2
        >>> solve(" 2-1 + 2 ")
        3
        >>> solve("(1+(4+5+2)-3)+(6+8)")
        23
    """
    stack: list[int] = []
    result: int = 0
    sign: int = 1  # current sign: 1 for positive, -1 for negative
    index: int = 0
    length: int = len(s)

    while index < length:
        character: str = s[index]

        if character.isdigit():
            # Parse the full multi-digit number
            number: int = 0
            while index < length and s[index].isdigit():
                number = number * 10 + int(s[index])
                index += 1
            result += sign * number
            continue  # index already advanced past the number

        elif character == "+":
            sign = 1
        elif character == "-":
            sign = -1
        elif character == "(":
            # Push current result and sign onto the stack, then reset
            stack.append(result)
            stack.append(sign)
            result = 0
            sign = 1
        elif character == ")":
            # result inside parentheses is complete; combine with outer context
            open_sign: int = stack.pop()   # sign before '('
            prev_result: int = stack.pop()  # result accumulated before '('
            result = prev_result + open_sign * result

        # Skip spaces and any other characters
        index += 1

    return result