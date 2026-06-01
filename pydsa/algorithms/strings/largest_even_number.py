METADATA = {
    "id": 3798,
    "name": "Largest Even Number",
    "slug": "largest_even_number",
    "category": "Strings",
    "aliases": [],
    "tags": ["strings", "greedy"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the largest even number that can be formed as a prefix of the given string.",
}

def solve(num: str) -> str:
    """
    Finds the largest even number that can be formed by taking a prefix of the input string.

    The largest even number formed by a prefix will be the prefix that ends at the 
    rightmost even digit in the string.

    Args:
        num: A string representing a large non-negative integer.

    Returns:
        A string representing the largest even number, or an empty string if no even number exists.

    Examples:
        >>> solve("52")
        '52'
        >>> solve("42")
        '42'
        >>> solve("423")
        '42'
        >>> solve("35427")
        '42'
        >>> solve("353")
        ''
    """
    # Iterate from the end of the string to find the first (rightmost) even digit
    for index in range(len(num) - 1, -1, -1):
        # Convert character to integer to check parity
        if int(num[index]) % 2 == 0:
            # The largest even number is the prefix ending at this index
            return num[:index + 1]

    # If no even digit is found, return an empty string
    return ""
