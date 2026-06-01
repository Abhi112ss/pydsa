METADATA = {
    "id": 3407,
    "name": "Substring Matching Pattern",
    "slug": "substring-matching-pattern",
    "category": "String",
    "aliases": [],
    "tags": ["kmp", "string_matching", "rolling_hash"],
    "difficulty": "easy",
    "time_complexity": "O(n + m)",
    "space_complexity": "O(m)",
    "description": "Determine if a pattern string is a substring of a given text string.",
}

def solve(text: str, pattern: str) -> bool:
    """
    Determines if the pattern string is a substring of the text string 
    using the Knuth-Morris-Pratt (KMP) algorithm.

    Args:
        text: The main string to search within.
        pattern: The string to search for.

    Returns:
        True if pattern is a substring of text, False otherwise.

    Examples:
        >>> solve("leetcode", "code")
        True
        >>> solve("hello", "ll")
        True
        >>> solve("abc", "d")
        False
    """
    if not pattern:
        return True
    if not text:
        return False

    # Step 1: Precompute the Longest Prefix Suffix (LPS) array for the pattern
    # lps[i] stores the length of the longest proper prefix of pattern[0...i] 
    # that is also a suffix of pattern[0...i].
    pattern_length = len(pattern)
    text_length = len(text)
    lps = [0] * pattern_length
    
    prefix_index = 0
    for i in range(1, pattern_length):
        while prefix_index > 0 and pattern[i] != pattern[prefix_index]:
            prefix_index = lps[prefix_index - 1]
        
        if pattern[i] == pattern[prefix_index]:
            prefix_index += 1
            lps[i] = prefix_index
        else:
            lps[i] = 0

    # Step 2: Perform the KMP search
    pattern_ptr = 0
    for text_ptr in range(text_length):
        # If characters don't match, use the LPS array to skip unnecessary comparisons
        while pattern_ptr > 0 and text[text_ptr] != pattern[pattern_ptr]:
            pattern_ptr = lps[pattern_ptr - 1]
        
        if text[text_ptr] == pattern[pattern_ptr]:
            pattern_ptr += 1
        
        # If the pattern pointer reaches the end of the pattern, we found a match
        if pattern_ptr == pattern_length:
            return True

    return False
