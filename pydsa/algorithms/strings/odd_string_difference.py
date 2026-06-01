METADATA = {
    "id": 2451,
    "name": "Odd String Difference",
    "slug": "odd-string-difference",
    "category": "Strings",
    "aliases": [],
    "tags": ["strings", "math"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Calculate the absolute difference between the sums of ASCII values of characters at odd indices of two strings.",
}

def solve(word1: str, word2: str) -> int:
    """
    Calculates the absolute difference between the sums of ASCII values 
    of characters at odd indices for two given strings.

    Args:
        word1: The first input string.
        word2: The second input string.

    Returns:
        The absolute difference between the sum of ASCII values of 
        characters at odd indices of word1 and word2.

    Examples:
        >>> solve("abc", "def")
        # word1 odd indices: 'b' (98)
        # word2 odd indices: 'e' (101)
        # abs(98 - 101) = 3
        3
        >>> solve("aaaa", "bbbb")
        # word1 odd indices: 'a' (97), 'a' (97) -> sum 194
        # word2 odd indices: 'b' (98), 'b' (98) -> sum 196
        # abs(194 - 196) = 2
        2
    """
    sum_odd_word1 = 0
    sum_odd_word2 = 0

    # Iterate through word1 using a step of 2 starting from index 1
    for index in range(1, len(word1), 2):
        sum_odd_word1 += ord(word1[index])

    # Iterate through word2 using a step of 2 starting from index 1
    for index in range(1, len(word2), 2):
        sum_odd_word2 += ord(word2[index])

    # Return the absolute difference between the two calculated sums
    return abs(sum_odd_word1 - sum_odd_word2)
