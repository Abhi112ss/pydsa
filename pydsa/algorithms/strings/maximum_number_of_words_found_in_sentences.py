METADATA = {
    "id": 2114,
    "name": "Maximum Number of Words Found in Sentences",
    "slug": "maximum-number-of-words-found-in-sentences",
    "category": "String",
    "aliases": [],
    "tags": ["string", "arrays"],
    "difficulty": "easy",
    "time_complexity": "O(n * m)",
    "space_complexity": "O(1)",
    "description": "Find the maximum number of words in any given sentence from a list of sentences.",
}

def solve(sentences: list[str]) -> int:
    """
    Calculates the maximum number of words found in any single sentence within the list.

    Args:
        sentences: A list of strings where each string represents a sentence.

    Returns:
        The maximum number of words found in any sentence.

    Examples:
        >>> solve(["alice and bob love leetcode", "i love leetcode"])
        5
        >>> solve(["hello", "world"])
        1
    """
    max_word_count = 0

    for sentence in sentences:
        # A sentence's word count is the number of spaces + 1, 
        # provided the sentence is not empty.
        # Alternatively, using split() handles multiple spaces and empty strings robustly.
        current_word_count = len(sentence.split())
        
        # Update the global maximum if the current sentence has more words
        if current_word_count > max_word_count:
            max_word_count = current_word_count

    return max_word_count
