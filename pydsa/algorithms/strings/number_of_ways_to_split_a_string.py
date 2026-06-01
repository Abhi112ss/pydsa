METADATA = {
    "id": 1573,
    "name": "Number of Ways to Split a String",
    "slug": "number-of-ways-to-split-a-string",
    "category": "String",
    "aliases": [],
    "tags": ["string", "prefix_sum", "counting"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Count the number of ways to split a string into two non-empty parts such that both parts have the same number of vowels and consonants.",
}

def solve(s: str) -> int:
    """
    Calculates the number of ways to split a string into two non-empty parts
    where both parts contain the same number of vowels and consonants.

    Args:
        s: The input string consisting of lowercase English letters.

    Returns:
        The number of valid split points.

    Examples:
        >>> solve("aacaba")
        2
        >>> solve("abc")
        0
    """
    vowels_set = {'a', 'e', 'i', 'o', 'u'}
    
    total_vowels = 0
    total_consonants = 0
    
    # First pass: Calculate the total count of vowels and consonants in the string
    for char in s:
        if char in vowels_set:
            total_vowels += 1
        else:
            total_consonants += 1
            
    ways_to_split = 0
    current_vowels = 0
    current_consonants = 0
    
    # Second pass: Iterate through the string up to the second to last character
    # (since both parts must be non-empty)
    for i in range(len(s) - 1):
        char = s[i]
        if char in vowels_set:
            current_vowels += 1
        else:
            current_consonants += 1
            
        # Calculate remaining counts for the second part
        remaining_vowels = total_vowels - current_vowels
        remaining_consonants = total_consonants - current_consonants
        
        # Check if the counts match for both vowels and consonants
        if current_vowels == remaining_vowels and current_consonants == remaining_consonants:
            ways_to_split += 1
            
    return ways_to_split
