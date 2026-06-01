METADATA = {
    "id": 3735,
    "name": "Lexicographically Smallest String After Reverse II",
    "slug": "lexicographically_smallest_string_after_reverse_ii",
    "category": "String",
    "aliases": [],
    "tags": ["string_manipulation", "greedy"],
    "difficulty": "medium",
    "time_complexity": "O(n^2)",
    "space_complexity": "O(n)",
    "description": "Find the lexicographically smallest string possible by reversing exactly one contiguous substring.",
}

def solve(s: str) -> str:
    """
    Finds the lexicographically smallest string possible by reversing exactly one 
    contiguous substring of the input string s.

    Args:
        s: The input string to manipulate.

    Returns:
        The lexicographically smallest string after one substring reversal.

    Examples:
        >>> solve("baaa")
        "aaab"
        >>> solve("abcde")
        "abcde"
        >>> solve("dcba")
        "abcd"
    """
    n = len(s)
    if n <= 1:
        return s

    # Initialize the best string as the original string
    # This covers the case where no reversal makes the string smaller
    min_string = s

    # Convert to list for easier slicing/manipulation if needed, 
    # but string slicing is efficient in Python.
    
    # Iterate through all possible start indices of the reversal window
    for start in range(n):
        # Iterate through all possible end indices of the reversal window
        # We start from start + 1 because reversing a single character does nothing
        for end in range(start + 1, n + 1):
            # Construct the new string:
            # prefix + reversed_substring + suffix
            prefix = s[:start]
            substring_to_reverse = s[start:end]
            suffix = s[end:]
            
            # Python's slicing [::-1] is highly optimized for reversing
            candidate = prefix + substring_to_reverse[::-1] + suffix
            
            # Update min_string if the candidate is lexicographically smaller
            if candidate < min_string:
                min_string = candidate
                
    return min_string
