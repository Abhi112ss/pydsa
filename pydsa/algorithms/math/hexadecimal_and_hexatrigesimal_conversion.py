METADATA = {
    "id": 3602,
    "name": "Hexadecimal and Hexatrigesimal Conversion",
    "slug": "hexadecimal-and-hexatrigesimal-conversion",
    "category": "Math",
    "aliases": [],
    "tags": ["math", "string_manipulation", "base_conversion"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Convert a string representing a number in one base to its representation in another base.",
}

def solve(num_str: str, from_base: int, to_base: int) -> str:
    """
    Converts a number string from a given base to a target base.

    Args:
        num_str: The string representation of the number in the source base.
        from_base: The base of the input string (e.g., 16 for hexadecimal).
        to_base: The base to convert the number into (e.g., 36 for hexatrigesimal).

    Returns:
        The string representation of the number in the target base.

    Examples:
        >>> solve("1A", 16, 10)
        '26'
        >>> solve("Z", 36, 16)
        '35'
    """
    # Define the character set for bases up to 36
    # 0-9 followed by A-Z
    charset = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    # Step 1: Convert the input string from from_base to a decimal integer
    # We use the positional notation formula: sum(digit * base^position)
    decimal_value = 0
    for char in num_str:
        digit_value = charset.index(char.upper())
        decimal_value = decimal_value * from_base + digit_value
        
    # Handle the case where the decimal value is 0
    if decimal_value == 0:
        return "0"
        
    # Step 2: Convert the decimal integer to the target base
    # We use the repeated division/remainder method
    result_chars = []
    while decimal_value > 0:
        remainder = decimal_value % to_base
        result_chars.append(charset[remainder])
        decimal_value //= to_base
        
    # The remainders are collected in reverse order (least significant to most)
    return "".join(reversed(result_chars))
