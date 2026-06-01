METADATA = {
    "id": 3579,
    "name": "Minimum Steps to Convert String with Operations",
    "slug": "minimum-steps-to-convert-string-with-operations",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dp", "strings", "edit-distance"],
    "difficulty": "medium",
    "time_complexity": "O(n * m)",
    "space_complexity": "O(n * m)",
    "description": "Find the minimum number of operations (insert, delete, replace) to convert one string to another.",
}

def solve(source: str, target: str) -> int:
    """
    Calculates the minimum number of operations (insert, delete, replace) 
    required to transform the source string into the target string.

    This is a classic implementation of the Levenshtein Distance algorithm 
    using dynamic programming.

    Args:
        source: The original string to be transformed.
        target: The destination string.

    Returns:
        The minimum number of edit operations required.

    Examples:
        >>> solve("horse", "ros")
        3
        >>> solve("intention", "execution")
        5
    """
    n = len(source)
    m = len(target)

    # Create a 2D DP table where dp[i][j] represents the minimum 
    # operations to convert source[0...i-1] to target[0...j-1].
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    # Base case: converting a string to an empty string requires 
    # deleting all characters.
    for i in range(n + 1):
        dp[i][0] = i

    # Base case: converting an empty string to a target string 
    # requires inserting all characters.
    for j in range(m + 1):
        dp[0][j] = j

    # Fill the DP table
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if source[i - 1] == target[j - 1]:
                # Characters match, no new operation needed
                dp[i][j] = dp[i - 1][j - 1]
            else:
                # Characters mismatch, take the minimum of:
                # 1. Replace: dp[i-1][j-1] + 1
                # 2. Delete:  dp[i-1][j] + 1
                # 3. Insert:  dp[i][j-1] + 1
                dp[i][j] = 1 + min(
                    dp[i - 1][j - 1],  # Replace
                    dp[i - 1][j],      # Delete
                    dp[i][j - 1]       # Insert
                )

    return dp[n][m]
