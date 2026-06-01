METADATA = {
    "id": 336,
    "name": "Palindrome Pairs",
    "slug": "palindrome-pairs",
    "category": "String",
    "aliases": [],
    "tags": ["hash_map", "trie", "string"],
    "difficulty": "hard",
    "time_complexity": "O(n * k^2)",
    "space_complexity": "O(n * k)",
    "description": "Find all pairs of unique indices (i, j) such that the concatenation of words[i] and words[j] is a palindrome.",
}

def solve(words: list[str]) -> list[list[int]]:
    """
    Finds all pairs of indices in the words list that form a palindrome when concatenated.

    Args:
        words: A list of strings.

    Returns:
        A list of lists, where each sub-list contains two indices [i, j] 
        such that words[i] + words[j] is a palindrome.

    Examples:
        >>> solve(["abcd", "dcba", "lls", "s", "sssll"])
        [[0, 1], [1, 0], [3, 2], [2, 4]]
        >>> solve(["a", ""])
        [[0, 1], [1, 0]]
    """
    word_to_index: dict[str, int] = {word: i for i, word in enumerate(words)}
    results: list[list[int]] = []

    def is_palindrome(s: str) -> bool:
        return s == s[::-1]

    for i, word in enumerate(words):
        n = len(word)
        # We iterate through all possible split points of the current word.
        # A split point 'j' divides the word into prefix: word[:j] and suffix: word[j:]
        for j in range(n + 1):
            prefix = word[:j]
            suffix = word[j:]

            # Case 1: If the prefix is a palindrome, we need to find if the 
            # reverse of the suffix exists in the dictionary. 
            # If it does, then (reversed_suffix + prefix + suffix) is a palindrome.
            # Since prefix is already a palindrome, this is (reversed_suffix + word).
            if is_palindrome(prefix):
                reversed_suffix = suffix[::-1]
                if reversed_suffix in word_to_index and word_to_index[reversed_suffix] != i:
                    results.append([word_to_index[reversed_suffix], i])

            # Case 2: If the suffix is a palindrome, we need to find if the
            # reverse of the prefix exists in the dictionary.
            # If it does, then (prefix + suffix + reversed_prefix) is a palindrome.
            # Since suffix is already a palindrome, this is (word + reversed_prefix).
            # Note: j > 0 prevents double counting the case where prefix is empty (already handled in Case 1)
            if j < n and is_palindrome(suffix):
                reversed_prefix = prefix[::-1]
                if reversed_prefix in word_to_index and word_to_index[reversed_prefix] != i:
                    results.append([i, word_to_index[reversed_prefix]])

    return results
