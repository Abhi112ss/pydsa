METADATA = {
    "id": 1143,
    "name": "Longest Common Subsequence",
    "slug": "longest-common-subsequence",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dynamic_programming", "matrix"],
    "difficulty": "medium",
    "time_complexity": "O(m*n)",
    "space_complexity": "O(m*n)",
    "description": "Find the length of the longest subsequence present in both strings.",
}

def solve(text1: str, text2: str) -> int:
    """
    Calculates the length of the longest common subsequence between two strings.

    Args:
        text1: The first input string.
        text2: The second input string.

    Returns:
        The length of the longest common subsequence.

    Examples:
        >>> solve("abcde", "ace")
        3
        >>> solve("abc", "abc")
        3
        >>> solve("abc", "def")
        0
    """
    m = len(text1)
    n = len(text2)

    # Initialize a 2D DP table with dimensions (m+1) x (n+1)
    # dp[i][j] represents the LCS length of text1[0...i-1] and text2[0...j-1]
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            # If characters match, extend the LCS found so far (diagonal move)
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                # If they don't match, take the maximum from either excluding 
                # the current char of text1 or the current char of text2
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[m][n]
