METADATA = {
    "id": 29,
    "name": "Divide Two Integers",
    "slug": "divide-two-integers",
    "category": "Math",
    "aliases": [],
    "tags": ["bit_manipulation", "math"],
    "difficulty": "medium",
    "time_complexity": "O(log N)",
    "space_complexity": "O(1)",
    "description": "Divide two integers without using multiplication, division, or the mod operator.",
}

def solve(dividend: int, divisor: int) -> int:
    """
    Divides two integers using bitwise manipulation to achieve O(log N) time complexity.

    Args:
        dividend: The number to be divided.
        divisor: The number to divide by.

    Returns:
        The quotient of the division, clamped within the 32-bit signed integer range [-2^31, 2^31 - 1].

    Examples:
        >>> solve(10, 3)
        3
        >>> solve(7, -3)
        -2
        >>> solve(0, 1)
        0
    """
    # Constants for 32-bit signed integer limits
    INT_MAX = 2147483647
    INT_MIN = -2147483648

    # Handle overflow case: -2^31 / -1 would be 2^31, which exceeds INT_MAX
    if dividend == INT_MIN and divisor == -1:
        return INT_MAX

    # Determine the sign of the result
    # If signs are different, the result is negative
    is_negative = (dividend < 0) != (divisor < 0)

    # Work with absolute values to simplify bitwise logic
    # Note: Using abs() is safe here because we handled the overflow case above
    abs_dividend = abs(dividend)
    abs_divisor = abs(divisor)

    quotient = 0

    # Use bitwise shifts to find the largest multiple of divisor (divisor * 2^n)
    # that is less than or equal to the remaining dividend.
    while abs_dividend >= abs_divisor:
        temp_divisor = abs_divisor
        multiple = 1
        
        # Double the divisor using left shift until it's larger than the dividend
        while abs_dividend >= (temp_divisor << 1):
            temp_divisor <<= 1
            multiple <<= 1
        
        # Subtract the largest found multiple from dividend and add multiple to quotient
        abs_dividend -= temp_divisor
        quotient += multiple

    # Apply the sign and return
    result = -quotient if is_negative else quotient
    
    # Final clamp (though the overflow case above handles the primary edge case)
    return max(INT_MIN, min(INT_MAX, result))
