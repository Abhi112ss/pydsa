METADATA = {
    "id": 2506,
    "name": "Count Pairs Of Similar Strings",
    "slug": "count-pairs-of-similar-strings",
    "category": "Hash Table",
    "aliases": [],
    "tags": ["hash_map", "sorting", "string"],
    "difficulty": "easy",
    "time_complexity": "O(n * k log k)",
    "space_complexity": "O(n * k)",
    "description": "Count the number of pairs of strings in an array that contain the same set of unique characters.",
}

def solve(words: list[str]) -> int:
    """
    Counts the number of pairs (i, j) such that words[i] and words[j] 
    contain the exact same set of unique characters.

    Args:
        words: A list of strings to evaluate.

    Returns:
        The total number of similar pairs.

    Examples:
        >>> solve(["aba", "zxy", "abc", "ba"])
        1
        >>> solve(["abcd", "dcba", "cbad", "abcd"])
        6
    """
    # Map to store the frequency of each unique character set representation
    # We represent the set of characters as a sorted string to make it hashable
    signature_counts: dict[str, int] = {}
    total_pairs: int = 0

    for word in words:
        # Extract unique characters and sort them to create a canonical signature
        # This ensures that "aba" and "ba" both result in "ab"
        unique_chars = sorted(set(word))
        signature = "".join(unique_chars)

        # If we have seen this signature before, every previous occurrence 
        # can form a new pair with the current word.
        if signature in signature_counts:
            current_count = signature_counts[signature]
            total_pairs += current_count
            signature_counts[signature] = current_count + 1
        else:
            signature_counts[signature] = 1

    return total_pairs
