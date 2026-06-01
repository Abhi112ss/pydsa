METADATA = {
    "id": 3675,
    "name": "Minimum Operations to Transform String",
    "slug": "minimum-operations-to-transform-string",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dp", "strings"],
    "difficulty": "medium",
    "time_complexity": "O(n*m)",
    "space_complexity": "O(n*m)",
    "description": "Find the minimum number of operations (insert, delete, replace) to transform one string into another.",
}

def solve(source: str, target: str) -> int:
    """
    Calculates the minimum number of operations to transform the source string 
    into the target string using Levenshtein distance algorithm.

    Args:
        source: The starting string.
        target: The destination string.

    Returns:
        The minimum number of operations (insertions, deletions, or substitutions).

    Examples:
        >>> solve("horse", "ros")
        3
        >>> solve("intention", "execution")
        5
    """
    n = len(source)
    m = len(target)

    # Initialize a 2D DP table where dp[i][j] represents the minimum 
    # operations to transform source[0...i-1] to target[0...j-1].
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    # Base cases: transforming a string to an empty string requires deletions.
    for i in range(n + 1):
        dp[i][0] = i
    
    # Base cases: transforming an empty string to a target requires insertions.
    for j in range(m + 1):
        dp[0][j] = j

    # Fill the DP table
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if source[i - 1] == target[j - 1]:
                # Characters match, no new operation needed
                dp[i][j] = dp[i - 1][j - 1]
            else:
                # Choose the minimum of:
                # 1. dp[i-1][j] + 1 (Deletion)
                # 2. dp[i][j-1] + 1 (Insertion)
                # 3. dp[i-1][j-1] + 1 (Substitution)
                dp[i][j] = 1 + min(
                    dp[i - 1][j],      # Deletion
                    dp[i][j - 1],      # Insertion
                    dp[i - 1][j - 1]   # Substitution
                )

    return dp[n][m]
