METADATA = {
    "id": 8,
    "name": "String to Integer (atoi)",
    "slug": "string-to-integer-atoi",
    "category": "Implementation",
    "aliases": [],
    "tags": ["string", "math"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Convert a string to a 32-bit signed integer following specific rules for whitespace, signs, and overflow.",
}

def solve(s: str) -> int:
    """
    Converts a string to a 32-bit signed integer (atoi).

    The conversion follows these steps:
    1. Read in and ignore any leading whitespace.
    2. Check if the next character (if present) is '-' or '+'. Read this character in if it is.
    3. Read in next characters until the next non-digit character or the end of the input is reached.
    4. Convert these digits into an integer.
    5. If the integer is out of the 32-bit signed integer range [-2^31, 2^31 - 1], clamp it.

    Args:
        s: The input string to convert.

    Returns:
        The converted 32-bit signed integer.

    Examples:
        >>> solve("42")
        42
        >>> solve("   -42")
        -42
        >>> solve("4193 with words")
        4193
        >>> solve("words and 987")
        0
        >>> solve("-91283472332")
        -2147483648
    """
    # Constants for 32-bit signed integer limits
    INT_MIN = -2147483648
    INT_MAX = 2147483647

    index = 0
    n = len(s)

    # 1. Skip leading whitespace
    while index < n and s[index] == ' ':
        index += 1

    if index == n:
        return 0

    # 2. Handle sign
    sign = 1
    if s[index] == '-':
        sign = -1
        index += 1
    elif s[index] == '+':
        index += 1

    # 3. Convert digits and handle overflow
    result = 0
    while index < n and s[index].isdigit():
        digit = int(s[index])
        
        # Check for overflow before updating result
        # If result > INT_MAX // 10, adding any digit will overflow
        # If result == INT_MAX // 10, adding a digit > 7 will overflow
        if result > (INT_MAX // 10) or (result == INT_MAX // 10 and digit > 7):
            return INT_MAX if sign == 1 else INT_MIN
        
        result = result * 10 + digit
        index += 1

    return sign * result
