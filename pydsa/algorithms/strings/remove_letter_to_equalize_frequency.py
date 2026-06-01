METADATA = {
    "id": 2423,
    "name": "Remove Letter To Equalize Frequency",
    "slug": "remove-letter-to-equalize-frequency",
    "category": "Hash Table",
    "aliases": [],
    "tags": ["hash_map", "greedy", "string"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Determine if removing exactly one character from a string can make all remaining characters have the same frequency.",
}

def solve(s: str) -> bool:
    """
    Determines if removing exactly one character from the string results in all 
    remaining characters having the same frequency.

    Args:
        s: The input string consisting of lowercase English letters.

    Returns:
        True if the condition is met, False otherwise.

    Examples:
        >>> solve("abcc")
        True
        >>> solve("aazz")
        False
        >>> solve("zz")
        True
    """
    if not s:
        return False

    # Count frequency of each character
    char_counts = {}
    for char in s:
        char_counts[char] = char_counts.get(char, 0) + 1

    # Count frequency of the frequencies
    # e.g., if counts are {a: 2, b: 2, c: 1}, freq_counts is {2: 2, 1: 1}
    freq_counts = {}
    for count in char_counts.values():
        freq_counts[count] = freq_counts.get(count, 0) + 1

    # Case 1: All characters have the same frequency and there is only one type of character
    # e.g., "aaaaa" -> remove one 'a', still all 'a's have same frequency.
    if len(freq_counts) == 1:
        # If there's only one distinct character, we can always remove one.
        # If there are multiple characters but all have same frequency, 
        # we can only succeed if one character has a frequency of 1.
        # e.g., "aabbcc" -> freq_counts is {2: 3}. Removing one 'a' makes it {2: 2, 1: 1} (False).
        # e.g., "aabbc" -> freq_counts is {2: 2, 1: 1}. (Handled by Case 2).
        # The only way len(freq_counts) == 1 works is if the single frequency is 1 (e.g., "abc")
        # OR if there is only one distinct character (e.g., "aaaa").
        # Wait, if s="abc", freq_counts={1:3}. Removing 'a' leaves {1:2}. Still True.
        # If s="aa", freq_counts={2:1}. Removing 'a' leaves {1:1}. Still True.
        # If s="aabb", freq_counts={2:2}. Removing 'a' leaves {2:1, 1:1}. False.
        
        # Correct logic for len(freq_counts) == 1:
        # If there is only 1 distinct character (e.g., "aaaa"), removing 1 works.
        # If there are multiple characters but all have same frequency (e.g., "aabb"), 
        # removing 1 makes it unequal (e.g., "abb"), UNLESS the frequency is 1 (e.g., "abc").
        count_val = list(freq_counts.keys())[0]
        return len(char_counts) == 1 or count_val == 1

    # Case 2: There are exactly two different frequencies
    if len(freq_counts) == 2:
        f1, f2 = sorted(freq_counts.keys())
        # f1 is the smaller frequency, f2 is the larger frequency
        
        # Subcase A: The larger frequency is 1 (impossible since f1 < f2)
        # Subcase B: The smaller frequency is 1 and there is only one character with that frequency
        # e.g., "aabbc" -> counts {2, 2, 1} -> freq_counts {2: 2, 1: 1}. 
        # Removing the 'c' leaves {2: 2}, which is uniform.
        if f1 == 1 and freq_counts[f1] == 1:
            return True
        
        # Subcase C: The larger frequency is exactly 1 greater than the smaller frequency,
        # and there is only one character with that larger frequency.
        # e.g., "aaabb" -> counts {3, 2} -> freq_counts {3: 1, 2: 1}.
        # Removing one 'a' leaves {2, 2}, which is uniform.
        if f2 == f1 + 1 and freq_counts[f2] == 1:
            return True

    # If there are more than 2 frequencies, or the 2 frequencies don't meet the criteria, return False
    return False
