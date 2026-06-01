METADATA = {
    "id": 3262,
    "name": "Find Overlapping Shifts",
    "slug": "find_overlapping_shifts",
    "category": "String",
    "aliases": [],
    "tags": ["string_matching", "kmp_algorithm", "z_algorithm"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Find the number of shifts where a pattern overlaps with a text using efficient string matching.",
}

def solve(text: str, pattern: str) -> int:
    """
    Finds the number of shifts where the pattern overlaps with the text.
    
    This implementation uses the Z-algorithm to find all occurrences of the 
    pattern within the text in linear time.

    Args:
        text: The main string to search within.
        pattern: The pattern string to search for.

    Returns:
        The count of occurrences of the pattern in the text.

    Examples:
        >>> solve("ababa", "aba")
        2
        >>> solve("aaaaa", "aa")
        4
    """
    if not pattern:
        return 0
    
    # Create a combined string: pattern + separator + text
    # The separator ensures the Z-values don't cross the boundary
    combined = pattern + "$" + text
    n = len(combined)
    z_array = [0] * n
    
    # Z-algorithm implementation to find longest common prefix 
    # between combined[i:] and combined[0:]
    left, right = 0, 0
    for i in range(1, n):
        if i <= right:
            z_array[i] = min(right - i + 1, z_array[i - left])
        
        # Attempt to extend the match manually
        while i + z_array[i] < n and combined[z_array[i]] == combined[i + z_array[i]]:
            z_array[i] += 1
            
        # Update the [left, right] window
        if i + z_array[i] - 1 > right:
            left, right = i, i + z_array[i] - 1
            
    # Count how many times the Z-value equals the pattern length
    # We only look at indices corresponding to the 'text' part of the combined string
    pattern_len = len(pattern)
    match_count = 0
    
    # The text starts after pattern + "$"
    # Index in combined = pattern_len + 1 + index_in_text
    for i in range(pattern_len + 1, n):
        if z_array[i] == pattern_len:
            match_count += 1
            
    return match_count
