METADATA = {
    "id": 3368,
    "name": "First Letter Capitalization",
    "slug": "first-letter-capitalization",
    "category": "String",
    "aliases": [],
    "tags": ["string_manipulation"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Capitalize the first letter of every word in a given string.",
}

def solve(text: str) -> str:
    """
    Capitalizes the first letter of every word in the input string.
    A word is defined as a sequence of characters following a space or 
    starting at the beginning of the string.

    Args:
        text: The input string to process.

    Returns:
        A new string where the first letter of each word is capitalized.

    Examples:
        >>> solve("hello world")
        'Hello World'
        >>> solve("a b c")
        'A B C'
        >>> solve("leetcode is fun")
        'Leetcode Is Fun'
    """
    if not text:
        return ""

    # Convert string to list because strings are immutable in Python
    result_chars = list(text)
    
    # Flag to track if the next character encountered should be capitalized
    # Initialized to True to handle the very first character of the string
    capitalize_next = True

    for index in range(len(result_chars)):
        current_char = result_chars[index]

        if current_char == " ":
            # If we encounter a space, the next non-space character must be capitalized
            capitalize_next = True
        elif capitalize_next:
            # Capitalize the character if the flag is set and it's not a space
            result_chars[index] = current_char.upper()
            capitalize_next = False
        else:
            # Ensure other characters are lowercase if the problem implies strict title case
            # Note: Standard 'capitalize' logic usually keeps existing casing, 
            # but for strict word-start capitalization, we only modify the target.
            # We follow the prompt's logic: "capitalize characters that follow a space or index 0"
            pass

    return "".join(result_chars)
