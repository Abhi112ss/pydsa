METADATA = {
    "id": 521,
    "name": "Longest Uncommon Subsequence I",
    "slug": "longest_uncommon_subsequence_i",
    "category": "String",
    "aliases": [],
    "tags": ["string_manipulation"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the longest uncommon subsequence between two strings.",
}

def solve(a: str, b: str) -> int:
    """Find the length of the longest uncommon subsequence between two strings.

    Args:
        a (str): The first string.
        b (str): The second string.

    Returns:
        int: The length of the longest uncommon subsequence, or -1 if none exists.

    Examples:
        >>> solve("aba", "cdc")
        3
        >>> solve("aaa", "aaa")
        -1
        >>> solve("aefawfawfawfaw", "aefawfeawfwafwaef")
        17
    """
    # If the strings are identical, no uncommon subsequence exists
    if a == b:
        return -1
    
    # The longer string itself is the longest uncommon subsequence
    return max(len(a), len(b))