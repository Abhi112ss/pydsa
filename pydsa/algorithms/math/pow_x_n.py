METADATA = {
    "id": 50,
    "name": "Pow(x, n)",
    "slug": "pow_x_n",
    "category": "Math",
    "aliases": [],
    "tags": ["recursion", "binary_exponentiation", "math"],
    "difficulty": "medium",
    "time_complexity": "O(log n)",
    "space_complexity": "O(log n)",
    "description": "Implement pow(x, n), which calculates x raised to the power n.",
}

def solve(x: float, n: int) -> float:
    """
    Calculates x raised to the power n using the binary exponentiation algorithm.

    Args:
        x: The base float value.
        n: The exponent integer value.

    Returns:
        The result of x raised to the power n.

    Examples:
        >>> solve(2.0, 10)
        1024.0
        >>> solve(2.1, 3)
        9.261000000000001
        >>> solve(2.0, -2)
        0.25
    """
    # Handle the negative exponent case by converting to positive
    # and taking the reciprocal at the end.
    is_negative = n < 0
    exponent = abs(n)
    base = x

    result = 1.0
    
    # Iterative Binary Exponentiation (Exponentiation by Squaring)
    # This reduces the complexity from O(n) to O(log n)
    while exponent > 0:
        # If the current exponent bit is 1, multiply the result by the current base
        if exponent % 2 == 1:
            result *= base
        
        # Square the base and integer-divide the exponent by 2
        base *= base
        exponent //= 2

    return 1.0 / result if is_negative else result
