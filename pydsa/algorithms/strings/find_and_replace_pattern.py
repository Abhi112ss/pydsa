METADATA = {
    "id": 890,
    "name": "Find and Replace Pattern",
    "slug": "find-and-replace-pattern",
    "category": "Hash Table",
    "aliases": [],
    "tags": ["hash_map", "string", "bijection"],
    "difficulty": "medium",
    "time_complexity": "O(N * K)",
    "space_complexity": "O(K)",
    "description": "Determine if there exists a bijection between the characters of a pattern and the characters of words in a list.",
}

def solve(words: list[str], pattern: str) -> list[str]:
    """
    Finds all words in the list that match the given pattern based on a bijection.

    A bijection means that each character in the pattern maps to exactly one 
    unique character in the word, and vice versa.

    Args:
        words: A list of strings to be checked against the pattern.
        pattern: The pattern string to match against.

    Returns:
        A list of strings from 'words' that follow the same character pattern.

    Examples:
        >>> solve(["dog", "cat", "zb", "zaz", "zbz"], "abb")
        ['zbz']
        >>> solve(["abc", "def", "ghi"], "abc")
        ['abc', 'def', 'ghi']
    """
    def matches_pattern(word: str, pattern: str) -> bool:
        # Since all strings are guaranteed to be the same length by problem constraints
        # (implied by the pattern length), we can use two maps to ensure bijection.
        char_to_pattern = {}
        pattern_to_char = {}

        for char_w, char_p in zip(word, pattern):
            # Check if the mapping from word character to pattern character is consistent
            if char_w in char_to_pattern:
                if char_to_pattern[char_w] != char_p:
                    return False
            else:
                char_to_pattern[char_w] = char_p

            # Check if the mapping from pattern character to word character is consistent
            # This ensures the mapping is injective (one-to-one)
            if char_p in pattern_to_char:
                if pattern_to_char[char_p] != char_w:
                    return False
            else:
                pattern_to_char[char_p] = char_w

        return True

    result = []
    for word in words:
        # Only words of the same length as the pattern can match
        if len(word) == len(pattern):
            if matches_pattern(word, pattern):
                result.append(word)
                
    return result
