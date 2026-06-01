METADATA = {
    "id": 7,
    "name": "Reverse Integer",
    "slug": "reverse-integer",
    "category": "Math",
    "aliases": [],
    "tags": ["math"],
    "difficulty": "medium",
    "time_complexity": "O(log n)",
    "space_complexity": "O(1)",
    "description": "Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range, return 0.",
}

def solve(x: int) -> int:
    """
    Reverses the digits of a signed 32-bit integer.

    Args:
        x: A signed 32-bit integer.

    Returns:
        The reversed integer, or 0 if the reversed integer overflows 
        the signed 32-bit integer range [-2^31, 2^31 - 1].

    Examples:
        >>> solve(123)
        321
        >>> solve(-123)
        -321
        >>> solve(120)
        21
    """
    # Define the 32-bit signed integer bounds
    MIN_INT = -2**31
    MAX_INT = 2**31 - 1

    # Determine the sign and work with the absolute value
    sign = 1 if x >= 0 else -1
    current_number = abs(x)
    reversed_number = 0

    while current_number > 0:
        # Extract the last digit using modulo
        last_digit = current_number % 10
        
        # Append the digit to the reversed number
        reversed_number = (reversed_number * 10) + last_digit
        
        # Move to the next digit
        current_number //= 10

    # Re-apply the sign
    result = sign * reversed_number

    # Check if the result falls outside the 32-bit signed integer range
    if result < MIN_INT or result > MAX_INT:
        return 0

    return result
