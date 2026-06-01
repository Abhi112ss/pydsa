METADATA = {
    "id": 1312,
    "name": "Minimum Insertion Steps to Make a String Palindrome",
    "slug": "minimum-insertion-steps-to-make-a-string-palindrome",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dynamic_programming", "lcs", "string"],
    "difficulty": "medium",
    "time_complexity": "O(n^2)",
    "space_complexity": "O(n^2)",
    "description": "Find the minimum number of insertions needed to make a given string a palindrome.",
}

def solve(s: str) -> int:
    """
    Calculates the minimum number of insertions required to make the string a palindrome.
    
    The problem is equivalent to finding the Longest Palindromic Subsequence (LPS).
    The minimum insertions needed is: length(s) - length(LPS).
    LPS can be found by calculating the Longest Common Subsequence (LCS) between 
    the string and its reverse.

    Args:
        s: The input string.

    Returns:
        The minimum number of insertions required.

    Examples:
        >>> solve("zzazz")
        0
        >>> solve("mbadm")
        2
        >>> solve("leetcode")
        5
    """
    n = len(s)
    if n <= 1:
        return 0

    # The Longest Palindromic Subsequence is the Longest Common Subsequence
    # between the string and its reverse.
    reversed_s = s[::-1]
    
    # dp[i][j] will store the length of LCS of s[0...i-1] and reversed_s[0...j-1]
    # We use a 2D array for clarity, though it can be optimized to O(n) space.
    dp = [[0] * (n + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if s[i - 1] == reversed_s[j - 1]:
                # If characters match, increment the length from the previous diagonal
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                # If characters don't match, take the maximum from top or left cell
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    longest_palindromic_subsequence_length = dp[n][n]
    
    # The result is the total length minus the characters that already form a palindrome
    return n - longest_palindromic_subsequence_length
