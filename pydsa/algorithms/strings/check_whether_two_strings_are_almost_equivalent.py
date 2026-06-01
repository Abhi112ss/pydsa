METADATA = {
    "id": 2068,
    "name": "Check Whether Two Strings are Almost Equivalent",
    "slug": "check_whether_two_strings_are_almost_equivalent",
    "category": "String",
    "aliases": [],
    "tags": ["hash_map", "strings"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Determine if two strings differ by at most three occurrences for each character.",
}


def solve(word1: str, word2: str) -> bool:
    """Check whether two strings are almost equivalent.

    Two strings are considered *almost equivalent* if for every lowercase English
    letter the absolute difference between its frequency in `word1` and its
    frequency in `word2` does not exceed 3.

    Args:
        word1: First input string consisting of lowercase English letters.
        word2: Second input string consisting of lowercase English letters.

    Returns:
        True if the strings are almost equivalent, otherwise False.

    Examples:
        >>> solve("abcde", "abcde")
        True
        >>> solve("aaaabb", "bbbaaa")
        True
        >>> solve("aaaa", "bbbb")
        False
    """
    # There are only 26 possible lowercase letters, so a fixed-size list suffices.
    frequency_difference: list[int] = [0] * 26

    for char1, char2 in zip(word1, word2):
        # Increment count for character from word1.
        frequency_difference[ord(char1) - ord('a')] += 1
        # Decrement count for character from word2.
        frequency_difference[ord(char2) - ord('a')] -= 1

    # Verify that no character's count difference exceeds the allowed threshold.
    for diff in frequency_difference:
        if abs(diff) > 3:
            return False
    return True