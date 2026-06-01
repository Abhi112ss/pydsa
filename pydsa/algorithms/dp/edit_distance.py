METADATA = {
    "id": 72,
    "name": "Edit Distance",
    "slug": "edit-distance",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dynamic_programming", "string", "matrix"],
    "difficulty": "hard",
    "time_complexity": "O(m*n)",
    "space_complexity": "O(m*n)",
    "description": "Find the minimum number of operations required to convert one word to another using insertion, deletion, or substitution.",
}

def solve(word1: str, word2: str) -> int:
    """
    Calculates the minimum number of operations (insert, delete, replace) 
    to convert word1 into word2 using dynamic programming.

    Args:
        word1: The source string.
        word2: The target string.

    Returns:
        The minimum number of edit operations required.

    Examples:
        >>> solve("horse", "ros")
        3
        >>> solve("intention", "execution")
        5
    """
    m = len(word1)
    n = len(word2)

    # dp[i][j] will hold the edit distance between word1[0...i-1] and word2[0...j-1]
    # We use (m+1) x (n+1) to account for empty string cases
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Base case: converting a string of length i to an empty string requires i deletions
    for i in range(m + 1):
        dp[i][0] = i

    # Base case: converting an empty string to a string of length j requires j insertions
    for j in range(n + 1):
        dp[0][j] = j

    # Fill the DP table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i - 1] == word2[j - 1]:
                # Characters match, no new operation needed
                dp[i][j] = dp[i - 1][j - 1]
            else:
                # Characters mismatch, take the minimum of:
                # 1. dp[i-1][j] + 1 (Deletion)
                # 2. dp[i][j-1] + 1 (Insertion)
                # 3. dp[i-1][j-1] + 1 (Substitution)
                dp[i][j] = 1 + min(
                    dp[i - 1][j],      # Delete
                    dp[i][j - 1],      # Insert
                    dp[i - 1][j - 1]   # Replace
                )

    return dp[m][n]
