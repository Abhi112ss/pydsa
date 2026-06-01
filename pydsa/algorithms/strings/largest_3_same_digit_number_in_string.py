METADATA = {
    "id": 2264,
    "name": "Largest 3-Same-Digit Number in String",
    "slug": "largest-3-same-digit-number-in-string",
    "category": "String",
    "aliases": [],
    "tags": ["string_traversal", "greedy"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the largest three-digit number consisting of only one unique digit that appears as a substring in the given string.",
}

def solve(num: str) -> str:
    """
    Finds the largest three-digit number consisting of only one unique digit 
    that appears as a substring in the input string.

    Args:
        num: A string representing a large integer.

    Returns:
        A string representing the largest 3-same-digit number, or an empty 
        string if no such number exists.

    Examples:
        >>> solve("6777133339")
        '777'
        >>> solve("2300019")
        '000'
        >>> solve("42352338")
        ''
    """
    max_digit = -1
    n = len(num)

    # Iterate through the string up to the third to last character
    for i in range(n - 2):
        # Check if the current character and the next two are identical
        if num[i] == num[i + 1] == num[i + 2]:
            # Convert the character to an integer to compare magnitude
            current_digit = int(num[i])
            if current_digit > max_digit:
                max_digit = current_digit

    # If no triplet was found, return an empty string
    if max_digit == -1:
        return ""

    # Return the digit repeated three times as a string
    return str(max_digit) * 3
