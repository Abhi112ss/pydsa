METADATA = {
    "id": 816,
    "name": "Ambiguous Coordinates",
    "slug": "ambiguous-coordinates",
    "category": "String",
    "aliases": [],
    "tags": ["string_manipulation", "backtracking"],
    "difficulty": "hard",
    "time_complexity": "O(n^3)",
    "space_complexity": "O(n^3)",
    "description": "Find all possible (x, y) coordinates that can be formed by inserting a decimal point into two given strings.",
}

def solve(x_str: str, y_str: str) -> list[list[float]]:
    """
    Finds all possible (x, y) coordinates by inserting a decimal point into x_str and y_str.

    A number is valid if:
    1. It contains exactly one decimal point.
    2. It does not have leading zeros (unless the number is just '0').
    3. It does not have trailing zeros after the decimal point (unless the number is '0').
    Wait, the actual rule for this problem is:
    - A number is valid if it doesn't have leading zeros (e.g., "01" is invalid, "0" is valid).
    - A number is valid if it doesn't have trailing zeros after the decimal point (e.g., "1.0" is invalid, "1" is valid).
    Actually, the rule is:
    - No leading zeros: "0.1" is okay, "01.1" is not. "0" is okay.
    - No trailing zeros after decimal: "1.10" is not okay, "1.1" is okay. "1.0" is not okay.

    Args:
        x_str: The string representing the x-coordinate.
        y_str: The string representing the y-coordinate.

    Returns:
        A list of lists, where each inner list is a valid [x, y] coordinate.

    Examples:
        >>> solve("123", "456")
        [[1.23, 4.56], [1.23, 45.6], [12.3, 4.56], [12.3, 45.6]]
        >>> solve("0", "0")
        []
    """

    def get_valid_numbers(s: str) -> list[float]:
        """Helper to find all valid float representations of a string."""
        valid_nums = []
        n = len(s)
        
        # Try inserting a decimal point at every possible position
        # i represents the index where the decimal point will be placed
        for i in range(1, n):
            integer_part = s[:i]
            fractional_part = s[i:]

            # Rule 1: No leading zeros in the integer part unless the integer part is just "0"
            if len(integer_part) > 1 and integer_part[0] == '0':
                continue
            
            # Rule 2: No trailing zeros in the fractional part
            if fractional_part[-1] == '0':
                continue
            
            # If both rules pass, the number is valid
            valid_nums.append(float(s[:i] + "." + s[i:]))
            
        return valid_nums

    # Generate all valid x values and y values independently
    valid_x = get_valid_numbers(x_str)
    valid_y = get_valid_numbers(y_str)

    # Combine all valid x and y values into coordinate pairs
    # Using a nested loop to create the Cartesian product
    result = []
    for x in valid_x:
        for y in valid_y:
            result.append([x, y])
            
    return result
