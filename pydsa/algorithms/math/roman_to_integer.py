METADATA = {
    "id": 13,
    "name": "Roman to Integer",
    "slug": "roman-to-integer",
    "category": "String",
    "aliases": [],
    "tags": ["math", "string", "hash_map"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Convert a Roman numeral string to its corresponding integer value.",
}

def solve(s: str) -> int:
    """
    Converts a Roman numeral string to an integer.

    The algorithm iterates through the string and compares the current numeral 
    with the next one. If the current numeral is smaller than the next, 
    it indicates a subtraction case (e.g., IV = 4). Otherwise, it is an 
    addition case.

    Args:
        s (str): A string representing a Roman numeral.

    Returns:
        int: The integer representation of the Roman numeral.

    Examples:
        >>> solve("III")
        3
        >>> solve("LVIII")
        58
        >>> solve("MCMXCIV")
        1994
    """
    roman_map: dict[str, int] = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    }

    total_value: int = 0
    n: int = len(s)

    for index in range(n):
        current_val: int = roman_map[s[index]]

        # If this is not the last character and the current value is less 
        # than the next value, we subtract the current value (subtraction rule).
        if index + 1 < n and current_val < roman_map[s[index + 1]]:
            total_value -= current_val
        else:
            # Otherwise, we simply add the value to the total.
            total_value += current_val

    return total_value
