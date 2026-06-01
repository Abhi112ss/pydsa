METADATA = {
    "id": 2315,
    "name": "Count Asterisks",
    "slug": "count-asterisks",
    "category": "String",
    "aliases": [],
    "tags": ["string", "counting"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Count the number of asterisks in a given string.",
}

def solve(s: str) -> int:
    """
    Counts the number of asterisk characters in the provided string.

    Args:
        s: The input string to process.

    Returns:
        The total count of '*' characters found in the string.

    Examples:
        >>> solve("a*b*c")
        2
        >>> solve("abc")
        0
        >>> solve("***")
        3
    """
    asterisk_count = 0
    
    # Iterate through each character in the string exactly once
    for character in s:
        # Check if the current character matches the target asterisk
        if character == '*':
            asterisk_count += 1
            
    return asterisk_count
