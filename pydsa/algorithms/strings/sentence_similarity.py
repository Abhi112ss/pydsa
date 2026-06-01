METADATA = {
    "id": 734,
    "name": "Sentence Similarity",
    "slug": "sentence_similarity",
    "category": "Hash Table",
    "aliases": [],
    "tags": ["hash_map", "hash_set"],
    "difficulty": "easy",
    "time_complexity": "O(n + p)",
    "space_complexity": "O(p)",
    "description": "Determine if two sentences are similar based on given similar word pairs.",
}


def solve(sentence1: list[str], sentence2: list[str], similar_pairs: list[list[str]]) -> bool:
    """Determine whether two sentences are similar.

    Args:
        sentence1: List of words representing the first sentence.
        sentence2: List of words representing the second sentence.
        similar_pairs: List of word pairs that are considered similar (bidirectional).

    Returns:
        True if the sentences are similar, False otherwise.

    Examples:
        >>> solve(["great","acting","skills"], ["fine","drama","talent"], [["great","fine"],["acting","drama"],["skills","talent"]])
        True
        >>> solve(["great"], ["great"], [])
        True
        >>> solve(["great"], ["good"], [])
        False
    """
    # Sentences must have the same length to be comparable.
    if len(sentence1) != len(sentence2):
        return False

    # Store each similar pair as an unordered frozenset for O(1) lookup.
    similar_set: set[frozenset[str]] = set()
    for first_word, second_word in similar_pairs:
        similar_set.add(frozenset((first_word, second_word)))

    # Compare words at each position.
    for index in range(len(sentence1)):
        word_a = sentence1[index]
        word_b = sentence2[index]
        if word_a == word_b:
            continue
        # If not equal, check if the unordered pair exists in the similarity set.
        if frozenset((word_a, word_b)) not in similar_set:
            return False

    return True