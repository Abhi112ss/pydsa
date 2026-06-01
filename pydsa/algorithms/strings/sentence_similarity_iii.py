METADATA = {
    "id": 1813,
    "name": "Sentence Similarity III",
    "slug": "sentence-similarity-iii",
    "category": "Two Pointers",
    "aliases": [],
    "tags": ["two_pointer", "strings", "array"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Determine if two sentences are similar by checking if one can be transformed into the other by removing words from the beginning or the end.",
}

def solve(sentence1: list[str], sentence2: list[str]) -> bool:
    """
    Determines if two sentences are similar by allowing removals from the start or end.

    Args:
        sentence1: A list of strings representing the first sentence.
        sentence2: A list of strings representing the second sentence.

    Returns:
        True if one sentence can be transformed into the other by removing words 
        from the prefix or suffix, False otherwise.

    Examples:
        >>> solve(["great", "acting", "roles"], ["great", "roles"])
        True
        >>> solve(["great", "acting", "roles"], ["acting"])
        False
    """
    n1 = len(sentence1)
    n2 = len(sentence2)

    # If the lengths are different, one must be a sub-segment of the other.
    # We identify which sentence is the shorter one to facilitate comparison.
    if n1 < n2:
        short_sentence, long_sentence = sentence1, sentence2
    else:
        short_sentence, long_sentence = sentence2, sentence1

    # If the shorter sentence is longer than the target, it's impossible.
    # (Though based on problem constraints, the shorter one is always <= the longer one).
    if len(short_sentence) > len(long_sentence):
        return False

    left = 0
    right_short = len(short_sentence) - 1
    right_long = len(long_sentence) - 1

    # Step 1: Match words from the beginning (prefix)
    while left < len(short_sentence) and short_sentence[left] == long_sentence[left]:
        left += 1

    # Step 2: Match words from the end (suffix)
    # We use the remaining available words from the end of both sentences.
    while right_short >= left and short_sentence[right_short] == long_sentence[right_long]:
        right_short -= 1
        right_long -= 1

    # If the pointers met or crossed, it means all words in the shorter sentence 
    # were matched as either part of a prefix or a suffix of the longer sentence.
    return left > right_short
