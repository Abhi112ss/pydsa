METADATA = {
    "id": 583,
    "name": "Delete Operation for Two Strings",
    "slug": "delete-operation-for-two-strings",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dynamic_programming", "lcs", "string"],
    "difficulty": "medium",
    "time_complexity": "O(m*n)",
    "space_complexity": "O(m*n)",
    "description": "Find the minimum number of deletions required to make two strings identical.",
}

def solve(word1: str, word2: str) -> int:
    """
    Calculates the minimum number of deletions to make two strings equal.
    
    The problem is solved by finding the Longest Common Subsequence (LCS).
    The minimum deletions required is: (len(word1) - LCS) + (len(word2) - LCS).

    Args:
        word1: The first input string.
        word2: The second input string.

    Returns:
        The minimum number of deletions needed to make word1 and word2 identical.

    Examples:
        >>> solve("sea", "eat")
        2
        >>> solve("leetcode", "etco")
        4
    """
    m = len(word1)
    n = len(word2)

    # Initialize a 2D DP table where dp[i][j] stores the length of 
    # the LCS of word1[0...i-1] and word2[0...j-1].
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Fill the DP table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i - 1] == word2[j - 1]:
                # If characters match, extend the previous LCS length
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                # If they don't match, take the maximum from either skipping 
                # a character in word1 or word2
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    lcs_length = dp[m][n]

    # Total deletions = (chars to remove from word1) + (chars to remove from word2)
    # This is equivalent to (m - lcs_length) + (n - lcs_length)
    return (m + n) - (2 * lcs_length)
