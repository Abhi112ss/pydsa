METADATA = {
    "id": 1781,
    "name": "Sum of Beauty of All Substrings",
    "slug": "sum-of-beauty-of-all-substrings",
    "category": "String",
    "aliases": [],
    "tags": ["hash_map", "sliding_window", "string_manipulation"],
    "difficulty": "medium",
    "time_complexity": "O(n^2)",
    "space_complexity": "O(1)",
    "description": "Calculate the sum of the beauty of all substrings, where beauty is the difference between the maximum and minimum frequencies of characters.",
}

def solve(s: str) -> int:
    """
    Calculates the sum of beauty of all substrings of the given string.
    
    Beauty is defined as the difference between the maximum frequency 
    and the minimum frequency of any character present in the substring.
    Only characters with frequency > 0 are considered for the minimum.

    Args:
        s: The input string consisting of lowercase English letters.

    Returns:
        The total sum of beauty values for all possible substrings.

    Examples:
        >>> solve("aabcb")
        5
        >>> solve("aabc")
        0
    """
    total_beauty = 0
    n = len(s)

    # Iterate through every possible starting position of a substring
    for start_index in range(n):
        # Frequency array for lowercase English letters (a-z)
        # Using a fixed size array ensures O(1) space complexity
        char_frequencies = [0] * 26
        
        # Expand the substring from the start_index to the end of the string
        for end_index in range(start_index, n):
            # Update frequency of the current character
            char_code = ord(s[end_index]) - ord('a')
            char_frequencies[char_code] += 1
            
            # Calculate max and min frequencies among characters present in the substring
            max_freq = 0
            min_freq = float('inf')
            
            for freq in char_frequencies:
                if freq > 0:
                    if freq > max_freq:
                        max_freq = freq
                    if freq < min_freq:
                        min_freq = freq
            
            # If min_freq was never updated (shouldn't happen for non-empty), beauty is 0
            if min_freq != float('inf'):
                total_beauty += (max_freq - min_freq)
                
    return total_beauty
