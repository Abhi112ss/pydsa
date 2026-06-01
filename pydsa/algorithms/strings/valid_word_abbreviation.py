METADATA = {
    "id": 408,
    "name": "Valid Word Abbreviation",
    "slug": "valid_word_abbreviation",
    "category": "String",
    "aliases": ["valid-word-abbreviation"],
    "tags": ["two_pointer", "string_parsing"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Check if a given abbreviation correctly represents a word.",
}

def solve(word: str, abbr: str) -> bool:
    """Check if a given abbreviation correctly represents a word.

    Args:
        word: The original word to check against.
        abbr: The abbreviation string containing letters and numbers.

    Returns:
        True if the abbreviation is valid for the word, False otherwise.

    Examples:
        >>> solve("internationalization", "i12iz4n")
        True
        >>> solve("apple", "a2e")
        False
        >>> solve("substitution", "s10n")
        True
        >>> solve("substitution", "sub4u4")
        True
        >>> solve("substitution", "12")
        True
        >>> solve("substitution", "su3i1u2on")
        True
        >>> solve("substitution", "substitution")
        True
        >>> solve("substitution", "s010n")
        False
        >>> solve("substitution", "s0ubstitution")
        False
    """
    word_index = 0
    abbr_index = 0
    word_length = len(word)
    abbr_length = len(abbr)

    while word_index < word_length and abbr_index < abbr_length:
        if abbr[abbr_index].isdigit():
            # Leading zeros are invalid
            if abbr[abbr_index] == '0':
                return False
            
            # Parse the full number
            num = 0
            while abbr_index < abbr_length and abbr[abbr_index].isdigit():
                num = num * 10 + int(abbr[abbr_index])
                abbr_index += 1
            
            # Skip the corresponding characters in the word
            word_index += num
        else:
            # Characters must match exactly
            if word[word_index] != abbr[abbr_index]:
                return False
            word_index += 1
            abbr_index += 1

    # Both pointers should reach the end simultaneously
    return word_index == word_length and abbr_index == abbr_length