METADATA = {
    "id": 680,
    "name": "Valid Palindrome II",
    "slug": "valid_palindrome_ii",
    "category": "String",
    "aliases": ["valid palindrome 2", "valid palindrome two"],
    "tags": ["string", "two_pointer"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Given a string s, return true if the s can be palindrome after deleting at most one character from it.",
}

def solve(s: str) -> bool:
    """
    Determine if a string can become a palindrome by removing at most one character.

    Args:
        s (str): The input string to check.

    Returns:
        bool: True if the string can be a palindrome after at most one deletion.

    Examples:
        >>> solve("aba")
        True
        >>> solve("abca")
        True
        >>> solve("abc")
        False
    """
    def is_palindrome(left: int, right: int) -> bool:
        """Check if substring s[left:right+1] is a palindrome."""
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True

    left = 0
    right = len(s) - 1

    while left < right:
        if s[left] != s[right]:
            # Mismatch found: try skipping either left or right character
            return is_palindrome(left + 1, right) or is_palindrome(left, right - 1)
        left += 1
        right -= 1

    # No mismatch found: already a palindrome
    return True