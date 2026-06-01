METADATA = {
    "id": 2023,
    "name": "Number of Pairs of Strings With Concatenation Equal to Target",
    "slug": "number-of-pairs-of-strings-with-concatenation-equal-to-target",
    "category": "Hash Table",
    "aliases": [],
    "tags": ["hash_map", "string_matching"],
    "difficulty": "medium",
    "time_complexity": "O(n * m)",
    "space_complexity": "O(n)",
    "description": "Count pairs of strings from an array that, when concatenated, form a target string.",
}

def solve(words: list[str], target: str) -> int:
    """
    Counts the number of pairs (i, j) such that words[i] + words[j] == target.

    Args:
        words: A list of strings to search through.
        target: The target string to form by concatenation.

    Returns:
        The total number of pairs that satisfy the condition.

    Examples:
        >>> solve(["a", "b", "c", "ab"], "abc")
        2
        >>> solve(["a", "b", "c", "ab"], "ab")
        1
    """
    # Count occurrences of each word to handle duplicates efficiently
    word_counts: dict[str, int] = {}
    for word in words:
        word_counts[word] = word_counts.get(word, 0) + 1

    pair_count = 0
    target_length = len(target)

    # Iterate through all possible split points of the target string.
    # A split point 'i' defines the prefix target[0:i] and suffix target[i:target_length].
    # The split point must result in non-empty strings, so i ranges from 1 to target_length - 1.
    for i in range(1, target_length):
        prefix = target[:i]
        suffix = target[i:]

        # If both the prefix and suffix exist in our word frequency map,
        # the number of pairs formed by these specific strings is count(prefix) * count(suffix).
        if prefix in word_counts and suffix in word_counts:
            pair_count += word_counts[prefix] * word_counts[suffix]

    return pair_count
