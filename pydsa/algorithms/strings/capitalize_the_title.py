METADATA = {
    "id": 2129,
    "name": "Capitalize the Title",
    "slug": "capitalize-the-title",
    "category": "String",
    "aliases": [],
    "tags": ["string_manipulation", "simulation"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Capitalize the first letter of every word in a string, provided the word length is greater than 1.",
}

def solve(s: str) -> str:
    """
    Capitalizes the first letter of every word in a string if the word length is > 1.

    Args:
        s: The input string containing words separated by single spaces.

    Returns:
        A new string where words with length > 1 have their first character capitalized.

    Examples:
        >>> solve("this is an example")
        'This Is An Example'
        >>> solve("a b c d e")
        'a b c d e'
        >>> solve("Hi There")
        'Hi There'
    """
    # Convert string to list because strings are immutable in Python
    chars = list(s)
    n = len(chars)

    for i in range(n):
        # A character should be capitalized if:
        # 1. It is the first character of the string (i == 0)
        # 2. It follows a space (chars[i-1] == ' ')
        # AND
        # 3. The word it belongs to has a length > 1. 
        # Since we only care about the first letter, we check if the NEXT 
        # character exists and is not a space.
        
        is_start_of_word = (i == 0) or (chars[i - 1] == ' ')
        
        if is_start_of_word:
            # Check if there is a character after this one and it's not a space
            # This ensures the word length is at least 2
            if i + 1 < n and chars[i + 1] != ' ':
                chars[i] = chars[i].upper()

    return "".join(chars)
