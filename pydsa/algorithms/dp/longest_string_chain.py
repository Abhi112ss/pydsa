METADATA = {
    "id": 1048,
    "name": "Longest String Chain",
    "slug": "longest-string-chain",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dynamic_programming", "hash_map", "sorting"],
    "difficulty": "medium",
    "time_complexity": "O(N * L^2)",
    "space_complexity": "O(N)",
    "description": "Find the length of the longest possible word chain where each word is a predecessor of the next by adding exactly one character.",
}

def solve(words: list[str]) -> int:
    """
    Finds the length of the longest string chain using dynamic programming.

    Args:
        words: A list of strings representing the available words.

    Returns:
        The length of the longest possible word chain.

    Examples:
        >>> solve(["a", "b", "ba", "bca", "bda", "bdca"])
        4
        >>> solve(["x", "xxy", "xxyy", "xy", "xyy", "xyyy"])
        4
    """
    # Sort words by length so we can build chains incrementally
    # A word can only be preceded by a word shorter than it.
    words.sort(key=len)

    # dp dictionary maps a word to the length of the longest chain ending with that word
    dp: dict[str, int] = {}
    max_chain_length = 0

    for word in words:
        # Every word is a chain of at least length 1
        current_word_max = 1
        
        # Try removing every possible character to find a predecessor
        for i in range(len(word)):
            # Create a predecessor by slicing the word to exclude the character at index i
            predecessor = word[:i] + word[i+1:]
            
            # If the predecessor exists in our dp map, update the current word's max chain
            if predecessor in dp:
                current_word_max = max(current_word_max, dp[predecessor] + 1)
        
        # Store the result for the current word
        dp[word] = current_word_max
        
        # Update the global maximum found so far
        max_chain_length = max(max_chain_length, current_word_max)

    return max_chain_length
