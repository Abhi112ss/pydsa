METADATA = {
    "id": 3856,
    "name": "Trim Trailing Vowels",
    "slug": "trim_trailing_vowels",
    "category": "String",
    "aliases": [],
    "tags": ["string", "two_pointer"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Remove all vowels from the end of a given string until a non-vowel character is encountered.",
}

def solve(s: str) -> str:
    """
    Removes all trailing vowels from the input string.

    Args:
        s: The input string to be trimmed.

    Returns:
        A new string with trailing vowels removed.

    Examples:
        >>> solve("apple")
        'appl'
        >>> solve("aeiou")
        ''
        >>> solve("hello")
        'hell'
        >>> solve("sky")
        'sky'
    """
    vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    
    # Start from the end of the string and move backwards
    end_index = len(s) - 1
    
    # Find the index of the last character that is not a vowel
    while end_index >= 0 and s[end_index] in vowels:
        end_index -= 1
        
    # If end_index is -1, it means the entire string consisted of vowels
    # Otherwise, return the substring up to and including the last non-vowel
    return s[:end_index + 1]
