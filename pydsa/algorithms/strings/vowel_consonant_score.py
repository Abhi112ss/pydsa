METADATA = {
    "id": 3813,
    "name": "Vowel-Consonant Score",
    "slug": "vowel_consonant_score",
    "category": "Strings",
    "aliases": [],
    "tags": ["strings", "sliding_window"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Calculate the maximum score difference between vowels and consonants in a substring of a given length.",
}

def solve(s: str, k: int) -> int:
    """
    Calculates the maximum score difference (vowels - consonants) for any substring of length k.

    Args:
        s: The input string consisting of lowercase English letters.
        k: The fixed length of the substring to evaluate.

    Returns:
        The maximum score (vowels - consonants) found among all substrings of length k.

    Examples:
        >>> solve("aeiou", 3)
        3
        >>> solve("abcde", 2)
        0
        >>> solve("leetcode", 4)
        0
    """
    vowels_set = {'a', 'e', 'i', 'o', 'u'}
    
    # current_score tracks (count of vowels - count of consonants) in the current window
    current_score = 0
    
    # Initialize the first window of size k
    for i in range(k):
        if s[i] in vowels_set:
            current_score += 1
        else:
            current_score -= 1
            
    max_score = current_score
    
    # Slide the window across the string
    for i in range(k, len(s)):
        # Remove the character that is sliding out of the window (left side)
        outgoing_char = s[i - k]
        if outgoing_char in vowels_set:
            current_score -= 1
        else:
            current_score += 1
            
        # Add the character that is sliding into the window (right side)
        incoming_char = s[i]
        if incoming_char in vowels_set:
            current_score += 1
        else:
            current_score -= 1
            
        # Update the maximum score found so far
        if current_score > max_score:
            max_score = current_score
            
    return max_score
