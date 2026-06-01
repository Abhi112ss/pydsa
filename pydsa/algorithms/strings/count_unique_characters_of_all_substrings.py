METADATA = {
    "id": 828,
    "name": "Count Unique Characters of All Substrings of a Given String",
    "slug": "count-unique-characters-of-all-substrings-of-a-given-string",
    "category": "Math",
    "aliases": [],
    "tags": ["dynamic_programming", "math", "string"],
    "difficulty": "hard",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Calculate the sum of unique characters in all possible substrings of a given string.",
}

def solve(s: str) -> int:
    """
    Calculates the sum of unique characters in all possible substrings of s.
    
    A character is unique in a substring if it appears exactly once in that substring.
    The algorithm uses the contribution technique: for each character at index i, 
    we calculate how many substrings contain this specific instance of the character 
    as its only occurrence of that character.

    Args:
        s: The input string consisting of uppercase and lowercase English letters.

    Returns:
        The total count of unique characters across all substrings.

    Examples:
        >>> solve("ABC")
        10
        >>> solve("ABA")
        8
    """
    n = len(s)
    # Store the indices of each character occurrence.
    # We initialize with -1 and n to act as boundaries for the calculation.
    char_indices: dict[str, list[int]] = {}
    for index, char in enumerate(s):
        if char not in char_indices:
            char_indices[char] = [-1]
        char_indices[char].append(index)
    
    total_unique_count = 0
    
    for char in char_indices:
        # Append the boundary index 'n' to handle the last occurrence
        if char_indices[char][-1] != n - 1:
            char_indices[char].append(n)
            
        indices = char_indices[char]
        
        # For each occurrence of the character at indices[i], it is unique in 
        # substrings that start after indices[i-1] and end before indices[i+1].
        # The number of such substrings is (current_index - prev_index) * (next_index - current_index).
        for i in range(1, len(indices) - 1):
            prev_idx = indices[i - 1]
            curr_idx = indices[i]
            next_idx = indices[i + 1]
            
            left_choices = curr_idx - prev_idx
            right_choices = next_idx - curr_idx
            
            total_unique_count += left_choices * right_choices
            
    return total_unique_count
