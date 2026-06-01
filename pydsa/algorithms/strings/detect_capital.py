METADATA = {
    "id": 520,
    "name": "Detect Capital",
    "slug": "detect_capital",
    "category": "String",
    "aliases": [],
    "tags": ["string", "implementation"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Check if a word uses capital letters correctly.",
}


def solve(word: str) -> bool:
    """Detect whether a word uses capital letters correctly.

    Args:
        word: The input string consisting of English letters.

    Returns:
        True if the word is either all uppercase, all lowercase,
        or only the first letter is uppercase; otherwise False.

    Examples:
        >>> solve("USA")
        True
        >>> solve("leetcode")
        True
        >>> solve("Google")
        True
        >>> solve("FlaG")
        False
    """
    # An empty string trivially satisfies the capital rules.
    if not word:
        return True

    # Check three valid patterns:
    # 1) All letters are uppercase.
    # 2) All letters are lowercase.
    # 3) Only the first letter is uppercase and the rest are lowercase.
    all_uppercase = word.isupper()
    all_lowercase = word.islower()
    first_upper_rest_lower = word[0].isupper() and word[1:].islower()

    return all_uppercase or all_lowercase or first_upper_rest_lower