METADATA = {
    "id": 830,
    "name": "Positions of Large Groups",
    "slug": "positions_of_large_groups",
    "category": "string",
    "aliases": [],
    "tags": ["two_pointer", "array"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the start and end indices of all groups of three or more consecutive identical characters in a string.",
}

def solve(s: str) -> list[list[int]]:
    """Find the start and end indices of all large groups in a string.

    Args:
        s: The input string consisting of lowercase English letters.

    Returns:
        A list of [start, end] pairs where each pair represents a group of
        three or more consecutive identical characters. The pairs are ordered
        by their appearance in the string.

    Examples:
        >>> solve("abbxxxxzyy")
        [[3, 6]]
        >>> solve("abc")
        []
        >>> solve("abcdddeeeeaabbbcd")
        [[3, 5], [6, 9], [12, 14]]
    """
    result: list[list[int]] = []
    start: int = 0  # start index of the current character block

    for index in range(len(s) + 1):
        # When we reach the end or encounter a different character,
        # the current block ends at index - 1.
        if index == len(s) or s[index] != s[start]:
            block_length: int = index - start
            if block_length >= 3:
                result.append([start, index - 1])  # record large group
            start = index  # begin a new block

    return result