METADATA = {
    "id": 1163,
    "name": "Last Substring in Lexicographical Order",
    "slug": "last-substring-in-lexicographical-order",
    "category": "String",
    "aliases": [],
    "tags": ["two_pointer", "greedy"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the lexicographically largest substring of a given string using a two-pointer approach.",
}

def solve(s: str) -> str:
    """
    Finds the lexicographically largest substring of the given string.

    The algorithm uses a two-pointer approach to compare suffixes. Instead of 
    generating all substrings, we compare potential starting positions and 
    skip indices that cannot possibly yield a larger substring.

    Args:
        s: The input string.

    Returns:
        The lexicographically largest substring.

    Examples:
        >>> solve("abab")
        'b'
        >>> solve("leetcode")
        'tcode'
    """
    n = len(s)
    # i is the starting index of the current best candidate
    # j is the starting index of the next candidate to compare
    i = 0
    j = 1
    # k is the offset used to compare characters at s[i+k] and s[j+k]
    k = 0

    while j + k < n:
        if s[i + k] == s[j + k]:
            # Characters match, increment offset to check next character
            k += 1
            continue
        elif s[i + k] < s[j + k]:
            # The substring starting at j is lexicographically larger.
            # Move i to j, and reset j to be the next position after the new i.
            # We skip all indices between the old i and the new i because 
            # they cannot be the start of the largest substring.
            i = max(i + k + 1, j)
            j = i + 1
        else:
            # The substring starting at i is still larger.
            # Move j past the current mismatch point.
            j = j + k + 1
        
        # Reset offset for the next comparison
        k = 0

    return s[i:]
