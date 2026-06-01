METADATA = {
    "id": 2961,
    "name": "Double Modular Exponentiation",
    "slug": "double_modular_exponentiation",
    "category": "Math",
    "aliases": [],
    "tags": ["math", "modular_arithmetic", "exponentiation"],
    "difficulty": "medium",
    "time_complexity": "O(log exponent)",
    "space_complexity": "O(1)",
    "description": "Compute (base^exponent) % modulus using efficient modular exponentiation.",
}

def solve(base: int, exponent: int, modulus: int) -> int:
    """
    Computes (base^exponent) % modulus using the binary exponentiation algorithm.

    Args:
        base: The base integer.
        exponent: The exponent integer.
        modulus: The modulus integer.

    Returns:
        The result of (base^exponent) % modulus.

    Examples:
        >>> solve(2, 10, 1000)
        24
        >>> solve(5, 3, 13)
        8
    """
    if modulus == 1:
        return 0
    
    # Handle negative base by converting to positive equivalent in modular arithmetic
    result = 1
    base = base % modulus
    
    while exponent > 0:
        # If exponent is odd, multiply the current base with the result
        if exponent % 2 == 1:
            result = (result * base) % modulus
        
        # Square the base and halve the exponent (binary exponentiation step)
        base = (base * base) % modulus
        exponent //= 2
        
    return result
