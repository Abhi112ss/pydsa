METADATA = {
    "id": 3726,
    "name": "Remove Zeros in Decimal Representation",
    "slug": "remove_zeros_in_decimal_representation",
    "category": "Math",
    "aliases": [],
    "tags": ["math", "string_manipulation"],
    "difficulty": "easy",
    "time_complexity": "O(log n)",
    "space_complexity": "O(log n)",
    "description": "Given a non-negative integer, return the integer formed by removing all zeros from its decimal representation.",
}

def solve(n: int) -> int:
    """
    Removes all zero digits from the decimal representation of a given integer.

    Args:
        n: A non-negative integer.

    Returns:
        An integer formed by concatenating the non-zero digits of n.
        If all digits are zero, returns 0.

    Examples:
        >>> solve(10203)
        123
        >>> solve(0)
        0
        >>> solve(500)
        5
    """
    # Convert the integer to a string to iterate through digits
    digit_string = str(n)
    
    # Filter out all '0' characters using a generator expression
    non_zero_digits = "".join(char for char in digit_string if char != '0')
    
    # If the resulting string is empty (e.g., input was 0 or 000), return 0
    if not non_zero_digits:
        return 0
        
    # Convert the filtered string back to an integer
    return int(non_zero_digits)
