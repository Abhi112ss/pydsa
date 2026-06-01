METADATA = {
    "id": 1056,
    "name": "Confusing Number",
    "slug": "confusing-number",
    "category": "Math",
    "aliases": [],
    "tags": ["math", "string_manipulation"],
    "difficulty": "easy",
    "time_complexity": "O(log n)",
    "space_complexity": "O(1)",
    "description": "Determine if a number is confusing, meaning its digits can be rotated to form a different number using specific digit mappings.",
}

def solve(n: int) -> bool:
    """
    Determines if a number is a 'confusing number'.
    
    A number is confusing if every digit can be rotated (0->0, 1->1, 6->9, 8->8, 9->6)
    and the resulting number is different from the original. If any digit cannot 
    be rotated (2, 3, 4, 5, 7), it is not confusing.

    Args:
        n: The integer to check.

    Returns:
        True if the number is confusing, False otherwise.

    Examples:
        >>> solve(6)
        True
        >>> solve(89)
        True
        >>> solve(2)
        False
        >>> solve(11)
        False
    """
    # Mapping of valid rotations. 
    # 0, 1, 8 map to themselves. 6 maps to 9, 9 maps to 6.
    rotation_map = {
        '0': '0',
        '1': '1',
        '6': '9',
        '8': '8',
        '9': '6'
    }
    
    original_str = str(n)
    rotated_chars = []
    
    for digit in original_str:
        # If a digit is not in our map, it cannot be rotated.
        if digit not in rotation_map:
            return False
        rotated_chars.append(rotation_map[digit])
    
    # Join the rotated digits to form the new number string.
    rotated_str = "".join(rotated_chars)
    
    # A number is confusing only if the rotated version is numerically different.
    # Note: Leading zeros in the rotated string are handled correctly by int() conversion.
    return int(rotated_str) != n
