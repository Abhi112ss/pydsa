METADATA = {
    "id": 2828,
    "name": "Check if a String Is an Acronym of Words",
    "slug": "check-if-a-string-is-an-acronym-of-words",
    "category": "String",
    "aliases": [],
    "tags": ["strings", "two_pointer"],
    "difficulty": "easy",
    "time_complexity": "O(N)",
    "space_complexity": "O(1)",
    "description": "Determine if a given string is an acronym formed by the first character of each word in a provided list.",
}

def solve(acronym: str, words: list[str]) -> bool:
    """
    Checks if the given string is an acronym of the provided list of words.

    An acronym is formed by taking the first character of each word in the list
    in the order they appear.

    Args:
        acronym: The string to check against the words.
        words: A list of strings representing the words to derive the acronym from.

    Returns:
        True if the string is an acronym of the words, False otherwise.

    Examples:
        >>> solve("apple", ["apple", "pie", "eat", "lemon", "eat"])
        True
        >>> solve("apple", ["apple", "pie", "eat"])
        False
    """
    # If the lengths don't match, it cannot be an acronym
    if len(acronym) != len(words):
        return False

    # Iterate through both the acronym and the words list simultaneously
    for index in range(len(acronym)):
        # Check if the character in the acronym matches the first character of the current word
        # We use index 0 of words[index] to get the first character
        if acronym[index] != words[index][0]:
            return False

    return True
