METADATA = {
    "id": 1456,
    "name": "Maximum Number of Vowels in a Substring of Given Length",
    "slug": "maximum-number-of-vowels-in-a-substring-of-given-length",
    "category": "String",
    "aliases": [],
    "tags": ["sliding_window", "string"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the maximum number of vowels in any substring of a given length k.",
}

def solve(s: str, k: int) -> int:
    """
    Finds the maximum number of vowels in any substring of length k using a sliding window.

    Args:
        s: The input string.
        k: The length of the substring.

    Returns:
        The maximum number of vowels found in any substring of length k.

    Examples:
        >>> solve("abciiidef", 3)
        3
        >>> solve("aeiou", 2)
        2
        >>> solve("leetcode", 3)
        2
    """
    vowels = {'a', 'e', 'i', 'o', 'u'}
    current_vowel_count = 0
    max_vowel_count = 0

    # Initialize the first window of size k
    for i in range(k):
        if s[i] in vowels:
            current_vowel_count += 1
    
    max_vowel_count = current_vowel_count

    # Slide the window from index k to the end of the string
    for i in range(k, len(s)):
        # Add the new character entering the window
        if s[i] in vowels:
            current_vowel_count += 1
        
        # Remove the character leaving the window
        if s[i - k] in vowels:
            current_vowel_count -= 1
        
        # Update the maximum count found so far
        if current_vowel_count > max_vowel_count:
            max_vowel_count = current_vowel_count
            
        # Optimization: if we found a window where all characters are vowels, return k
        if max_vowel_count == k:
            return k

    return max_vowel_count
