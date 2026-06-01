METADATA = {
    "id": 516,
    "name": "Longest Palindromic Subsequence",
    "slug": "longest-palindromic-subsequence",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dynamic_programming", "string"],
    "difficulty": "medium",
    "time_complexity": "O(n^2)",
    "space_complexity": "O(n^2)",
    "description": "Find the length of the longest subsequence in a string that reads the same forwards and backwards.",
}

def solve(s: str) -> int:
    """
    Calculates the length of the longest palindromic subsequence in the given string.

    The problem is solved using dynamic programming. A subsequence is a sequence 
    that can be derived from another sequence by deleting zero or more elements 
    without changing the order of the remaining elements.

    Args:
        s: The input string.

    Returns:
        The length of the longest palindromic subsequence.

    Examples:
        >>> solve("bbbab")
        4
        >>> solve("cbbd")
        2
    """
    n = len(s)
    if n == 0:
        return 0

    # dp[i][j] will store the length of the longest palindromic subsequence 
    # in the substring s[i...j]
    dp = [[0] * n for _ in range(n)]

    # Every single character is a palindrome of length 1
    for i in range(n):
        dp[i][i] = 1

    # Build the table. We iterate through possible lengths of substrings from 2 to n.
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            
            # If characters at the start and end match
            if s[i] == s[j]:
                # If length is 2, it's just 2. Otherwise, it's 2 + result of inner substring.
                if length == 2:
                    dp[i][j] = 2
                else:
                    dp[i][j] = dp[i + 1][j - 1] + 2
            else:
                # If they don't match, take the maximum by either skipping the first or last char
                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

    return dp[0][n - 1]
