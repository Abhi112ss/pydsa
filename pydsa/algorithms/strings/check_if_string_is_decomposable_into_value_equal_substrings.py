METADATA = {
    "id": 1933,
    "name": "Check if String Is Decomposable Into Value-Equal Substrings",
    "slug": "check-if-string-is-decomposable-into-value-equal-substrings",
    "category": "String",
    "aliases": [],
    "tags": ["strings", "greedy"],
    "difficulty": "medium",
    "time_complexity": "O(n^2)",
    "space_complexity": "O(1)",
    "description": "Determine if a string can be decomposed into substrings where each substring's integer value equals its length.",
}

def solve(s: str) -> bool:
    """
    Checks if the string can be decomposed into substrings where the integer 
    value of the substring is equal to its length.

    Args:
        s: The input string consisting of digits.

    Returns:
        True if the string is decomposable, False otherwise.

    Examples:
        >>> solve("123")
        True
        >>> solve("10")
        False
        >>> solve("1222")
        True
    """
    n = len(s)
    i = 0

    while i < n:
        # A substring cannot start with '0' unless the value is 0, 
        # but length must be > 0, so '0' is invalid as a starting digit.
        if s[i] == '0':
            return False
        
        found_match = False
        # Try all possible substring lengths starting from index i.
        # The maximum possible length is limited by the remaining string length.
        for length in range(1, n - i + 1):
            substring = s[i : i + length]
            
            # Convert substring to integer to check the condition.
            # Note: The value must equal the length of the substring.
            if int(substring) == length:
                # If a match is found, move the pointer forward by the length.
                i += length
                found_match = True
                break
        
        # If no substring starting at index i satisfies the condition, return False.
        if not found_match:
            return False
            
    return True
