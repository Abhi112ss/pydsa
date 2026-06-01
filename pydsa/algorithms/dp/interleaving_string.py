METADATA = {
    "id": 97,
    "name": "Interleaving String",
    "slug": "interleaving-string",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dp", "string"],
    "difficulty": "medium",
    "time_complexity": "O(m * n)",
    "space_complexity": "O(m * n)",
    "description": "Determine if a string s3 can be formed by interleaving s1 and s2 while maintaining the relative order of characters in each.",
}

def solve(s1: str, s2: str, s3: str) -> bool:
    """
    Determines if s3 is formed by interleaving s1 and s2.

    Args:
        s1: The first source string.
        s2: The second source string.
        s3: The target string to check for interleaving.

    Returns:
        True if s3 is an interleaving of s1 and s2, False otherwise.

    Examples:
        >>> solve("aabcc", "dbbca", "aadbbcbcac")
        True
        >>> solve("aabcc", "dbbca", "aadbbbaccc")
        False
    """
    m, n = len(s1), len(s2)

    # If the total length doesn't match, it's impossible to interleave
    if m + n != len(s3):
        return False

    # dp[i][j] will be True if s3[0:i+j] can be formed by s1[0:i] and s2[0:j]
    dp: list[list[bool]] = [[False] * (n + 1) for _ in range(m + 1)]

    # Base case: two empty strings form an empty string
    dp[0][0] = True

    # Fill the first column: only using characters from s1
    for i in range(1, m + 1):
        dp[i][0] = dp[i - 1][0] and s1[i - 1] == s3[i - 1]

    # Fill the first row: only using characters from s2
    for j in range(1, n + 1):
        dp[0][j] = dp[0][j - 1] and s2[j - 1] == s3[j - 1]

    # Fill the rest of the DP table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            # Current character in s3 must match either s1[i-1] or s2[j-1]
            # and the previous state must have been valid.
            match_s1 = dp[i - 1][j] and s1[i - 1] == s3[i + j - 1]
            match_s2 = dp[i][j - 1] and s2[j - 1] == s3[i + j - 1]
            dp[i][j] = match_s1 or match_s2

    return dp[m][n]
