METADATA = {
    "id": 3908,
    "name": "Valid Digit Number",
    "slug": "valid_digit_number",
    "category": "String",
    "aliases": [],
    "tags": ["string_matching", "regex", "simulation"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Determine if a given string represents a valid number in scientific notation.",
}

def solve(s: str) -> bool:
    """
    Determines if the input string represents a valid number.
    
    A valid number can be:
    1. An integer (e.g., "2", "-5", "+10")
    2. A decimal (e.g., "0.1", ".5", "3.")
    3. Scientific notation (e.g., "2e10", "-1.2E-5")
    
    Rules:
    - An optional sign ('+' or '-') can precede the number.
    - A decimal point can appear at most once.
    - An exponent ('e' or 'E') can appear at most once and must be followed by an integer.
    - There must be at least one digit in the significand (the part before 'e').
    - There must be at least one digit in the exponent (the part after 'e').

    Args:
        s: The string to validate.

    Returns:
        True if the string is a valid number, False otherwise.

    Examples:
        >>> solve("0")
        True
        >>> solve(" 0.1 ")
        True
        >>> solve("abc")
        False
        >>> solve("1e10")
        True
        >>> solve("2e")
        False
        >>> solve("e3")
        False
        >>> solve("99e2.5")
        False
        >>> solve("--6")
        False
        >>> solve("-+3")
        False
        >>> solve("95a54e53")
        False
    """
    s = s.strip()
    if not s:
        return False

    has_digit = False
    has_decimal = False
    has_exponent = False

    for i, char in enumerate(s):
        if char.isdigit():
            has_digit = True
        elif char in ("+", "-"):
            # Signs can only appear at the start or immediately after an exponent
            if i > 0 and s[i - 1] not in ("e", "E"):
                return False
        elif char in ("e", "E"):
            # Exponent can only appear once and must follow at least one digit
            if has_exponent or not has_digit:
                return False
            has_exponent = True
            # Reset digit flag to ensure there is a digit after the exponent
            has_digit = False
        elif char == ".":
            # Decimal can only appear once and cannot appear after an exponent
            if has_decimal or has_exponent:
                return False
            has_decimal = True
        else:
            # Any other character is invalid
            return False

    # The string is valid only if at least one digit was found (considering the reset for exponent)
    return has_digit
