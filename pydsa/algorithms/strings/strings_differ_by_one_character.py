METADATA = {
    "id": 1554,
    "name": "Strings Differ by One Character",
    "slug": "strings-differ-by-one-character",
    "category": "Hash Table",
    "aliases": [],
    "tags": ["hash_map", "strings", "pattern_matching"],
    "difficulty": "medium",
    "time_complexity": "O(n * L)",
    "space_complexity": "O(n * L)",
    "description": "Find the number of pairs of strings that differ by exactly one character.",
}

def solve(words: list[str]) -> int:
    """
    Calculates the number of pairs of strings in the list that differ by exactly one character.

    The algorithm uses a pattern-based approach. For each word, we generate all possible
    patterns by replacing one character at a time with a wildcard (e.g., 'aba' -> ['*ba', 'a*a', 'ab*']).
    We count the occurrences of these patterns using a hash map. If a pattern appears K times,
    it means there are K(K-1)/2 pairs of words that share that specific pattern.

    Args:
        words: A list of strings of equal length.

    Returns:
        The total number of pairs of strings that differ by exactly one character.

    Examples:
        >>> solve(["aba", "aca", "aaa"])
        2
        >>> solve(["abc", "abc"])
        1
        >>> solve(["a", "b", "c"])
        0
    """
    if not words:
        return 0

    word_length = len(words[0])
    pattern_counts: dict[str, int] = {}
    total_pairs = 0

    for word in words:
        # For each position in the word, create a pattern with a wildcard
        for i in range(word_length):
            # Construct the pattern: prefix + wildcard + suffix
            pattern = word[:i] + "*" + word[i+1:]
            
            # If this pattern has been seen before, every previous occurrence 
            # forms a valid pair with the current word.
            if pattern in pattern_counts:
                total_pairs += pattern_counts[pattern]
                pattern_counts[pattern] += 1
            else:
                pattern_counts[pattern] = 1

    return total_pairs
