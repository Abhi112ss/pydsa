METADATA = {
    "id": 2330,
    "name": "Valid Palindrome IV",
    "slug": "valid-palindrome-iv",
    "category": "String",
    "aliases": [],
    "tags": ["two_pointer", "greedy", "string"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Determine if a string can become a palindrome by removing at most two characters.",
}

def solve(s: str) -> bool:
    """
    Determines if the string 's' can become a palindrome by removing at most two characters.
    
    The problem asks if we can achieve a palindrome by removing 0, 1, or 2 characters.
    However, the core logic is simpler: if we can remove at most 2 characters to make it 
    a palindrome, we are essentially checking if the string is "almost" a palindrome.
    Actually, the problem is even simpler: can we remove at most 2 characters to make 
    it a palindrome? This is equivalent to checking if the string is a palindrome 
    after skipping at most 2 mismatches.

    Args:
        s: The input string.

    Returns:
        True if the string can become a palindrome by removing at most 2 characters, 
        False otherwise.

    Examples:
        >>> solve("abca")
        True
        >>> solve("abcde")
        False
    """
    
    def is_palindrome_range(left: int, right: int) -> bool:
        """Helper to check if a substring is a palindrome."""
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True

    def check_with_removals(left: int, right: int, removals_left: int) -> bool:
        """
        Recursive helper to check if substring s[left:right+1] can be a palindrome
        given a budget of removals.
        """
        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                # If we have no removals left, this path is invalid
                if removals_left == 0:
                    return False
                
                # Try removing either the left character or the right character
                # and decrement the budget of allowed removals.
                return (check_with_removals(left + 1, right, removals_left - 1) or 
                        check_with_removals(left, right - 1, removals_left - 1))
        return True

    # The problem asks for at most 2 removals.
    # Note: The problem description in LeetCode 2330 actually asks if we can 
    # make it a palindrome by removing at most 2 characters.
    # However, the standard interpretation of "Valid Palindrome IV" is 
    # "can we make it a palindrome by removing at most 2 characters".
    # Wait, looking at the problem constraints and logic: 
    # If we can remove 2 characters, we check if s[i+1...j] or s[i...j-1] 
    # can be a palindrome with 1 removal left.
    
    return check_with_removals(0, len(s) - 1, 2)
