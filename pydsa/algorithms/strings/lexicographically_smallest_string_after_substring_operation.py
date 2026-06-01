METADATA = {
    "id": 2734,
    "name": "Lexicographically Smallest String After Substring Operation",
    "slug": "lexicographically-smallest-string-after-substring-operation",
    "category": "String",
    "aliases": [],
    "tags": ["strings", "greedy"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Find the lexicographically smallest string possible by choosing a substring and replacing it with its reverse.",
}

def solve(s: str) -> str:
    """
    Finds the lexicographically smallest string possible by reversing a substring.
    
    The optimal strategy is to find the first occurrence where a character is 
    strictly greater than the character immediately following it. Reversing 
    the substring starting from this character to the end of the string 
    will result in the lexicographically smallest result. If no such character 
    exists (the string is non-decreasing), the string is already the smallest.

    Args:
        s: The input string.

    Returns:
        The lexicographically smallest string after one substring reversal.

    Examples:
        >>> solve("cbabc")
        'abcbc'
        >>> solve("ba")
        'ab'
        >>> solve("abc")
        'abc'
    """
    n = len(s)
    # Convert to list for efficient slicing and manipulation
    chars = list(s)
    
    # Find the first index i where chars[i] > chars[i+1]
    # This is the first point where the string "descends" lexicographically
    pivot_index = -1
    for i in range(n - 1):
        if chars[i] > chars[i + 1]:
            pivot_index = i
            break
            
    # If no such index is found, the string is already sorted non-decreasingly
    if pivot_index == -1:
        return s
        
    # To get the smallest string, we reverse the substring from the pivot 
    # to the end of the string. This moves the smaller characters 
    # (which were at the end) to the front of the suffix.
    prefix = chars[:pivot_index]
    suffix_reversed = chars[pivot_index:][::-1]
    
    return "".join(prefix + suffix_reversed)
