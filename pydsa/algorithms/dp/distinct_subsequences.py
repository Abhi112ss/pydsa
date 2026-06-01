METADATA = {
    "id": 115,
    "name": "Distinct Subsequences",
    "slug": "distinct-subsequences",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["string", "dynamic programming", "memoization"],
    "difficulty": "hard",
    "time_complexity": "O(m * n)",
    "space_complexity": "O(m * n)",
    "description": "Given two strings s and t, return the number of distinct subsequences of s which equals t.",
}

def solve(s: str, t: str) -> int:
    """
    Calculates the number of distinct subsequences of s that equal t using 2D dynamic programming.

    Args:
        s: The source string.
        t: The target string to find as a subsequence.

    Returns:
        The total number of distinct subsequences of s that match t.

    Examples:
        >>> solve("rabbbit", "rabbit")
        3
        >>> solve("babgbag", "bag")
        5
    """
    m, n = len(s), len(t)

    # dp[i][j] represents the number of distinct subsequences of s[i:] that match t[j:]
    # We use (m + 1) x (n + 1) to handle empty string base cases.
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Base case: If t is an empty string, there is exactly 1 subsequence (the empty one)
    for i in range(m + 1):
        dp[i][n] = 1

    # Fill the DP table from bottom-up
    for i in range(m - 1, -1, -1):
        for j in range(n - 1, -1, -1):
            # Option 1: Always possible to skip the current character in s
            dp[i][j] = dp[i + 1][j]

            # Option 2: If characters match, we can also choose to include s[i] in our subsequence
            if s[i] == t[j]:
                dp[i][j] += dp[i + 1][j + 1]

    return dp[0][0]
