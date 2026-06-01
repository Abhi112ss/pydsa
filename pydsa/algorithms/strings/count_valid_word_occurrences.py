METADATA = {
    "id": 3926,
    "name": "Count Valid Word Occurrences",
    "slug": "count-valid-word-occurrences",
    "category": "String",
    "aliases": [],
    "tags": ["string", "hash_map"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(m)",
    "description": "Count the occurrences of specific valid words within a given string after tokenization.",
}

import re

def solve(text: str, valid_words: list[str]) -> int:
    """
    Counts how many times words from a valid_words list appear in the text.

    Args:
        text: The input string containing words and potentially other characters.
        valid_words: A list of strings representing the words to count.

    Returns:
        The total count of occurrences of all valid words found in the text.

    Examples:
        >>> solve("hello world hello", ["hello", "world"])
        3
        >>> solve("apple, banana! apple", ["apple", "orange"])
        2
    """
    # Create a frequency map for the valid words for O(1) lookup
    # and to handle potential duplicates in the valid_words list if necessary.
    # However, the problem usually implies counting occurrences of the set.
    # We use a dictionary to store the target words.
    target_counts = {}
    for word in valid_words:
        target_counts[word] = target_counts.get(word, 0) + 1

    # Use regex to find all sequences of alphanumeric characters (tokens)
    # This handles punctuation and whitespace automatically.
    tokens = re.findall(r'\w+', text)

    total_occurrences = 0
    
    # Iterate through the tokens and check if they exist in our target map
    for token in tokens:
        if token in target_counts:
            total_occurrences += 1

    return total_occurrences
