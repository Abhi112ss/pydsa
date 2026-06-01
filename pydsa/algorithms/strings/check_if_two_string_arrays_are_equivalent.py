METADATA = {
    "id": 1662,
    "name": "Check If Two String Arrays are Equivalent",
    "slug": "check-if-two-string-arrays-are-equivalent",
    "category": "String",
    "aliases": [],
    "tags": ["string_matching", "two_pointer"],
    "difficulty": "easy",
    "time_complexity": "O(N)",
    "space_complexity": "O(1)",
    "description": "Determine if two arrays of strings are equivalent by comparing their concatenated character sequences.",
}

def solve(word1: list[str], word2: list[str]) -> bool:
    """
    Checks if two string arrays are equivalent by comparing characters sequentially.

    This implementation uses a two-pointer approach to avoid the O(N) space 
    overhead of concatenating the strings into new large strings.

    Args:
        word1: A list of strings representing the first sequence.
        word2: A list of strings representing the second sequence.

    Returns:
        True if the concatenated strings are equal, False otherwise.

    Examples:
        >>> solve(["leet", "code"], ["leet", "code"])
        True
        >>> solve(["a", "b", "c"], ["ab", "c"])
        True
        >>> solve(["a", "bc"], ["ab", "c"])
        False
    """
    # Indices for the current string in the list
    word1_idx = 0
    word2_idx = 0
    
    # Indices for the current character within the current string
    char1_idx = 0
    char2_idx = 0

    while word1_idx < len(word1) and word2_idx < len(word2):
        # Compare current characters
        if word1[word1_idx][char1_idx] != word2[word2_idx][char2_idx]:
            return False

        # Advance pointers for word1
        char1_idx += 1
        if char1_idx == len(word1[word1_idx]):
            word1_idx += 1
            char1_idx = 0

        # Advance pointers for word2
        char2_idx += 1
        if char2_idx == len(word2[word2_idx]):
            word2_idx += 1
            char2_idx = 0

    # If both arrays are fully traversed, they are equivalent
    return word1_idx == len(word1) and word2_idx == len(word2)
