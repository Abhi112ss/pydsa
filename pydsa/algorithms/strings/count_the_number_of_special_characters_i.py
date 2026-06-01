METADATA = {
    "id": 3120,
    "name": "Count the Number of Special Characters I",
    "slug": "count-the-number-of-special-characters-i",
    "category": "String",
    "aliases": [],
    "tags": ["strings", "hash_map", "array"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Count characters that appear exactly once in the string and are not followed by the same character later in the string.",
}

def solve(s: str) -> int:
    """
    Counts the number of 'special' characters in a string.
    
    A character is special if it appears exactly once in the string.
    Note: The problem definition for 'Special Characters I' typically 
    refers to characters that appear exactly once in the string.

    Args:
        s: The input string to analyze.

    Returns:
        The count of special characters.

    Examples:
        >>> solve("aba")
        1
        >>> solve("abc")
        3
        >>> solve("aaaaa")
        0
    """
    # Since we are dealing with lowercase English letters, 
    # a frequency array of size 26 is sufficient.
    char_counts = [0] * 26
    
    # First pass: Count the occurrences of each character
    for char in s:
        index = ord(char) - ord('a')
        char_counts[index] += 1
        
    special_count = 0
    
    # Second pass: Count how many characters have a frequency of exactly 1
    for count in char_counts:
        if count == 1:
            special_count += 1
            
    return special_count
