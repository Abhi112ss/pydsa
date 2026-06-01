METADATA = {
    "id": 1455,
    "name": "Check If a Word Occurs As a Prefix of Any Word in a Sentence",
    "slug": "check-if-a-word-occurs-as-a-prefix-of-any-word-in-a-sentence",
    "category": "String",
    "aliases": [],
    "tags": ["string", "search"],
    "difficulty": "easy",
    "time_complexity": "O(N * M)",
    "space_complexity": "O(N)",
    "description": "Determine if a given prefix exists at the start of any word within a space-separated sentence.",
}

def solve(sentence: str, word: str) -> bool:
    """
    Checks if the given word is a prefix of any word in the sentence.

    Args:
        sentence: A space-separated string of words.
        word: The prefix string to search for.

    Returns:
        True if 'word' is a prefix of any word in 'sentence', False otherwise.

    Examples:
        >>> solve("blue is sky", "bl")
        True
        >>> solve("blue is sky", "sk")
        True
        >>> solve("blue is sky", "blue")
        True
        >>> solve("blue is sky", "is ")
        False
        >>> solve("blue is sky", "sky ")
        False
    """
    # Split the sentence into individual words based on whitespace
    words_in_sentence = sentence.split()

    # Iterate through each word to check the prefix condition
    for current_word in words_in_sentence:
        # Use the built-in startswith method for efficient prefix checking
        if current_word.startswith(word):
            return True

    return False
