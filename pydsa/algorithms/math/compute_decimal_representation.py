METADATA = {
    "id": 3697,
    "name": "Compute Decimal Representation",
    "slug": "compute_decimal_representation",
    "category": "Math",
    "aliases": [],
    "tags": ["math", "bit_manipulation"],
    "difficulty": "easy",
    "time_complexity": "O(log n)",
    "space_complexity": "O(1)",
    "description": "Convert a number represented in a given base into its decimal equivalent.",
}

def solve(digits: list[int], base: int) -> int:
    """
    Computes the decimal representation of a number given its digits and base.

    Args:
        digits: A list of integers representing the digits of the number in the given base.
        base: The base of the number system.

    Returns:
        The decimal (base 10) integer representation of the input digits.

    Raises:
        ValueError: If any digit is not within the valid range [0, base - 1].

    Examples:
        >>> solve([1, 0, 1], 2)
        5
        >>> solve([1, 2, 3], 10)
        123
        >>> solve([A, B], 16) # where A=10, B=11
        171
    """
    decimal_value = 0
    
    for digit in digits:
        # Validate that the digit is valid for the given base
        if not (0 <= digit < base):
            raise ValueError(f"Digit {digit} is invalid for base {base}")
            
        # Horner's method: multiply current total by base and add the new digit
        # This avoids calculating powers of the base explicitly
        decimal_value = (decimal_value * base) + digit
        
    return decimal_value
