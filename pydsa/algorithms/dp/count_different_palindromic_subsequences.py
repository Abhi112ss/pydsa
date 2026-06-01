METADATA = {
    "id": 730,
    "name": "Count Different Palindromic Subsequences",
    "slug": "count-different-palindromic-subsequences",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dynamic_programming", "string", "interval_dp"],
    "difficulty": "hard",
    "time_complexity": "O(n^2)",
    "space_complexity": "O(n^2)",
    "description": "Count the number of unique palindromic subsequences in a given string modulo 10^9 + 7.",
}

def solve(s: str) -> int:
    """
    Counts the number of unique palindromic subsequences in string s using interval DP.

    The algorithm uses a 2D DP table where dp[i][j] represents the number of 
    unique palindromic subsequences in the substring s[i:j+1].

    Args:
        s: The input string containing characters 'a', 'b', 'c', or 'd'.

    Returns:
        The count of unique palindromic subsequences modulo 10^9 + 7.

    Examples:
        >>> solve("bccb")
        6
        >>> solve("abcd")
        4
    """
    MOD = 1_000_000_007
    n = len(s)
    # dp[i][j] stores the count of unique palindromic subsequences in s[i...j]
    dp = [[0] * n for _ in range(n)]

    # Base case: single characters are palindromes
    for i in range(n):
        dp[i][i] = 1

    # Iterate over the length of the substring
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1

            if s[i] == s[j]:
                # Find the first and last occurrence of s[i] inside the range (i, j)
                left = i + 1
                right = j - 1
                while left <= right and s[left] != s[i]:
                    left += 1
                while left <= right and s[right] != s[i]:
                    right -= 1

                if left > right:
                    # Case 1: No occurrence of s[i] between i and j
                    # e.g., "aba" -> subsequences: "a", "b", "aa", "aba"
                    # The formula is 2 * dp[i+1][j-1] + 2
                    dp[i][j] = dp[i + 1][j - 1] * 2 + 2
                elif left == right:
                    # Case 2: Exactly one occurrence of s[i] between i and j
                    # e.g., "aaa" -> subsequences: "a", "aa", "aaa"
                    # The formula is 2 * dp[i+1][j-1] + 1
                    dp[i][j] = dp[i + 1][j - 1] * 2 + 1
                else:
                    # Case 3: Two or more occurrences of s[i] between i and j
                    # e.g., "a...a...a...a"
                    # We must subtract the inner duplicates to avoid overcounting
                    dp[i][j] = dp[i + 1][j - 1] * 2 - dp[left + 1][right - 1]
            else:
                # Standard inclusion-exclusion for interval DP
                dp[i][j] = dp[i + 1][j] + dp[i][j - 1] - dp[i + 1][j - 1]

            # Apply modulo and handle negative results from subtraction
            dp[i][j] %= MOD

    return (dp[0][n - 1] + MOD) % MOD
