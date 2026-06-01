METADATA = {
    "id": 424,
    "name": "Longest Repeating Character Replacement",
    "slug": "longest-repeating-character-replacement",
    "category": "Sliding Window",
    "aliases": [],
    "tags": ["sliding_window", "hash_map", "string"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the length of the longest substring containing the same letter after performing at most k replacements.",
}

def solve(s: str, k: int) -> int:
    """
    Finds the length of the longest substring containing the same letter 
    after performing at most k replacements.

    Args:
        s: The input string consisting of uppercase English letters.
        k: The maximum number of characters that can be replaced.

    Returns:
        The length of the longest valid substring.

    Examples:
        >>> solve("ABAB", 2)
        4
        >>> solve("AABABBA", 1)
        4
    """
    # Frequency map for characters in the current window
    # Since input is uppercase English letters, size is at most 26
    char_counts: dict[str, int] = {}
    
    max_length = 0
    max_freq = 0
    window_start = 0
    
    for window_end in range(len(s)):
        current_char = s[window_end]
        char_counts[current_char] = char_counts.get(current_char, 0) + 1
        
        # Track the frequency of the most frequent character in the current window.
        # This helps us determine how many characters need to be replaced.
        max_freq = max(max_freq, char_counts[current_char])
        
        # The number of characters to replace is (window_size - max_freq).
        # If this exceeds k, the window is invalid, so we shrink it from the left.
        window_size = window_end - window_start + 1
        if (window_size - max_freq) > k:
            left_char = s[window_start]
            char_counts[left_char] -= 1
            window_start += 1
            # Note: We don't strictly need to update max_freq here because 
            # max_length only increases when we find a new max_freq.
            
        # Update the global maximum length found so far
        max_length = max(max_length, window_end - window_start + 1)
        
    return max_length
