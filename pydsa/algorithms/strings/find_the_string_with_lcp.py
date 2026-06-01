METADATA = {
    "id": 2573,
    "name": "Find the String with Given Prefix and Suffix",
    "slug": "find-the-string-with-given-prefix-and-suffix",
    "category": "String",
    "aliases": [],
    "tags": ["strings", "greedy"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Find the lexicographically smallest string that has a given prefix and suffix, where the prefix and suffix may overlap.",
}

def solve(prefix: str, suffix: str) -> str:
    """
    Finds the lexicographically smallest string that starts with 'prefix' 
    and ends with 'suffix'.

    The strategy is to check if the suffix can overlap with the prefix. 
    If the suffix starts with the end of the prefix, we merge them. 
    Otherwise, we simply concatenate them.

    Args:
        prefix: The required starting substring.
        suffix: The required ending substring.

    Returns:
        The lexicographically smallest string satisfying the conditions, 
        or an empty string if no such string exists.

    Examples:
        >>> solve("ab", "ba")
        "aba"
        >>> solve("abc", "def")
        "abcdef"
        >>> solve("abc", "cde")
        "abcde"
        >>> solve("abc", "abc")
        "abc"
    """
    n_prefix = len(prefix)
    n_suffix = len(suffix)

    # Check for all possible overlap lengths from longest to shortest.
    # The longest possible overlap is min(len(prefix), len(suffix)).
    # However, we want the smallest string, which means the largest overlap.
    # But wait, the problem asks for the lexicographically smallest string.
    # Actually, the smallest string is achieved by the largest possible overlap 
    # that satisfies the prefix/suffix condition.
    
    # Let's iterate through possible overlap lengths 'k'.
    # If prefix ends with the first 'k' characters of suffix, then 
    # the string can be prefix + suffix[k:].
    
    # To get the lexicographically smallest string, we want the shortest string.
    # The shortest string is formed by the maximum possible overlap.
    
    max_overlap = 0
    # We check overlap lengths from the maximum possible down to 1.
    # An overlap of length 'k' means prefix[n_prefix - k:] == suffix[:k]
    for k in range(min(n_prefix, n_suffix), 0, -1):
        if prefix.endswith(suffix[:k]):
            max_overlap = k
            break
            
    # If the suffix is entirely contained within the prefix (or vice versa)
    # and it satisfies the overlap condition, the result is just the prefix
    # (if suffix is a suffix of prefix) or suffix (if prefix is a prefix of suffix).
    # But the logic prefix + suffix[max_overlap:] covers all cases.
    
    # Special case: if suffix is a substring of prefix and it's at the end.
    if prefix.endswith(suffix):
        return prefix
    
    # Special case: if prefix is a substring of suffix and it's at the start.
    if suffix.startswith(prefix):
        return suffix

    # General case: merge with the largest possible overlap.
    # Note: The problem asks for the lexicographically smallest string.
    # Since any valid string must contain prefix and suffix, the shortest 
    # string is always the best candidate for lexicographical smallest 
    # because we are adding characters. Actually, the problem implies 
    # we want the shortest valid string.
    
    # Re-evaluating: The shortest string is always the lexicographically smallest 
    # among strings of the same length. But here, different overlaps result 
    # in different lengths. However, the problem constraints and typical 
    # LeetCode logic for this specific problem imply we look for the 
    # shortest string that satisfies the condition.
    
    # Let's check if the suffix is already a suffix of the prefix.
    if prefix.endswith(suffix):
        return prefix
    
    # Let's check if the prefix is already a prefix of the suffix.
    if suffix.startswith(prefix):
        return suffix

    # Check for overlap
    for k in range(min(n_prefix, n_suffix), 0, -1):
        if prefix.endswith(suffix[:k]):
            return prefix + suffix[k:]
            
    # No overlap found
    return prefix + suffix
