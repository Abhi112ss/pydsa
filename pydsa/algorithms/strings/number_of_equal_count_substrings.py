METADATA = {
    "id": 2067,
    "name": "Number of Equal Count Substrings",
    "slug": "number-of-equal-count-substrings",
    "category": "String",
    "aliases": [],
    "tags": ["hash_map", "strings", "sliding_window"],
    "difficulty": "medium",
    "time_complexity": "O(n^2)",
    "space_complexity": "O(1)",
    "description": "Count the number of substrings where all characters that appear in the substring appear an equal number of times.",
}

def solve(s: str) -> int:
    """
    Counts the number of substrings where all present characters have the same frequency.

    Args:
        s: The input string consisting of lowercase English letters.

    Returns:
        The total count of substrings satisfying the condition.

    Examples:
        >>> solve("abacaba")
        10
        >>> solve("abc")
        4
    """
    n = len(s)
    total_equal_count_substrings = 0

    # Iterate through every possible starting position of a substring
    for start_index in range(n):
        # Frequency map for characters in the current substring
        # Since we only have lowercase English letters, a fixed-size array is O(1) space
        char_counts = [0] * 26
        distinct_chars_count = 0
        
        # Expand the substring from the start_index to the end of the string
        for end_index in range(start_index, n):
            char_idx = ord(s[end_index]) - ord('a')
            
            # If this is a new character in the current substring, increment distinct count
            if char_counts[char_idx] == 0:
                distinct_chars_count += 1
            
            char_counts[char_idx] += 1
            
            # To check if all non-zero counts are equal, we find the frequency 
            # of the first character we encountered and compare others to it.
            # However, a more robust way is to check if all non-zero counts 
            # match the frequency of the first non-zero character found.
            
            # Optimization: Instead of iterating 26 every time, we can track 
            # if all current non-zero counts are equal.
            # We pick the frequency of the character we just added.
            target_frequency = char_counts[char_idx]
            
            # Check if all characters that have appeared so far have the same frequency
            is_equal = True
            # We only need to check the 'distinct_chars_count' characters
            # But since the alphabet is small (26), iterating 26 is O(1)
            for count in char_counts:
                if count > 0 and count != target_frequency:
                    is_equal = False
                    break
            
            if is_equal:
                total_equal_count_substrings += 1
                
    return total_equal_count_substrings
