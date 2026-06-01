METADATA = {
    "id": 712,
    "name": "Minimum ASCII Delete Sum for Two Strings",
    "slug": "minimum-ascii-delete-sum-for-two-strings",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dynamic_programming", "string", "sequence"],
    "difficulty": "medium",
    "time_complexity": "O(m*n)",
    "space_complexity": "O(m*n)",
    "description": "Find the minimum ASCII sum of deleted characters to make two strings equal.",
}

def solve(word1: str, word2: str) -> int:
    """
    Calculates the minimum ASCII sum of deleted characters to make two strings equal.

    The problem is a variation of the Longest Common Subsequence (LCS) problem.
    Instead of maximizing the length of the subsequence, we maximize the ASCII 
    sum of the common subsequence. The result is the total ASCII sum of both 
    strings minus twice the ASCII sum of the maximum common subsequence.

    Args:
        word1: The first input string.
        word2: The second input string.

    Returns:
        The minimum ASCII sum of deleted characters.

    Examples:
        >>> solve("sea", "eat")
        230
        >>> solve("delete", "leet")
        403
    """
    m, n = len(word1), len(word2)

    # dp[i][j] will store the minimum ASCII delete sum for word1[i:] and word2[j:]
    # We use a 2D array for clarity, though it can be optimized to 1D.
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Base case: If one string is empty, we must delete all characters of the other string
    for i in range(m - 1, -1, -1):
        dp[i][n] = dp[i + 1][n] + ord(word1[i])
    
    for j in range(n - 1, -1, -1):
        dp[m][j] = dp[m][j + 1] + ord(word2[j])

    # Fill the DP table from bottom-right to top-left
    for i in range(m - 1, -1, -1):
        for j in range(n - 1, -1, -1):
            if word1[i] == word2[j]:
                # If characters match, no deletion needed for this pair
                dp[i][j] = dp[i + 1][j + 1]
            else:
                # If they don't match, we take the minimum of deleting from word1 or word2
                delete_from_word1 = ord(word1[i]) + dp[i + 1][j]
                delete_from_word2 = ord(word2[j]) + dp[i][j + 1]
                dp[i][j] = min(delete_from_word1, delete_from_word2)

    return dp[0][0]
