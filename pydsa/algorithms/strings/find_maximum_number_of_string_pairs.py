METADATA = {
    "id": 2744,
    "name": "Find Maximum Number of String Pairs",
    "slug": "find-maximum-number-of-string-pairs",
    "category": "Hash Table",
    "aliases": [],
    "tags": ["hash_map", "strings", "array"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Find the maximum number of pairs of strings in an array such that the strings are reverses of each other.",
}

def solve(words: list[str]) -> int:
    """
    Finds the maximum number of pairs (words[i], words[j]) such that 
    words[i] is the reverse of words[j] and i < j.

    Args:
        words: A list of strings.

    Returns:
        The total number of pairs found.

    Examples:
        >>> solve(["lc", "cl", "gg"])
        1
        >>> solve(["ab", "ba", "cd", "dc"])
        2
        >>> solve(["apple", "apple"])
        0
    """
    seen_words: set[str] = set()
    pair_count: int = 0

    for word in words:
        # Calculate the reverse of the current word
        reversed_word: str = word[::-1]

        # If the reverse has been seen before, we found a valid pair
        if reversed_word in seen_words:
            pair_count += 1
            # We remove the reversed word to ensure each word is used in at most one pair
            # However, the problem constraints/logic for this specific LeetCode problem 
            # usually imply we are looking for unique index pairs (i, j).
            # Since we iterate once, checking 'if reversed_word in seen_words' 
            # and then adding the current word handles the 'i < j' condition perfectly.
            seen_words.remove(reversed_word)
        else:
            # Otherwise, add the current word to the set to look for its partner later
            seen_words.add(word)

    return pair_count
