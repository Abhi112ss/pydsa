METADATA = {
    "id": 44,
    "name": "Wildcard Matching",
    "slug": "wildcard-matching",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dynamic_programming", "greedy", "string", "two_pointers"],
    "difficulty": "hard",
    "time_complexity": "O(m*n)",
    "space_complexity": "O(m*n)",
    "description": "Implement wildcard pattern matching with support for '?' and '*'.",
}

def solve(s: str, p: str) -> bool:
    """
    Determines if a string matches a pattern containing '?' and '*'.
    '?' matches any single character.
    '*' matches any sequence of characters (including the empty sequence).

    Args:
        s: The input string to match.
        p: The pattern string containing wildcards.

    Returns:
        True if the pattern matches the string, False otherwise.

    Examples:
        >>> solve("aa", "a")
        False
        >>> solve("aa", "*")
        True
        >>> solve("cb", "?a")
        False
        >>> solve("adceb", "*a*b")
        True
        >>> solve("acdcb", "a*c?b")
        False
    """
    m, n = len(s), len(p)
    
    # dp[i][j] will be True if the first i characters of s 
    # match the first j characters of p.
    dp = [[False] * (n + 1) for _ in range(m + 1)]

    # Base case: empty string matches empty pattern
    dp[0][0] = True

    # Handle patterns that start with '*' which can match an empty string
    for j in range(1, n + 1):
        if p[j - 1] == '*':
            dp[0][j] = dp[0][j - 1]
        else:
            # Once we hit a non-star character, no subsequent 
            # pattern can match an empty string
            break

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if p[j - 1] == '*':
                # Two cases for '*':
                # 1. '*' matches zero characters: dp[i][j-1]
                # 2. '*' matches one or more characters: dp[i-1][j]
                dp[i][j] = dp[i][j - 1] or dp[i - 1][j]
            elif p[j - 1] == '?' or s[i - 1] == p[j - 1]:
                # Current characters match, look at the previous state
                dp[i][j] = dp[i - 1][j - 1]
            else:
                # Characters do not match
                dp[i][j] = False

    return dp[m][n]
