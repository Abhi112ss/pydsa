METADATA = {
    "id": 1092,
    "name": "Shortest Common Supersequence",
    "slug": "shortest-common-supersequence",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dp", "string", "longest-common-subsequence"],
    "difficulty": "hard",
    "time_complexity": "O(n*m)",
    "space_complexity": "O(n*m)",
    "description": "Find the shortest string that has both input strings as subsequences.",
}

def solve(word1: str, word2: str) -> str:
    """
    Finds the shortest common supersequence of two strings using Dynamic Programming.

    The algorithm first computes the Longest Common Subsequence (LCS) table, 
    then reconstructs the supersequence by traversing the table backwards.

    Args:
        word1: The first input string.
        word2: The second input string.

    Returns:
        The shortest common supersequence string.

    Examples:
        >>> solve("abac", "cab")
        'cabac'
        >>> solve("abc", "def")
        'abcdef'
    """
    n = len(word1)
    m = len(word2)

    # dp[i][j] will store the length of the LCS of word1[0...i-1] and word2[0...j-1]
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if word1[i - 1] == word2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # Reconstruct the supersequence by backtracking through the DP table
    supersequence_chars = []
    i, j = n, m

    while i > 0 and j > 0:
        if word1[i - 1] == word2[j - 1]:
            # Character is part of LCS, add once and move diagonally
            supersequence_chars.append(word1[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            # Character in word1 is not part of LCS at this step, add it and move up
            supersequence_chars.append(word1[i - 1])
            i -= 1
        else:
            # Character in word2 is not part of LCS at this step, add it and move left
            supersequence_chars.append(word2[j - 1])
            j -= 1

    # Append remaining characters from word1 or word2 if one string is exhausted
    while i > 0:
        supersequence_chars.append(word1[i - 1])
        i -= 1
    while j > 0:
        supersequence_chars.append(word2[j - 1])
        j -= 1

    # The characters were added in reverse order
    return "".join(reversed(supersequence_chars))
