METADATA = {
    "id": 1668,
    "name": "Maximum Repeating Substring",
    "slug": "maximum_repeating_substring",
    "category": "String",
    "aliases": ["maxRepeating"],
    "tags": ["string", "string_matching"],
    "difficulty": "easy",
    "time_complexity": "O(n^2)",
    "space_complexity": "O(1)",
    "description": "Find the maximum number of consecutive repetitions of a pattern that appears as a substring in a given word.",
}


def solve(word: str, pattern: str) -> int:
    """Return the maximum k such that pattern repeated k times is a substring of word.

    Args:
        word: The string in which to search for repeated patterns.
        pattern: The pattern string to be repeated.

    Returns:
        The largest integer k where pattern * k is a substring of word.
        Returns 0 if pattern does not appear in word.

    Examples:
        >>> solve("ababc", "ab")
        2
        >>> solve("ababc", "ba")
        1
        >>> solve("ababc", "ac")
        0
    """
    # If the pattern is longer than the word, it cannot repeat even once.
    if len(pattern) > len(word):
        return 0

    max_repeat = 0
    repeat = 1
    # Continue while the repeated pattern fits within the word length and is found.
    while len(pattern) * repeat <= len(word) and pattern * repeat in word:
        max_repeat = repeat
        repeat += 1

    return max_repeat