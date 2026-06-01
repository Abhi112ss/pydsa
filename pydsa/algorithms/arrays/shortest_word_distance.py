METADATA = {
    "id": 243,
    "name": "Shortest Word Distance",
    "slug": "shortest-word-distance",
    "category": "Array",
    "aliases": [],
    "tags": ["two_pointer", "array_traversal"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the shortest distance between two given words in an array of strings.",
}

def solve(words: list[str], word1: str, word2: str) -> int:
    """
    Finds the minimum distance between two words in a list of strings.

    Args:
        words: A list of strings containing the target words.
        word1: The first target word.
        word2: The second target word.

    Returns:
        The smallest index difference between occurrences of word1 and word2.

    Examples:
        >>> solve(["practice", "makes", "perfect", "coding", "makes"], "makes", "coding")
        1
        >>> solve(["a", "b", "c", "a"], "a", "c")
        2
    """
    # Initialize indices to -1 to represent that the words haven't been found yet
    index1: int = -1
    index2: int = -1
    min_distance: int = len(words)

    for current_index, word in enumerate(words):
        if word == word1:
            index1 = current_index
        elif word == word2:
            index2 = current_index

        # If both words have been encountered at least once, calculate distance
        if index1 != -1 and index2 != -1:
            # Update the minimum distance found so far
            current_distance = abs(index1 - index2)
            if current_distance < min_distance:
                min_distance = current_distance
                
            # Optimization: if distance is 1, it's the smallest possible
            if min_distance == 1:
                return 1

    return min_distance
