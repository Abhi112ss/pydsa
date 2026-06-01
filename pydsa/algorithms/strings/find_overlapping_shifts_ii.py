METADATA = {
    "id": 3268,
    "name": "Find Overlapping Shifts II",
    "slug": "find_overlapping_shifts_ii",
    "category": "String",
    "aliases": [],
    "tags": ["string_matching", "rolling_hash", "kmp"],
    "difficulty": "hard",
    "time_complexity": "O(n + m)",
    "space_complexity": "O(n + m)",
    "description": "Find all starting positions where a pattern matches a text, allowing for overlapping occurrences.",
}

def solve(text: str, pattern: str) -> list[int]:
    """
    Finds all starting indices of pattern occurrences in text using the KMP algorithm.

    Args:
        text: The main string to search within.
        pattern: The substring to search for.

    Returns:
        A list of integers representing the starting indices of all occurrences.

    Examples:
        >>> solve("ababa", "aba")
        [0, 2]
        >>> solve("aaaaa", "aa")
        [0, 1, 2, 3]
    """
    if not pattern:
        return []
    
    n = len(text)
    m = len(pattern)
    
    if m > n:
        return []

    # Step 1: Precompute the Longest Prefix Suffix (LPS) array for the pattern
    # lps[i] is the length of the longest proper prefix of pattern[0...i] 
    # that is also a suffix of pattern[0...i].
    lps = [0] * m
    prefix_len = 0
    i = 1
    while i < m:
        if pattern[i] == pattern[prefix_len]:
            prefix_len += 1
            lps[i] = prefix_len
            i += 1
        else:
            if prefix_len != 0:
                prefix_len = lps[prefix_len - 1]
            else:
                lps[i] = 0
                i += 1

    # Step 2: Perform the KMP search
    results = []
    text_idx = 0
    pattern_idx = 0
    
    while text_idx < n:
        if text[text_idx] == pattern[pattern_idx]:
            text_idx += 1
            pattern_idx += 1
        
        if pattern_idx == m:
            # Match found: record the starting index
            results.append(text_idx - pattern_idx)
            # To find overlapping matches, we reset pattern_idx using LPS
            pattern_idx = lps[pattern_idx - 1]
        
        elif text_idx < n and text[text_idx] != pattern[pattern_idx]:
            # Mismatch after pattern_idx matches
            if pattern_idx != 0:
                pattern_idx = lps[pattern_idx - 1]
            else:
                text_idx += 1
                
    return results
