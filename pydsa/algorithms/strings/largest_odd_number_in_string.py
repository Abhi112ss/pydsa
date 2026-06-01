METADATA = {
    "id": 1903,
    "name": "Largest Odd Number in String",
    "slug": "largest-odd-number-in-string",
    "category": "String",
    "aliases": [],
    "tags": ["string_traversal", "greedy"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the largest-valued odd integer that is a non-empty substring of num, or an empty string if no odd integer exists.",
}

def solve(num: str) -> str:
    """
    Finds the largest odd number that is a substring of the given string.
    
    The largest odd number will always be a prefix of the original string 
    that ends at the rightmost odd digit.

    Args:
        num: A string representing a large integer.

    Returns:
        A string representing the largest odd number, or an empty string if none exists.

    Examples:
        >>> solve("52")
        '5'
        >>> solve("4206")
        ''
        >>> solve("35427")
        '35427'
    """
    # Iterate from the end of the string towards the beginning
    # to find the first (rightmost) odd digit.
    for index in range(len(num) - 1, -1, -1):
        # Convert character to integer and check if it is odd
        if int(num[index]) % 2 != 0:
            # The largest odd number is the substring from the start 
            # up to and including this rightmost odd digit.
            return num[:index + 1]

    # If no odd digit is found, return an empty string.
    return ""
