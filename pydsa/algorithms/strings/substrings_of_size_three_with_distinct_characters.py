METADATA = {
    "id": 1876,
    "name": "Substrings of Size Three with Distinct Characters",
    "slug": "substrings-of-size-three-with-distinct-characters",
    "category": "String",
    "aliases": [],
    "tags": ["sliding_window", "string"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Count the number of substrings of length three that consist of distinct characters.",
}

def solve(s: str) -> int:
    """
    Counts the number of substrings of length three that consist of distinct characters.

    Args:
        s: The input string.

    Returns:
        The total count of substrings of length 3 with all unique characters.

    Examples:
        >>> solve("aababcabc")
        4
        >>> solve("aabcde")
        3
        >>> solve("aaa")
        0
    """
    n = len(s)
    if n < 3:
        return 0

    distinct_substring_count = 0

    # Iterate through the string up to the point where a window of 3 can still be formed
    for i in range(n - 2):
        # Extract the current window of size 3
        char_1 = s[i]
        char_2 = s[i + 1]
        char_3 = s[i + 2]

        # Check if all three characters in the window are unique
        # Since the window size is constant (3), this check is O(1)
        if char_1 != char_2 and char_1 != char_3 and char_2 != char_3:
            distinct_substring_count += 1

    return distinct_substring_count
