METADATA = {
    "id": 1935,
    "name": "Maximum Number of Words You Can Type",
    "slug": "maximum_number_of_words_you_can_type",
    "category": "algorithms",
    "aliases": [],
    "tags": ["strings", "hash_set"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(k)",
    "description": "Count how many words in a sentence can be typed without using any broken letters.",
}


def solve(text: str, broken_letters: list[str]) -> int:
    """Return the number of words that can be typed without using broken letters.

    Args:
        text: A sentence consisting of words separated by single spaces.
        broken_letters: A list of characters that are broken on the keyboard.

    Returns:
        The count of words that do not contain any broken character.

    Examples:
        >>> solve("hello world", ["w"])
        1
        >>> solve("leet code", ["e", "t"])
        0
    """
    # Convert broken letters to a set for O(1) membership checks.
    broken_set = set(broken_letters)

    # Split the sentence into individual words.
    words = text.split()

    # Count words that have no intersection with the broken set.
    typed_word_count = 0
    for word in words:
        # If none of the characters in the word are broken, it can be typed.
        if all(character not in broken_set for character in word):
            typed_word_count += 1
    return typed_word_count