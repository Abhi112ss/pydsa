METADATA = {
    "id": 3541,
    "name": "Find Most Frequent Vowel and Consonant",
    "slug": "find_most_frequent_vowel_and_consonant",
    "category": "String",
    "aliases": [],
    "tags": ["hash_map", "string_traversal"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the most frequent vowel and the most frequent consonant in a given string.",
}

def solve(s: str) -> dict[str, str]:
    """
    Finds the most frequent vowel and the most frequent consonant in the input string.
    
    If there is a tie in frequency, the character that appears first in the 
    alphabetical order is returned. If no vowels or no consonants exist, 
    the respective value is an empty string.

    Args:
        s: The input string to analyze.

    Returns:
        A dictionary containing two keys: 'vowel' and 'consonant', 
        mapping to the most frequent character found.

    Examples:
        >>> solve("leetcode")
        {'vowel': 'e', 'consonant': 'c'}
        >>> solve("apple")
        {'vowel': 'e', 'consonant': 'p'}
        >>> solve("xyz")
        {'vowel': '', 'consonant': 'x'}
    """
    vowels_set = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    
    # Frequency maps for vowels and consonants
    vowel_counts: dict[str, int] = {}
    consonant_counts: dict[str, int] = {}

    for char in s:
        if not char.isalpha():
            continue
            
        # Normalize to lowercase for consistent counting
        lower_char = char.lower()
        
        if lower_char in vowels_set:
            vowel_counts[lower_char] = vowel_counts.get(lower_char, 0) + 1
        else:
            consonant_counts[lower_char] = consonant_counts.get(lower_char, 0) + 1

    def get_most_frequent(counts: dict[str, int]) -> str:
        if not counts:
            return ""
        
        # Find the maximum frequency
        max_freq = max(counts.values())
        
        # Filter candidates that have the max frequency
        candidates = [char for char, freq in counts.items() if freq == max_freq]
        
        # Return the lexicographically smallest character among candidates
        return min(candidates)

    # Calculate results using the helper
    return {
        "vowel": get_most_frequent(vowel_counts),
        "consonant": get_most_frequent(consonant_counts)
    }
