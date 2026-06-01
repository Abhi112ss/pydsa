METADATA = {
    "id": 12,
    "name": "Integer to Roman",
    "slug": "integer-to-roman",
    "category": "Math",
    "aliases": [],
    "tags": ["math", "string", "greedy"],
    "difficulty": "medium",
    "time_complexity": "O(1)",
    "space_complexity": "O(1)",
    "description": "Convert an integer to its Roman numeral representation using a greedy approach.",
}

def solve(num: int) -> str:
    """
    Converts an integer to a Roman numeral string.

    Args:
        num: An integer between 1 and 3999 inclusive.

    Returns:
        The Roman numeral representation of the input integer.

    Examples:
        >>> solve(3749)
        'MMMDCCXLIX'
        >>> solve(58)
        'LVIII'
        >>> solve(1994)
        'MCMXCIV'
    """
    # Mapping of Roman numeral values to their symbols in descending order.
    # We include subtractive combinations (like IV, IX, XL, etc.) to simplify the greedy logic.
    roman_mapping = [
        (1000, "M"),
        (900, "CM"),
        (500, "D"),
        (400, "CD"),
        (100, "C"),
        (90, "XC"),
        (50, "L"),
        (40, "XL"),
        (10, "X"),
        (9, "IX"),
        (5, "V"),
        (4, "IV"),
        (1, "I"),
    ]

    result_parts = []

    # Iterate through the mapping from largest value to smallest.
    for value, symbol in roman_mapping:
        # If the current value is greater than the remaining number,
        # append the symbol and subtract the value.
        if num >= value:
            count = num // value
            result_parts.append(symbol * count)
            num %= value
            
        # Optimization: if num reaches 0, we can stop early.
        if num == 0:
            break

    return "".join(result_parts)
