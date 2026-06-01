METADATA = {
    "id": 10,
    "name": "Regular Expression Matching",
    "slug": "regular-expression-matching",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dynamic_programming", "recursion", "string"],
    "difficulty": "hard",
    "time_complexity": "O(m * n)",
    "space_complexity": "O(m * n)",
    "description": "Implement regular expression matching with support for '.' and '*'.",
}

def solve(s: str, p: str) -> bool:
    """
    Determates if a string matches a pattern containing '.' and '*'.

    '.' Matches any single character.
    '*' Matches zero or more of the preceding element.

    Args:
        s: The input string to match.
        p: The pattern string containing '.' and '*'.

    Returns:
        True if the string matches the pattern, False otherwise.

    Examples:
        >>> solve("aa", "a")
        False
        >>> solve("aa", "a*")
        True
        >>> solve("ab", ".*")
        True
        >>> solve("aab", "c*a*b")
        True
    """
    m, n = len(s), len(p)

    # dp[i][j] will be True if s[i:] matches p[j:]
    # We use (m+1) x (n+1) to account for empty string/pattern cases
    dp = [[False] * (n + 1) for _ in range(m + 1)]

    # Base case: empty string matches empty pattern
    dp[m][n] = True

    # Fill the DP table from bottom-up (backwards)
    for i in range(m, -1, -1):
        for j in range(n - 1, -1, -1):
            # Check if the current characters match
            first_match = i < m and (p[j] == s[i] or p[j] == '.')

            # Handle the '*' wildcard case
            if j + 1 < n and p[j + 1] == '*':
                # Two choices for '*':
                # 1. Skip the '*' and its preceding character (zero occurrences)
                # 2. If first_match is true, move to the next character in 's' (one or more occurrences)
                dp[i][j] = dp[i][j + 2] or (first_match and dp[i + 1][j])
            else:
                # Standard matching case (no '*')
                dp[i][j] = first_match and dp[i + 1][j + 1]

    return dp[0][0]
