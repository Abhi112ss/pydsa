METADATA = {
    "id": 1930,
    "name": "Unique Length-3 Palindromic Subsequences",
    "slug": "unique-length-3-palindromic-subsequences",
    "category": "String",
    "aliases": [],
    "tags": ["strings", "hash_set"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the number of unique length-3 palindromic subsequences in a given string.",
}

def solve(s: str) -> int:
    """
    Calculates the number of unique length-3 palindromic subsequences in the string.
    
    A length-3 palindrome is defined by the pattern 'aba', where the first 
    and last characters are identical. To find unique ones, we identify 
    the first and last occurrence of every character 'a' and count how many 
    unique characters exist between those two indices.

    Args:
        s: The input string.

    Returns:
        The count of unique length-3 palindromic subsequences.

    Examples:
        >>> solve("aabca")
        3
        >>> solve("aabaa")
        3
    """
    # Dictionary to store the first and last index of each character encountered
    # Key: character, Value: [first_index, last_index]
    char_range = {}

    for index, char in enumerate(s):
        if char not in char_range:
            char_range[char] = [index, index]
        else:
            char_range[char][1] = index

    unique_palindromes_count = 0

    # Iterate through each character that could serve as the 'outer' part of the palindrome
    for char in char_range:
        first_idx, last_idx = char_range[char]
        
        # A length-3 palindrome requires at least 3 characters between the same outer chars
        if last_idx - first_idx > 1:
            # Use a set to find unique characters strictly between the first and last occurrence
            # Since the alphabet is limited (lowercase English), this set size is at most 26
            middle_chars = set()
            for i in range(first_idx + 1, last_idx):
                middle_chars.add(s[i])
            
            unique_palindromes_count += len(middle_chars)

    return unique_palindromes_count
