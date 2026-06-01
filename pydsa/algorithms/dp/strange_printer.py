METADATA = {
    "id": 664,
    "name": "Strange Printer",
    "slug": "strange-printer",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["interval_dp", "dynamic_programming"],
    "difficulty": "hard",
    "time_complexity": "O(n^3)",
    "space_complexity": "O(n^2)",
    "description": "Find the minimum number of turns to print a given string where each turn can print a sequence of the same character.",
}

def solve(s: str) -> int:
    """
    Calculates the minimum number of turns required to print the string s.

    The problem is solved using Interval Dynamic Programming. We define dp[i][j]
    as the minimum number of turns to print the substring from index i to j.
    If s[i] matches some s[k] within the range, we can potentially combine the 
    printing of s[i] with the printing of s[k], reducing the total turns.

    Args:
        s: The target string to be printed.

    Returns:
        The minimum number of turns required to print the string.

    Examples:
        >>> solve("aaa")
        1
        >>> solve("aba")
        2
        >>> solve("abacaba")
        4
    """
    if not s:
        return 0

    # Optimization: Remove consecutive duplicate characters as they don't 
    # change the number of turns required (e.g., "aaabbb" -> "ab").
    unique_chars = []
    if s:
        unique_chars.append(s[0])
        for i in range(1, len(s)):
            if s[i] != s[i - 1]:
                unique_chars.append(s[i])
    
    n = len(unique_chars)
    # dp[i][j] represents the min turns for the substring unique_chars[i...j]
    dp = [[0] * n for _ in range(n)]

    # Base case: single characters take 1 turn
    for i in range(n):
        dp[i][i] = 1

    # Iterate over the length of the interval (from length 2 to n)
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            
            # Initial assumption: print the first character separately, 
            # then add the turns required for the rest of the interval.
            dp[i][j] = 1 + dp[i + 1][j]

            # Try to find a character s[k] that matches s[i] to reduce turns.
            # If s[i] == s[k], the turn used for s[i] can cover s[k] as well.
            for k in range(i + 1, j + 1):
                if unique_chars[i] == unique_chars[k]:
                    # If s[i] == s[k], we split the interval into [i+1...k] and [k+1...j].
                    # Note: dp[i+1][k] already accounts for the turn that covers s[i] and s[k].
                    # We use max(1, ...) logic implicitly by how the subproblems are structured.
                    # The cost is turns for [i+1...k] + turns for [k+1...j].
                    # If k is the end of the range, the second part is 0.
                    left_part = dp[i + 1][k]
                    right_part = dp[k + 1][j] if k + 1 <= j else 0
                    dp[i][j] = min(dp[i][j], left_part + right_part)

    return dp[0][n - 1]
