METADATA = {
    "id": 266,
    "name": "Palindrome Permutation",
    "slug": "palindrome_permutation",
    "category": "Algorithms",
    "aliases": ["palindrome-permutation"],
    "tags": ["hash_map", "strings"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Given a string, determine if a permutation of the string could form a palindrome.",
}

def solve(s: str) -> bool:
    """Determine if any permutation of the string can form a palindrome.

    A string can be rearranged into a palindrome if and most one character
    has an odd frequency (the middle character in odd-length palindromes).

    Args:
        s: The input string to check.

    Returns:
        True if some permutation of s is a palindrome, False otherwise.

    Examples:
        >>> solve("code")
        False
        >>> solve("aab")
        True
        >>> solve("carerac")
        True
        >>> solve("")
        True
        >>> solve("a")
        True
    """
    # Count character frequencies using a fixed-size array for lowercase letters
    char_counts = [0] * 128  # ASCII range covers all standard characters

    for char in s:
        char_counts[ord(char)] ^= 1  # Toggle between 0 and 1 (odd/even tracking)

    # A palindrome allows at most one character with an odd count
    odd_count = sum(char_counts)

    return odd_count <= 1