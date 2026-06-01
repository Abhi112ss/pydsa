METADATA = {
    "id": 1216,
    "name": "Valid Palindrome III",
    "slug": "valid-palindrome-iii",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dp", "string"],
    "difficulty": "hard",
    "time_complexity": "O(n^2)",
    "space_complexity": "O(n^2)",
    "description": "Determine if a string can become a palindrome by removing at most k characters.",
}

def solve(s: str, k: int) -> bool:
    """
    Determines if the string 's' can be transformed into a palindrome by 
    removing at most 'k' characters.

    The problem is equivalent to finding the Longest Palindromic Subsequence (LPS)
    of the string. If (length of s - length of LPS) <= k, then it is possible.

    Args:
        s: The input string.
        k: The maximum number of characters allowed to be removed.

    Returns:
        True if the string can become a palindrome by removing at most k characters, 
        False otherwise.

    Examples:
        >>> solve("abcdeca", 2)
        True
        >>> solve("abcdeca", 1)
        False
    """
    n = len(s)
    if n <= 1:
        return True

    # dp[i][j] will store the length of the Longest Palindromic Subsequence 
    # in the substring s[i...j]
    dp = [[0] * n for _ in range(n)]

    # Every single character is a palindrome of length 1
    for i in range(n):
        dp[i][i] = 1

    # Build the DP table for substrings of length 2 up to n
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j]:
                # If characters match, add 2 to the LPS of the inner substring
                dp[i][j] = dp[i + 1][j - 1] + 2 if length > 2 else 2
            else:
                # If they don't match, take the maximum by skipping either i or j
                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

    longest_palindromic_subsequence_length = dp[0][n - 1]
    
    # The number of deletions required is the difference between 
    # total length and the length of the longest palindromic subsequence
    return (n - longest_palindromic_subsequence_length) <= k
