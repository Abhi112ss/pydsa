METADATA = {
    "id": 467,
    "name": "Unique Substrings in Wraparound String",
    "slug": "unique-substrings-in-wraparound-string",
    "category": "String",
    "aliases": [],
    "tags": ["dynamic_programming", "string", "hash_table"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Count the number of unique substrings that wrap around the alphabet.",
}

def solve(s: str) -> int:
    """
    Counts the number of unique substrings in a wraparound string.
    
    A substring is valid if every character is the next character in the 
    alphabet (with 'z' wrapping to 'a').

    Args:
        s: The input string consisting of lowercase English letters.

    Returns:
        The total number of unique valid substrings.

    Examples:
        >>> solve("abc")
        6
        >>> solve("zb")
        2
        >>> solve("aaa")
        1
    """
    # max_len_ending_at[i] stores the length of the longest valid 
    # substring ending with the character represented by index i (0-25).
    # This allows us to count only new unique substrings.
    max_len_ending_at = [0] * 26
    
    # To handle the wraparound logic easily, we map 'a'-'z' to 0-25.
    def char_to_idx(c: str) -> int:
        return ord(c) - ord('a')

    for i in range(len(s)):
        current_char_idx = char_to_idx(s[i])
        
        # If it's the first character or it follows the previous character 
        # in a wraparound sequence (e.g., 'a' follows 'z' or 'b' follows 'a').
        if i > 0 and char_to_idx(s[i-1]) == (current_char_idx - 1) % 26:
            # Increment the length of the current valid sequence.
            # We use the previous character's max length + 1.
            prev_char_idx = char_to_idx(s[i-1])
            max_len_ending_at[current_char_idx] = max_len_ending_at[prev_char_idx] + 1
        else:
            # Start a new sequence of length 1.
            max_len_ending_at[current_char_idx] = 1
            
        # Note: We don't use max() here because if we encounter the same 
        # character again in a shorter sequence, it doesn't contribute 
        # new unique substrings. However, the problem logic requires 
        # tracking the longest sequence ending at this char to ensure 
        # we count all unique substrings.
        # Actually, the logic is: if we find a sequence of length L ending at char C,
        # it contributes L - (previous max length for C) new substrings.
        # But wait, the standard DP approach for this is:
        # max_len_ending_at[char] = max(max_len_ending_at[char], current_run_length)
        # Let's refine the logic to strictly follow the "new substrings" rule.

    # Re-implementing the core logic to correctly handle the "unique" constraint.
    # We need to track the current continuous run length.
    max_len_ending_at = [0] * 26
    current_run_length = 0
    
    for i in range(len(s)):
        curr = char_to_idx(s[i])
        
        if i > 0 and char_to_idx(s[i-1]) == (curr - 1) % 26:
            current_run_length += 1
        else:
            current_run_length = 1
            
        # If the current run length is greater than what we've seen 
        # ending at this specific character, the difference represents 
        # the number of new unique substrings we've discovered.
        if current_run_length > max_len_ending_at[curr]:
            # We don't actually add to a total here, we just update the max.
            # The total count is the sum of all increments.
            # Let's use a running total.
            pass 

    # Corrected implementation:
    max_len_ending_at = [0] * 26
    total_unique_substrings = 0
    current_run_length = 0
    
    for i in range(len(s)):
        curr = char_to_idx(s[i])
        
        if i > 0 and char_to_idx(s[i-1]) == (curr - 1) % 26:
            current_run_length += 1
        else:
            current_run_length = 1
            
        # If this run is longer than any previous run ending with 'curr',
        # the new substrings are those with lengths: 
        # (max_len_ending_at[curr] + 1) up to current_run_length.
        if current_run_length > max_len_ending_at[curr]:
            total_unique_substrings += (current_run_length - max_len_ending_at[curr])
            max_len_ending_at[curr] = current_run_length
            
    return total_unique_substrings
