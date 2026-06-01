METADATA = {
    "id": 2186,
    "name": "Minimum Number of Steps to Make Two Strings Anagram II",
    "slug": "minimum-number-of-steps-to-make-two-strings-anagram-ii",
    "category": "String",
    "aliases": [],
    "tags": ["hash_map", "string", "frequency_counter"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the minimum number of characters to replace in one string to make it an anagram of another string of the same length.",
}

def solve(s: str, t: str) -> int:
    """
    Calculates the minimum number of character replacements needed to make s an anagram of t.

    Args:
        s: The first input string.
        t: The second input string.

    Returns:
        The minimum number of steps (replacements) required.

    Examples:
        >>> solve("lold", "hold")
        1
        >>> solve("anagram", "mangaar")
        0
        >>> solve("aabb", "bbaa")
        0
        >>> solve("leetcode", "practice")
        5
    """
    # Since the alphabet size is constant (26 lowercase English letters),
    # the space complexity is O(1).
    char_counts = [0] * 26

    # Count frequencies of characters in the first string
    for char in s:
        char_counts[ord(char) - ord('a')] += 1

    # Subtract frequencies of characters in the second string
    for char in t:
        char_counts[ord(char) - ord('a')] -= 1

    # The number of steps is the sum of positive differences.
    # A positive difference means 's' has more of this character than 't'.
    # Since len(s) == len(t), the sum of positive differences equals 
    # the sum of negative differences (the number of characters to replace).
    steps = 0
    for count in char_counts:
        if count > 0:
            steps += count

    return steps
