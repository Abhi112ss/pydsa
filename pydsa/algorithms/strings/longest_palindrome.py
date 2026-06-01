METADATA = {
    "id": 409,
    "name": "Longest Palindrome",
    "slug": "longest_palindrome",
    "category": "String",
    "aliases": [],
    "tags": ["greedy", "hash_table"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Return the maximum length of a palindrome that can be built from the given characters.",
}

def solve(s: str) -> int:
    """Calculate the length of the longest palindrome that can be formed from the characters of *s*.

    Args:
        s: A string consisting of uppercase and/or lowercase English letters.

    Returns:
        The length of the longest possible palindrome.

    Examples:
        >>> solve("abccccdd")
        7
        >>> solve("a")
        1
        >>> solve("Aa")
        1
    """
    # Count occurrences of each character.
    char_counts: dict[str, int] = {}
    for ch in s:
        char_counts[ch] = char_counts.get(ch, 0) + 1

    palindrome_length = 0
    odd_found = False

    # Add the largest even contribution of each character.
    for count in char_counts.values():
        even_part = (count // 2) * 2
        palindrome_length += even_part
        if count % 2 == 1:
            odd_found = True

    # If any character has an odd count, we can place exactly one in the center.
    if odd_found and palindrome_length % 2 == 0:
        palindrome_length += 1

    return palindrome_length