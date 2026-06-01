METADATA = {
    "id": 647,
    "name": "Palindromic Substrings",
    "slug": "palindromic_substrings",
    "category": "String",
    "aliases": [],
    "tags": ["dynamic_programming", "string", "expand_around_center"],
    "difficulty": "medium",
    "time_complexity": "O(n^2)",
    "space_complexity": "O(1)",
    "description": "Count the number of palindromic substrings in a given string.",
}

def solve(s: str) -> int:
    """
    Counts the total number of palindromic substrings in the input string.
    
    The algorithm uses the 'Expand Around Center' approach. For each character 
    (and each gap between characters), we attempt to expand outwards as long 
    as the characters match, incrementing the count for every valid palindrome found.

    Args:
        s: The input string to analyze.

    Returns:
        The total count of palindromic substrings.

    Examples:
        >>> solve("abc")
        3
        >>> solve("aaa")
        6
    """
    if not s:
        return 0

    total_palindromes = 0
    n = len(s)

    def count_palindromes_from_center(left: int, right: int) -> int:
        """
        Helper to expand outwards from a given center and count palindromes.
        
        Args:
            left: Starting left index.
            right: Starting right index.
            
        Returns:
            Number of palindromes found starting from this center.
        """
        count = 0
        # Expand as long as indices are in bounds and characters match
        while left >= 0 and right < n and s[left] == s[right]:
            count += 1
            left -= 1
            right += 1
        return count

    for i in range(n):
        # Case 1: Odd length palindromes (center is a single character)
        total_palindromes += count_palindromes_from_center(i, i)
        
        # Case 2: Even length palindromes (center is the gap between i and i+1)
        total_palindromes += count_palindromes_from_center(i, i + 1)

    return total_palindromes
