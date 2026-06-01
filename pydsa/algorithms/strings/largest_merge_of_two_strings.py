METADATA = {
    "id": 1754,
    "name": "Largest Merge Of Two Strings",
    "slug": "largest-merge-of-two-strings",
    "category": "String",
    "aliases": [],
    "tags": ["string", "greedy"],
    "difficulty": "medium",
    "time_complexity": "O((N+M)^2)",
    "space_complexity": "O(N+M)",
    "description": "Construct the largest possible merge of two strings by greedily picking the character from the string that has the lexicographically larger suffix.",
}

def solve(a: str, b: str) -> str:
    """
    Constructs the largest merge of two strings using a greedy approach.

    At each step, we compare the remaining suffixes of both strings. We pick 
    the first character from the string that is lexicographically larger. 
    This ensures that we preserve larger characters for earlier positions 
    in the resulting string.

    Args:
        a: The first input string.
        b: The second input string.

    Returns:
        The lexicographically largest merged string.

    Examples:
        >>> solve("cabaa", "bcaaa")
        'cbcabaaaaa'
        >>> solve("a", "d")
        'da'
    """
    result_chars: list[str] = []
    # Convert to list for efficient popping if needed, 
    # but slicing strings is idiomatic in Python for suffix comparison.
    # We use pointers or slicing to track progress.
    
    idx_a, idx_b = 0, 0
    len_a, len_b = len(a), len(b)

    while idx_a < len_a and idx_b < len_b:
        # Compare the remaining suffixes of both strings.
        # Python's string comparison is O(K) where K is the length of the suffix.
        if a[idx_a:] > b[idx_b:]:
            result_chars.append(a[idx_a])
            idx_a += 1
        else:
            result_chars.append(b[idx_b])
            idx_b += 1

    # Append any remaining characters from either string.
    if idx_a < len_a:
        result_chars.append(a[idx_a:])
    if idx_b < len_b:
        result_chars.append(b[idx_b:])

    return "".join(result_chars)
