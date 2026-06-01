METADATA = {
    "id": 2942,
    "name": "Find Words Containing Character",
    "slug": "find-words-containing-character",
    "category": "String",
    "aliases": [],
    "tags": ["string", "array", "string_search"],
    "difficulty": "easy",
    "time_complexity": "O(n * m)",
    "space_complexity": "O(1)",
    "description": "Return the indices of words in a list that contain a specific target character.",
}

def solve(words: list[str], target: str) -> list[int]:
    """
    Finds the indices of all words in the input list that contain the target character.

    Args:
        words: A list of strings to search through.
        target: The single character to look for in each word.

    Returns:
        A list of integers representing the indices of the words containing the target.

    Examples:
        >>> solve(["leet", "code"], "e")
        [0, 1]
        >>> solve(["abc", "bcd", "aaaa", "cbc"], "a")
        [0, 2]
    """
    indices: list[int] = []

    # Iterate through the list using enumerate to track the current index
    for index, word in enumerate(words):
        # Check if the target character exists within the current word
        # The 'in' operator in Python for strings is highly optimized
        if target in word:
            indices.append(index)

    return indices
