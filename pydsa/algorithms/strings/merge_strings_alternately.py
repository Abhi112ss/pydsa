METADATA = {
    "id": 1768,
    "name": "Merge Strings Alternately",
    "slug": "merge_strings_alternately",
    "category": "String",
    "aliases": [],
    "tags": ["two_pointer", "string"],
    "difficulty": "easy",
    "time_complexity": "O(n + m)",
    "space_complexity": "O(n + m)",
    "description": "Merge two strings by alternating characters.",
}


def solve(word1: str, word2: str) -> str:
    """Merge two strings by alternating characters.

    Args:
        word1: The first input string.
        word2: The second input string.

    Returns:
        A new string formed by alternating characters from `word1` and `word2`.
        If one string is longer, the remaining characters are appended at the end.

    Examples:
        >>> solve("abc", "pqr")
        'apbqcr'
        >>> solve("ab", "pqrs")
        'apbqrs'
    """
    # Initialize pointers for both strings
    index1: int = 0
    index2: int = 0
    merged_chars: list[str] = []

    # Alternate characters while both strings have remaining characters
    while index1 < len(word1) and index2 < len(word2):
        merged_chars.append(word1[index1])
        merged_chars.append(word2[index2])
        index1 += 1
        index2 += 1

    # Append any leftover characters from the longer string
    if index1 < len(word1):
        merged_chars.extend(word1[index1:])
    if index2 < len(word2):
        merged_chars.extend(word2[index2:])

    return "".join(merged_chars)