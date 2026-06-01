METADATA = {
    "id": 2947,
    "name": "Count Beautiful Substrings I",
    "slug": "count-beautiful-substrings-i",
    "category": "String",
    "aliases": [],
    "tags": ["hash_map", "strings", "substring"],
    "difficulty": "medium",
    "time_complexity": "O(n^2)",
    "space_complexity": "O(1)",
    "description": "Count substrings where the number of vowels equals the number of consonants, and the product of vowel and consonant counts is divisible by k.",
}

def solve(word: str, k: int) -> int:
    """
    Counts the number of 'beautiful' substrings in a given word.
    
    A substring is beautiful if:
    1. The number of vowels equals the number of consonants.
    2. The product of the number of vowels and the number of consonants is divisible by k.

    Args:
        word: The input string consisting of lowercase English letters.
        k: The divisor for the product condition.

    Returns:
        The total count of beautiful substrings.

    Examples:
        >>> solve("Leeetcode", 5)
        0
        >>> solve("aazz", 2)
        2
    """
    vowels_set = {'a', 'e', 'i', 'o', 'u'}
    n = len(word)
    beautiful_count = 0

    # Iterate through every possible starting position of a substring
    for start_index in range(n):
        vowel_count = 0
        consonant_count = 0
        
        # Expand the substring from the start_index to the end of the word
        for end_index in range(start_index, n):
            if word[end_index] in vowels_set:
                vowel_count += 1
            else:
                consonant_count += 1
            
            # Check the two conditions for a 'beautiful' substring
            # 1. Equal number of vowels and consonants
            # 2. Product of counts is divisible by k
            if vowel_count == consonant_count:
                product = vowel_count * consonant_count
                if product % k == 0:
                    beautiful_count += 1
                    
    return beautiful_count
