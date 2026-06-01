METADATA = {
    "id": 472,
    "name": "Concatenated Words",
    "slug": "concatenated-words",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dynamic_programming", "trie", "dfs", "hash_table"],
    "difficulty": "hard",
    "time_complexity": "O(N * L^3)",
    "space_complexity": "O(N * L)",
    "description": "Find all words in a list that are formed by concatenating at least two shorter words from the same list.",
}

def solve(words: list[str]) -> list[str]:
    """
    Finds all words in the input list that are formed by concatenating 
    at least two other words from the same list.

    Args:
        words: A list of strings to evaluate.

    Returns:
        A list of strings that are concatenated words.

    Examples:
        >>> solve(["cat", "cats", "catsdogcats", "dog", "dogcatsdog", "catsdog"])
        ['catsdogcats', 'dogcatsdog', 'catsdog']
    """
    # Use a set for O(1) average time complexity lookups
    word_set = set(words)
    result = []

    # Memoization dictionary to store results of sub-problems
    # memo[word] = True if word can be formed by other words in the set
    memo: dict[str, bool] = {}

    def can_form(word: str, original_word: str) -> bool:
        """
        Helper function using memoized DFS to check if a word can be 
        decomposed into words present in the word_set.
        """
        if word in memo:
            return memo[word]
        
        # Try every possible split point for the current word
        for i in range(1, len(word) + 1):
            prefix = word[:i]
            suffix = word[i:]

            # A word is valid if the prefix is in the set AND
            # (the suffix is in the set OR the suffix can be further decomposed)
            # We must ensure we don't count the word itself as its own component
            if prefix in word_set and prefix != original_word:
                if not suffix or suffix in word_set:
                    memo[word] = True
                    return True
                
                if can_form(suffix, original_word):
                    memo[word] = True
                    return True
        
        memo[word] = False
        return False

    for word in words:
        # Reset memo for each word to ensure 'original_word' constraint is handled
        # or use a more robust memoization strategy. 
        # Here, we clear memo to keep the logic simple and correct.
        memo.clear()
        if can_form(word, word):
            result.append(word)

    return result
