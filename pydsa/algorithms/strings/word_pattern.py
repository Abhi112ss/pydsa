METADATA = {
    "id": 290,
    "name": "Word Pattern",
    "slug": "word_pattern",
    "category": "String",
    "aliases": [],
    "tags": ["hash_map", "string_parsing"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Determine if a string follows a given pattern by establishing a bijection between pattern characters and words.",
}


def solve(pattern: str, s: str) -> bool:
    """Determine whether the string ``s`` follows the same pattern as ``pattern``.

    Args:
        pattern: A string consisting of lowercase letters representing the pattern.
        s: A space‑separated string of words.

    Returns:
        True if there exists a bijective mapping between characters in ``pattern`` and
        words in ``s`` such that the sequence of words matches the sequence of pattern
        characters; otherwise False.

    Examples:
        >>> solve("abba", "dog cat cat dog")
        True
        >>> solve("abba", "dog cat cat fish")
        False
        >>> solve("aaaa", "dog dog dog dog")
        True
        >>> solve("abc", "b c a")
        True
    """
    # Split the input string into individual words.
    words: list[str] = s.split()
    # The pattern and the list of words must have the same length to be comparable.
    if len(pattern) != len(words):
        return False

    # Dictionaries to enforce a bijection between pattern characters and words.
    char_to_word: dict[str, str] = {}
    word_to_char: dict[str, str] = {}

    for index, (char, word) in enumerate(zip(pattern, words)):
        # If the character has been seen before, it must map to the same word.
        if char in char_to_word:
            if char_to_word[char] != word:
                return False
        else:
            char_to_word[char] = word

        # Similarly, if the word has been seen before, it must map to the same character.
        if word in word_to_char:
            if word_to_char[word] != char:
                return False
        else:
            word_to_char[word] = char

    return True