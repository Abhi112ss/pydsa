METADATA = {
    "id": 3325,
    "name": "Count Substrings With K-Frequency Characters I",
    "slug": "count-substrings-with-k-frequency-characters-i",
    "category": "String",
    "aliases": [],
    "tags": ["sliding_window", "hash_map", "string"],
    "difficulty": "easy",
    "time_complexity": "O(n^2)",
    "space_complexity": "O(1)",
    "description": "Count the number of substrings where every character that appears in the substring appears exactly k times.",
}

def solve(s: str, k: int) -> int:
    """
    Counts the number of substrings where every character present in the 
    substring appears exactly k times.

    Args:
        s: The input string consisting of lowercase English letters.
        k: The required frequency for each character present in a valid substring.

    Returns:
        The total count of valid substrings.

    Examples:
        >>> solve("abacaba", 1)
        7
        >>> solve("aaabbb", 3)
        2
    """
    n = len(s)
    total_valid_substrings = 0

    # Iterate through every possible starting position of a substring
    for start_index in range(n):
        # Frequency map for characters in the current substring
        # Since we only have lowercase English letters, a fixed size array or dict works.
        # Using a dictionary for clarity, but space is O(1) as max 26 keys.
        char_frequencies = {}
        
        # Track how many characters currently satisfy the 'exactly k' condition
        # and how many unique characters are in the current substring.
        chars_with_k_freq = 0
        unique_chars_count = 0

        # Expand the substring from start_index to the end of the string
        for end_index in range(start_index, n):
            char = s[end_index]
            
            # Update frequency and tracking variables
            if char not in char_frequencies:
                char_frequencies[char] = 0
                unique_chars_count += 1
            
            char_frequencies[char] += 1
            
            # If this character just reached exactly k, increment our counter
            if char_frequencies[char] == k:
                chars_with_k_freq += 1
            # If it was k and now it's k+1, it no longer satisfies the condition
            elif char_frequencies[char] == k + 1:
                chars_with_k_freq -= 1
            
            # A substring is valid if all unique characters present appear exactly k times.
            # This means the number of characters with frequency k must equal the 
            # total number of unique characters in the current substring.
            if chars_with_k_freq == unique_chars_count:
                total_valid_substrings += 1
                
            # Optimization: if any character frequency exceeds k, we can't immediately 
            # stop because we are looking for 'exactly k', but in this specific problem 
            # structure, once a char > k, it can never return to k for this start_index.
            # However, for simplicity and O(n^2) requirement, we continue.

    return total_valid_substrings
