METADATA = {
    "id": 166,
    "name": "Fraction to Recurring Decimal",
    "slug": "fraction-to-recurring-decimal",
    "category": "Math",
    "aliases": [],
    "tags": ["hash_map", "math", "string_manipulation"],
    "difficulty": "medium",
    "time_complexity": "O(denominator)",
    "space_complexity": "O(denominator)",
    "description": "Convert a fraction into its decimal representation, using parentheses to denote repeating digits.",
}

def solve(numerator: int, denominator: int) -> str:
    """
    Args:
        numerator: The integer numerator of the fraction.
        denominator: The integer denominator of the fraction.

    Returns:
        A string representing the decimal form of the fraction.
    """
    if numerator == 0:
        return "0"

    result_parts = []

    if (numerator < 0) ^ (denominator < 0):
        result_parts.append("-")

    numerator = abs(numerator)
    denominator = abs(denominator)

    integer_part = numerator // denominator
    remainder = numerator % denominator
    result_parts.append(str(integer_part))

    if remainder == 0:
        return "".join(result_parts)

    result_parts.append(".")
    remainder_map = {}

    while remainder != 0:
        if remainder in remainder_map:
            decimal_start_index = remainder_map[remainder]
            decimal_string = "".join(result_parts)
            result_parts.insert(decimal_start_index, "(")
            result_parts.append(")")
            break

        remainder_map[remainder] = len(result_parts)
        remainder *= 10
        digit = remainder // denominator
        result_parts.append(str(digit))
        remainder %= denominator

    return "".join(result_parts)