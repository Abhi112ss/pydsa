METADATA = {
    "id": 3223,
    "name": "Minimum Length of String After Operations",
    "slug": "minimum-length-of-string-after-operations",
    "category": "String",
    "aliases": [],
    "tags": ["string", "stack", "greedy"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Find the minimum length of a string after repeatedly removing any substring of length 3 or more consisting of the same character.",
}

def solve(s: str) -> int:
    """
    Calculates the minimum length of the string after performing the removal operation.
    
    The operation allows removing any substring of length 3 or more consisting of 
    the same character. To minimize the length, we want to reduce each contiguous 
    block of identical characters to either 1 or 2 characters.
    
    Specifically:
    - If a block has an odd length (e.g., 5), it can be reduced to 1.
    - If a block has an even length (e.g., 4), it can be reduced to 2.
    
    Args:
        s: The input string.
        
    Returns:
        The minimum possible length of the string after all possible operations.
        
    Examples:
        >>> solve("aaabbb")
        2
        >>> solve("aaabbbaaa")
        3
        >>> solve("aabbcc")
        6
    """
    if not s:
        return 0

    n = len(s)
    total_min_length = 0
    i = 0

    while i < n:
        current_char = s[i]
        count = 0
        
        # Count the length of the current contiguous block of identical characters
        while i < n and s[i] == current_char:
            count += 1
            i += 1
        
        # If the block length is odd, it can be reduced to 1 character.
        # If the block length is even, it can be reduced to 2 characters.
        # This is because we can always pick a substring of length 3 to remove 
        # until we are left with 1 or 2.
        if count % 2 == 1:
            total_min_length += 1
        else:
            total_min_length += 2
            
    return total_min_length
