METADATA = {
    "id": 161,
    "name": "One Edit Distance",
    "slug": "one_edit_distance",
    "category": "String",
    "aliases": [],
    "tags": ["string_manipulation", "two_pointer"],
    "difficulty": "medium",
    "time_complexity": "O(N)",
    "space_complexity": "O(1)",
    "description": "Determine if two strings are exactly one edit distance apart.",
}

def solve(s: str, t: str) -> bool:
    """
    Determines if two strings are exactly one edit distance apart.
    An edit can be an insertion, a deletion, or a replacement of a character.

    Args:
        s: The first input string.
        t: The second input string.

    Returns:
        True if the strings are exactly one edit distance apart, False otherwise.

    Examples:
        >>> solve("ab", "acb")
        True
        >>> solve("cab", "ad")
        False
        >>> solve("", "")
        False
        >>> solve("a", "")
        True
    """
    n, m = len(s), len(t)

    # If the length difference is more than 1, they cannot be one edit apart
    if abs(n - m) > 1:
        return False

    # Ensure s is the shorter string to simplify logic
    if n > m:
        return solve(t, s)

    for i in range(n):
        # Find the first character mismatch
        if s[i] != t[i]:
            if n == m:
                # Case 1: Replacement
                # The rest of the strings must be identical after this character
                return s[i + 1:] == t[i + 1:]
            else:
                # Case 2: Insertion (into s) or Deletion (from t)
                # Since s is shorter, we skip the current char in t and compare the rest
                return s[i:] == t[i + 1:]

    # If no mismatch was found in the loop, the only way they are one edit apart
    # is if the longer string has exactly one extra character at the end.
    return n + 1 == m
