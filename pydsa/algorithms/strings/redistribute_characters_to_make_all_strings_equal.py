METADATA = {
    "id": 1897,
    "name": "Redistribute Characters to Make All Strings Equal",
    "slug": "redistribute-characters-to-make-all-strings-equal",
    "category": "Hash Table",
    "aliases": [],
    "tags": ["hash_map", "strings", "counting"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Determine if characters from a list of strings can be redistributed so that every string contains the same number of each character.",
}

def solve(words: list[str]) -> bool:
    """
    Determines if characters from a list of strings can be redistributed 
    so that every string contains the same number of each character.

    Args:
        words: A list of strings to redistribute.

    Returns:
        True if redistribution is possible, False otherwise.

    Examples:
        >>> solve(["a", "a", "a"])
        True
        >>> solve(["a", "b", "c"])
        False
        >>> solve(["aac", "aca", "caa"])
        True
    """
    if not words:
        return True

    num_strings = len(words)
    # Frequency map for all characters across all words
    # Since we only deal with lowercase English letters, size is fixed at 26
    total_counts = [0] * 26

    for word in words:
        for char in word:
            # Map 'a'-'z' to index 0-25
            total_counts[ord(char) - ord('a')] += 1

    # Check if every character's total count is divisible by the number of strings
    for count in total_counts:
        if count % num_strings != 0:
            return False

    return True
