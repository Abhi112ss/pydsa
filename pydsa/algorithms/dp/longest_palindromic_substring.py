METADATA = {
    "id": 5,
    "name": "Longest Palindromic Substring",
    "slug": "longest-palindromic-substring",
    "category": "String",
    "aliases": [],
    "tags": ["string", "dynamic_programming", "expand_around_center"],
    "difficulty": "medium",
    "time_complexity": "O(n^2)",
    "space_complexity": "O(1)",
    "description": "Find the longest contiguous substring within a string that reads the same forwards and backwards.",
}

def solve(s: str) -> str:
    """
    Finds the longest palindromic substring in the given string using the 
    expand around center approach.

    Args:
        s: The input string to search.

    Returns:
        The longest substring that is a palindrome. Returns an empty string if input is empty.

    Examples:
        >>> solve("babad")
        "bab"  # Note: "aba" is also valid
        >>> solve("cbbd")
        "bb"
    """
    if not s:
        return ""

    start_index = 0
    max_length = 0

    def expand_around_center(left: int, right: int) -> int:
        """
        Expands outwards from the given indices as long as the characters match.
        
        Args:
            left: The starting left index.
            right: The starting right index.
            
        Returns:
            The length of the palindrome found.
        """
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        # The loop terminates when s[left] != s[right] or boundaries are hit.
        # The length is (right - 1) - (left + 1) + 1 = right - left - 1
        return right - left - 1

    for i in range(len(s)):
        # Case 1: Odd length palindrome (center is a single character)
        len1 = expand_around_center(i, i)
        
        # Case 2: Even length palindrome (center is between two characters)
        len2 = expand_around_center(i, i + 1)
        
        # Determine the longest palindrome found at this center
        current_max_len = max(len1, len2)
        
        # If we found a new longest palindrome, update the global boundaries
        if current_max_len > max_length:
            max_length = current_max_len
            # Calculate the start index based on the center i and the length
            # For both odd and even, this formula works to find the start
            start_index = i - (current_max_len - 1) // 2

    return s[start_index : start_index + max_length]
