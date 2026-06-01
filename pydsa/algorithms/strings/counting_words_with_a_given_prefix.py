METADATA = {
    "id": 2185,
    "name": "Counting Words With a Given Prefix",
    "slug": "counting-words-with-a-given-prefix",
    "category": "String",
    "aliases": [],
    "tags": ["string_matching", "trie"],
    "difficulty": "easy",
    "time_complexity": "O(n * m)",
    "space_complexity": "O(1)",
    "description": "Count how many strings in a given array start with a specific prefix.",
}

def solve(words: list[str], prefix: str) -> int:
    """
    Counts the number of strings in the words list that start with the given prefix.

    Args:
        words: A list of strings to search through.
        prefix: The prefix string to match against.

    Returns:
        The total count of words that start with the specified prefix.

    Examples:
        >>> solve(["leet", "code"], "leet")
        1
        >>> solve(["apple", "pen", "apple", "apple", "ap", "apply", "apple"], "appl")
        3
        >>> solve(["a", "b", "c"], "d")
        0
    """
    count = 0
    prefix_length = len(prefix)

    for word in words:
        # Check if the current word is long enough to contain the prefix
        # and if the substring matches the prefix.
        # Python's startswith is highly optimized for this operation.
        if word.startswith(prefix):
            count += 1

    return count
