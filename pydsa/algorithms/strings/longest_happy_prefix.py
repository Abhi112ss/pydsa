METADATA = {
    "id": 1392,
    "name": "Longest Happy Prefix",
    "slug": "longest-happy-prefix",
    "category": "String",
    "aliases": [],
    "tags": ["string", "kmp", "rolling_hash"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Find the longest proper prefix of a string that is also a suffix of the same string.",
}

def solve(s: str) -> str:
    """
    Finds the longest happy prefix using the KMP preprocessing algorithm (LPS array).

    A happy prefix is a proper prefix of a string that is also a suffix of the same string.
    The KMP algorithm's Longest Prefix Suffix (LPS) array construction is the optimal
    way to solve this in linear time.

    Args:
        s: The input string.

    Returns:
        The longest proper prefix that is also a suffix.

    Examples:
        >>> solve("level")
        "l"
        >>> solve("ababab")
        "abab"
        >>> solve("leetcode")
        ""
    """
    n = len(s)
    if n <= 1:
        return ""

    # lps[i] will store the length of the longest proper prefix of s[0...i]
    # that is also a suffix of s[0...i].
    lps = [0] * n
    
    # length of the previous longest prefix suffix
    length = 0
    i = 1

    # Build the LPS array using the KMP preprocessing logic
    while i < n:
        if s[i] == s[length]:
            # If characters match, increment length and move to next index
            length += 1
            lps[i] = length
            i += 1
        else:
            # If characters do not match
            if length != 0:
                # Try the previous longest prefix suffix to avoid redundant checks
                length = lps[length - 1]
            else:
                # No prefix suffix found for this position
                lps[i] = 0
                i += 1

    # The last value in the LPS array gives the length of the longest 
    # proper prefix that is also a suffix for the entire string.
    longest_length = lps[-1]
    return s[:longest_length]
