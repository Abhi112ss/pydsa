METADATA = {
    "id": 2243,
    "name": "Calculate Digit Sum of a String",
    "slug": "calculate-digit-sum-of-a-string",
    "category": "String",
    "aliases": [],
    "tags": ["string", "math"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Calculate the sum of all digits present in a given string.",
}

def solve(s: str) -> int:
    """
    Calculates the sum of all numeric digits present in the input string.

    Args:
        s: The input string containing characters and potentially digits.

    Returns:
        The integer sum of all digits found in the string.

    Examples:
        >>> solve("abc123def4")
        10
        >>> solve("no digits here")
        0
        >>> solve("999")
        27
    """
    digit_sum = 0
    
    for char in s:
        # Check if the character is a digit using the built-in isdigit method
        # or by checking the ASCII range '0'-'9'
        if '0' <= char <= '9':
            # Convert character to integer using ASCII offset
            # ord('0') is 48, so ord(char) - 48 gives the integer value
            digit_sum += ord(char) - ord('0')
            
    return digit_sum
