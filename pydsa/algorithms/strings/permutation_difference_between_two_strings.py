METADATA = {
    "id": 3146,
    "name": "Permutation Difference between Two Strings",
    "slug": "permutation-difference-between-two-strings",
    "category": "Strings",
    "aliases": [],
    "tags": ["strings", "hash_map"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Find the maximum absolute difference between the indices of the same characters in two strings that are permutations of each other.",
}

def solve(s1: str, s2: str) -> int:
    """
    Calculates the maximum absolute difference between the indices of 
    the same characters in two strings.

    Args:
        s1: The first string.
        s2: The second string (a permutation of s1).

    Returns:
        The maximum absolute difference between indices of identical characters.

    Examples:
        >>> solve("abc", "cba")
        2
        >>> solve("abb", "bab")
        1
    """
    # Map each character in the first string to its index
    char_to_index_s1 = {char: index for index, char in enumerate(s1)}
    
    max_difference = 0
    
    # Iterate through the second string and compare indices
    for index_s2, char in enumerate(s2):
        # Retrieve the index of the same character from the first string
        index_s1 = char_to_index_s1[char]
        
        # Calculate the absolute difference and update the maximum found so far
        current_difference = abs(index_s1 - index_s2)
        if current_difference > max_difference:
            max_difference = current_difference
            
    return max_difference
