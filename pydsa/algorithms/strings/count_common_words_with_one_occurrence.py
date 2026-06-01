METADATA = {
    "id": 2085,
    "name": "Count Common Words With One Occurrence",
    "slug": "count-common-words-with-one-occurrence",
    "category": "Hash Table",
    "aliases": [],
    "tags": ["string", "hash_map"],
    "difficulty": "medium",
    "time_complexity": "O(n + m)",
    "space_complexity": "O(n + m)",
    "description": "Count how many words appear exactly once in both word1 and word2.",
}

def solve(word1: list[str], word2: list[str]) -> int:
    """
    Counts the number of words that appear exactly once in both word1 and word2.

    Args:
        word1: A list of strings representing the first collection of words.
        word2: A list of strings representing the second collection of words.

    Returns:
        The integer count of words that have a frequency of exactly 1 in both lists.

    Examples:
        >>> solve(["a", "a"], ["b", "b"])
        0
        >>> solve(["a", "b", "c"], ["b", "c", "d"])
        2
        >>> solve(["a", "b", "c"], ["a", "b", "c"])
        3
    """
    # Frequency maps to store the count of each word in both lists
    counts_word1: dict[str, int] = {}
    counts_word2: dict[str, int] = {}

    # Populate the frequency map for the first list
    for word in word1:
        counts_word1[word] = counts_word1.get(word, 0) + 1

    # Populate the frequency map for the second list
    for word in word2:
        counts_word2[word] = counts_word2.get(word, 0) + 1

    common_single_occurrence_count = 0

    # Iterate through the keys of the first map to find common words
    # that satisfy the 'exactly one occurrence' condition in both maps
    for word, count in counts_word1.items():
        if count == 1:
            # Check if the word exists in the second map and has a count of exactly 1
            if counts_word2.get(word) == 1:
                common_single_occurrence_count += 1

    return common_single_occurrence_count
