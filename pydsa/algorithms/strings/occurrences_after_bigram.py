METADATA = {
    "id": 1078,
    "name": "Occurrences After Bigram",
    "slug": "occurrences-after-bigram",
    "category": "String",
    "aliases": [],
    "tags": ["string", "array"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Find the indices of words that immediately follow a specific pair of consecutive words in a given list.",
}

def solve(text: list[str], bigram: list[str]) -> list[int]:
    """
    Finds the indices of words that appear immediately after the specified bigram.

    Args:
        text: A list of strings representing the sequence of words.
        bigram: A list of two strings representing the target bigram.

    Returns:
        A list of integers representing the indices of the words following the bigram.

    Examples:
        >>> solve(["a", "b", "a", "c", "b"], ["a", "b"])
        [2]
        >>> solve(["a", "b", "c", "a", "b", "c"], ["a", "b"])
        [2, 5]
    """
    result_indices: list[int] = []
    
    # We iterate up to len(text) - 2 because a bigram requires at least 
    # two elements, and we need to check the element at index i + 2.
    for i in range(len(text) - 2):
        # Check if the current word and the next word match the bigram
        if text[i] == bigram[0] and text[i + 1] == bigram[1]:
            # If they match, the word following the bigram is at index i + 2
            result_indices.append(i + 2)
            
    return result_indices
