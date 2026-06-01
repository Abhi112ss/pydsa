METADATA = {
    "id": 214,
    "name": "Shortest Palindrome",
    "slug": "shortest_palindrome",
    "category": "String",
    "aliases": ["shortest_palindrome"],
    "tags": ["string_matching", "kmp", "rolling_hash"],
    "difficulty": "hard",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Find the shortest palindrome by adding characters in front of the given string.",
}

def solve(s: str) -> str:
    """Find the shortest palindrome by adding characters in front of the given string.

    Uses KMP's partial match table to find the longest palindromic prefix.

    Args:
        s: The input string.

    Returns:
        The shortest palindrome formed by adding characters in front of s.

    Examples:
        >>> solve("aacecaaa")
        "aaacecaaa"
        >>> solve("abcd")
        "dcbabcd"
    """
    if not s:
        return ""

    # Create a combined string: s + '#' + reverse(s)
    # The '#' is a separator that won't appear in the original string
    rev_s = s[::-1]
    combined = s + '#' + rev_s

    # Build KMP partial match table (failure function) for the combined string
    n = len(combined)
    failure = [0] * n

    # Build the failure function using KMP algorithm
    for i in range(1, n):
        j = failure[i - 1]
        while j > 0 and combined[i] != combined[j]:
            j = failure[j - 1]
        if combined[i] == combined[j]:
            j += 1
        failure[i] = j

    # The last value in failure table gives us the length of the longest
    # palindromic prefix of the original string
    longest_palindrome_prefix_len = failure[-1]

    # We need to add the reverse of the remaining suffix in front
    suffix_to_add = rev_s[:len(s) - longest_palindrome_prefix_len]

    return suffix_to_add + s