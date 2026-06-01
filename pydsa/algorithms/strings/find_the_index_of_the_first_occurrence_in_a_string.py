METADATA = {
    "id": 28,
    "name": "Find the Index of the First Occurrence in a String",
    "slug": "find-the-index-of-the-first-occurrence-in-a-string",
    "category": "String",
    "aliases": ["strStr"],
    "tags": ["string_matching", "two_pointer"],
    "difficulty": "easy",
    "time_complexity": "O(n * m)",
    "space_complexity": "O(1)",
    "description": "Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.",
}

def solve(haystack: str, needle: str) -> int:
    """
    Finds the first occurrence of a needle string within a haystack string.

    Args:
        haystack: The string to search within.
        needle: The substring to search for.

    Returns:
        The starting index of the first occurrence of needle in haystack, 
        or -1 if needle is not found.

    Examples:
        >>> solve("sadbutsad", "sad")
        0
        >>> solve("leetcode", "leeto")
        -1
    """
    n = len(haystack)
    m = len(needle)

    # If needle is empty, the problem definition usually implies index 0
    if m == 0:
        return 0

    # We only need to iterate up to the point where the remaining 
    # characters in haystack are at least as long as the needle.
    for i in range(n - m + 1):
        # Check if the substring of haystack starting at i matches needle
        # We use slicing for a clean implementation, which is O(m)
        if haystack[i : i + m] == needle:
            return i

    return -1
