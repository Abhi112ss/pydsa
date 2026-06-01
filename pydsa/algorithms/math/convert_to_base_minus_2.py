METADATA = {
    "id": 1017,
    "name": "Convert to Base -2",
    "slug": "convert-to-base-minus-two",
    "category": "Math",
    "aliases": [],
    "tags": ["math", "base_conversion"],
    "difficulty": "medium",
    "time_complexity": "O(log n)",
    "space_complexity": "O(log n)",
    "description": "Convert a non-negative integer to its representation in negabinary (base -2).",
}

def solve(n: int) -> str:
    """
    Converts a non-negative integer to its base -2 representation.

    The algorithm uses the standard division-remainder method for base conversion,
    but adjusts the remainder to ensure it is always non-negative (0 or 1),
    which is required for base -2.

    Args:
        n: A non-negative integer to convert.

    Returns:
        A string representing the base -2 version of the input integer.

    Examples:
        >>> solve(1)
        '1'
        >>> solve(2)
        '110'
        >>> solve(3)
        '111'
        >>> solve(4)
        '100'
    """
    if n == 0:
        return "0"

    digits = []
    while n > 0:
        # Standard remainder in Python for negative numbers can be tricky.
        # We need remainder r such that 0 <= r < |-2|.
        # Since |base| is 2, r must be 0 or 1.
        remainder = n % -2
        
        # If remainder is negative, adjust it to be positive.
        # Because n = quotient * (-2) + remainder, 
        # we can rewrite as n = (quotient + 1) * (-2) + (remainder + 2)
        # This keeps the equation balanced while making the remainder positive.
        if remainder < 0:
            remainder += 2
            n = (n // -2) + 1
        else:
            n = n // -2
            
        digits.append(str(remainder))

    # The digits are collected from least significant to most significant.
    return "".join(reversed(digits))
