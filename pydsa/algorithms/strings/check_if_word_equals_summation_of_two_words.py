METADATA = {
    "id": 1880,
    "name": "Check if Word Equals Summation of Two Words",
    "slug": "check_if_word_equals_summation_of_two_words",
    "category": "string",
    "aliases": [],
    "tags": ["string", "two_pointer"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Determine if a target word can be formed by concatenating two words from a given set.",
}


def solve(words: list[str], target: str) -> bool:
    """Check if the target word can be expressed as the concatenation of two words.

    Args:
        words: A list of distinct words that can be used for concatenation.
        target: The word to be checked.

    Returns:
        True if there exist two words (they may be the same) whose concatenation equals
        the target, otherwise False.

    Examples:
        >>> solve(["abc","def","abcd"], "abcdef")
        True
        >>> solve(["a","b","c"], "ab")
        True
        >>> solve(["hello","world"], "helloworlds")
        False
    """
    word_set = set(words)  # O(m) extra space where m is number of words
    target_length = len(target)

    # Iterate over every possible split point (excluding empty prefix/suffix)
    for split_index in range(1, target_length):
        prefix = target[:split_index]
        suffix = target[split_index:]

        # If both parts exist in the set, the target can be formed
        if prefix in word_set and suffix in word_set:
            return True

    return False