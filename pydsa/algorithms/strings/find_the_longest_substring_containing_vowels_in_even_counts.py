METADATA = {
    "id": 1371,
    "name": "Find the Longest Substring Containing Vowels in Even Counts",
    "slug": "find-the-longest-substring-containing-vowels-in-even-counts",
    "category": "Hash Table",
    "aliases": [],
    "tags": ["bit_manipulation", "hash_map", "prefix_sum"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the length of the longest substring that contains an even count of each vowel (a, e, i, o, u).",
}

def solve(s: str) -> int:
    """
    Finds the length of the longest substring containing an even count of each vowel.

    Args:
        s: The input string consisting of lowercase English letters.

    Returns:
        The length of the longest substring where each vowel appears an even number of times.

    Examples:
        >>> solve("eleetminicoworoep")
        ieetminicoworoep = 13
        >>> solve("aeiou")
        0
    """
    # Map each vowel to a specific bit position in a 5-bit integer
    vowel_to_bit = {
        'a': 0,
        'e': 1,
        'i': 2,
        'o': 3,
        'u': 4
    }
    
    # mask_first_occurrence stores the first index where a specific parity mask was seen.
    # The mask represents the parity (even/odd) of the counts of 'a', 'e', 'i', 'o', 'u'.
    # Initial state: mask 0 (all even) is seen at index -1.
    mask_first_occurrence = {0: -1}
    
    current_mask = 0
    max_length = 0
    
    for index, char in enumerate(s):
        # If the character is a vowel, flip its corresponding bit in the mask
        if char in vowel_to_bit:
            bit_position = vowel_to_bit[char]
            current_mask ^= (1 << bit_position)
        
        # If this exact parity mask has been seen before, the substring between 
        # the previous occurrence and the current index has all even vowel counts.
        if current_mask in mask_first_occurrence:
            previous_index = mask_first_occurrence[current_mask]
            substring_length = index - previous_index
            if substring_length > max_length:
                max_length = substring_length
        else:
            # Otherwise, record the first time we encounter this specific parity configuration
            mask_first_occurrence[current_mask] = index
            
    return max_length
