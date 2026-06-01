METADATA = {
    "id": 3461,
    "name": "Check If Digits Are Equal in String After Operations I",
    "slug": "check-if-digits-are-equal-in-string-after-operations-i",
    "category": "String",
    "aliases": [],
    "tags": ["string_manipulation", "simulation"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Check if two strings contain the same sequence of digits after ignoring all non-digit characters.",
}

def solve(word1: str, word2: str) -> bool:
    """
    Determines if the sequence of digits in word1 is identical to the sequence 
    of digits in word2, ignoring all non-digit characters.

    Args:
        word1: The first input string.
        word2: The second input string.

    Returns:
        True if the extracted digit sequences are equal, False otherwise.

    Examples:
        >>> solve("a1b2c", "12")
        True
        >>> solve("abc", "def")
        True
        >>> solve("123", "12")
        False
    """
    
    def get_digit_sequence(word: str) -> list[str]:
        """Helper to extract digits from a string into a list."""
        digits = []
        for char in word:
            if char.isdigit():
                digits.append(char)
        return digits

    # Extract digits from both words
    # Note: While we use a list to store digits, the space complexity 
    # is O(n) in the worst case of all digits, but the problem 
    # logic effectively compares the streams.
    digits1 = get_digit_sequence(word1)
    digits2 = get_digit_sequence(word2)

    # Compare the resulting sequences
    return digits1 == digits2
