METADATA = {
    "id": 2062,
    "name": "Count Vowel Substrings of a String",
    "slug": "count-vowel-substrings-of-a-string",
    "category": "Hash Table",
    "aliases": [],
    "tags": ["sliding_window", "hash_map", "string"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Count the number of substrings that consist only of vowels and contain all five vowels at least once.",
}

def solve(word: str) -> int:
    """
    Counts the number of substrings that consist only of vowels and contain 
    all five vowels ('a', 'e', 'i', 'o', 'u') at least once.

    Args:
        word: The input string consisting of lowercase English letters.

    Returns:
        The total count of valid vowel substrings.

    Examples:
        >>> solve("aeiouu")
        2
        >>> solve("unicornariel")
        0
        >>> solve("cuaieuouac")
        7
    """
    vowels = {'a', 'e', 'i', 'o', 'u'}
    
    def count_at_most(k: int) -> int:
        """
        Helper function using a sliding window to count substrings 
        containing at most 'k' distinct vowels, where all characters 
        in the substring must be vowels.
        
        Note: To solve the 'exactly 5' problem, we use the principle:
        Exactly(5) = AtMost(5) - AtMost(4) is not directly applicable here 
        because of the 'only vowels' constraint. Instead, we use a 
        sliding window approach to find substrings containing exactly 5 
        distinct vowels within segments of pure vowels.
        """
        # This specific problem is better solved by splitting the string 
        # into blocks of pure vowels and then applying the 'at most' logic.
        pass

    # Alternative approach: 
    # 1. Split the string into segments containing only vowels.
    # 2. For each segment, count substrings containing exactly 5 distinct vowels.
    # To count substrings with exactly 5 distinct vowels in a pure-vowel segment:
    # count(exactly 5) = count(at most 5) - count(at most 4)
    
    def count_at_most_distinct(vowel_segment: str, target_distinct: int) -> int:
        """Counts substrings in a pure-vowel segment with <= target_distinct vowels."""
        count = 0
        left = 0
        freq_map = {}
        
        for right in range(len(vowel_segment)):
            char = vowel_segment[right]
            freq_map[char] = freq_map.get(char, 0) + 1
            
            # Shrink window if we exceed the allowed number of distinct vowels
            while len(freq_map) > target_distinct:
                left_char = vowel_segment[left]
                freq_map[left_char] -= 1
                if freq_map[left_char] == 0:
                    del freq_map[left_char]
                left += 1
            
            # All substrings ending at 'right' and starting from 'left' to 'right'
            # are valid under the 'at most' constraint.
            count += (right - left + 1)
        return count

    total_count = 0
    current_segment = []
    
    # Iterate through the word to isolate segments of pure vowels
    for char in word:
        if char in vowels:
            current_segment.append(char)
        else:
            if current_segment:
                segment_str = "".join(current_segment)
                # Exactly 5 = (At most 5) - (At most 4)
                # Since the segment only contains vowels, 'at most 5' is just 
                # the total number of substrings in the segment.
                total_count += count_at_most_distinct(segment_str, 5) - \
                               count_at_most_distinct(segment_str, 4)
                current_segment = []
                
    # Handle the last segment if the word ends with a vowel
    if current_segment:
        segment_str = "".join(current_segment)
        total_count += count_at_most_distinct(segment_str, 5) - \
                       count_at_most_distinct(segment_str, 4)
                       
    return total_count
