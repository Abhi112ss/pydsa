METADATA = {
    "id": 2781,
    "name": "Length of the Longest Valid Substring",
    "slug": "length-of-the-longest-valid-substring",
    "category": "String",
    "aliases": [],
    "tags": ["string", "sliding_window", "two_pointers"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the length of the longest substring that contains only vowels or only consonants.",
}

def solve(s: str) -> int:
    """
    Calculates the length of the longest substring consisting entirely of 
    either vowels or consonants.

    Args:
        s: The input string consisting of lowercase English letters.

    Returns:
        The length of the longest valid substring.

    Examples:
        >>> solve("aeiou")
        5
        >>> solve("abcde")
        2
        >>> solve("aeb")
        1
    """
    if not s:
        return 0

    vowels_set = {'a', 'e', 'i', 'o', 'u'}
    max_length = 0
    current_length = 0
    
    # Track the type of the current sequence: 
    # True for vowels, False for consonants, None for start
    is_prev_vowel = None

    for char in s:
        is_current_vowel = char in vowels_set
        
        # If we are starting a new sequence or continuing the current type
        if is_prev_vowel is None or is_current_vowel == is_prev_vowel:
            current_length += 1
            is_prev_vowel = is_current_vowel
        else:
            # Type changed: update max and reset length to 1 (the current char)
            max_length = max(max_length, current_length)
            current_length = 1
            is_prev_vowel = is_current_vowel
            
    # Final check to catch the last sequence in the loop
    return max(max_length, current_length)
