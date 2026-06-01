METADATA = {
    "id": 3136,
    "name": "Valid Word",
    "slug": "valid-word",
    "category": "String",
    "aliases": [],
    "tags": ["strings", "regex"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Check if a word meets specific criteria regarding length, character types, and valid characters.",
}

def solve(word: str) -> bool:
    """
    Determines if a given word is valid based on specific criteria.
    
    A word is valid if:
    1. It has at least 3 characters.
    2. It contains only digits (0-9), uppercase letters (A-Z), or lowercase letters (a-z).
    3. It contains at least one vowel (a, e, i, o, u, A, E, I, O, U).
    4. It contains at least one consonant (any letter that is not a vowel).
    5. It contains at least one digit.

    Args:
        word: The string to be validated.

    Returns:
        True if the word meets all criteria, False otherwise.

    Examples:
        >>> solve("234Adas")
        True
        >>> solve("b3")
        False
        >>> solve("a3$e")
        False
    """
    # Criterion 1: Minimum length of 3
    if len(word) < 3:
        return False

    vowels = set("aeiouAEIOU")
    has_vowel = False
    has_consonant = False
    has_digit = False

    for char in word:
        # Criterion 2: Check for valid characters (alphanumeric only)
        if not char.isalnum():
            return False
        
        if char.isdigit():
            has_digit = True
        elif char.isalpha():
            # Check if the character is a vowel or a consonant
            if char in vowels:
                has_vowel = True
            else:
                has_consonant = True
        
        # Optimization: If we found all required types, we still need to 
        # finish the loop to ensure no invalid characters (like symbols) exist.

    # Criterion 3, 4, 5: Check if all required categories were present
    return has_vowel and has_consonant and has_digit