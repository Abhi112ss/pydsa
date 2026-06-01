METADATA = {
    "id": 884,
    "name": "Uncommon Words from Two Sentences",
    "slug": "uncommon_words_from_two_sentences",
    "category": "String",
    "aliases": [],
    "tags": ["hash_map"],
    "difficulty": "easy",
    "time_complexity": "O(n + m)",
    "space_complexity": "O(n + m)",
    "description": "Return all words that appear exactly once across both sentences.",
}


def solve(sentence_one: str, sentence_two: str) -> list[str]:
    """Return the list of uncommon words from two sentences.

    Args:
        sentence_one: A string containing words separated by single spaces.
        sentence_two: Another string containing words separated by single spaces.

    Returns:
        A list of words that appear exactly once across both sentences.
        The order of words in the returned list does not matter.

    Examples:
        >>> solve("this apple is sweet", "this apple is sour")
        ['sweet', 'sour']
        >>> solve("apple apple", "banana")
        ['banana']
    """
    # Split both sentences into words and count frequencies across both.
    word_counts: dict[str, int] = {}
    for word in sentence_one.split():
        word_counts[word] = word_counts.get(word, 0) + 1
    for word in sentence_two.split():
        word_counts[word] = word_counts.get(word, 0) + 1

    # Collect words whose total count is exactly one.
    uncommon_words: list[str] = [word for word, count in word_counts.items() if count == 1]
    return uncommon_words