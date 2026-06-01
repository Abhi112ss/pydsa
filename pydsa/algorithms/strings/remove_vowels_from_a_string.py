METADATA = {
    "id": 1119,
    "name": "Remove Vowels from a String",
    "slug": "remove_vowels_from_a_string",
    "category": "String",
    "aliases": [],
    "tags": ["strings", "hash_set"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Return a new string with all vowels (a, e, i, o, u) removed from the input.",
}


def solve(input_string: str) -> str:
    """Remove all vowels from the given string.

    Args:
        input_string: The original string that may contain vowels.

    Returns:
        A new string consisting of the original characters except for
        'a', 'e', 'i', 'o', and 'u'.

    Examples:
        >>> solve("leetcode")
        'ltcd'
        >>> solve("AEIOUxyz")
        'AEIOUxyz'  # only lowercase vowels are removed
    """
    vowels = {"a", "e", "i", "o", "u"}  # constant lookup set
    result_characters = []  # list for efficient concatenation

    for character in input_string:
        # Append only if the character is not a lowercase vowel
        if character not in vowels:
            result_characters.append(character)

    return "".join(result_characters)