METADATA = {
    "id": 1246,
    "name": "Palindrome Removal",
    "slug": "palindrome-removal",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dynamic_programming", "interval_dp"],
    "difficulty": "hard",
    "time_complexity": "O(n^3)",
    "space_complexity": "O(n^2)",
    "description": "Find the minimum number of operations to remove a string by removing palindromic substrings.",
}

def solve(s: str) -> int:
    """
    Calculates the minimum number of operations to remove all characters from a string,
    where an operation consists of removing a palindromic substring.

    Args:
        s: The input string consisting of lowercase English letters.

    Returns:
        The minimum number of operations required to remove the entire string.

    Examples:
        >>> solve("abacaba")
        1
        >>> solve("abc")
        3
        >>> solve("aa")
        1
    """
    n = len(s)
    if n == 0:
        return 0

    # dp[i][j] represents the minimum operations to remove substring s[i:j+1]
    dp = [[0] * n for _ in range(n)]

    for length in range(1, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1

            # Base case: single character requires 1 operation
            if length == 1:
                dp[i][j] = 1
                continue

            # Default case: treat the interval as two separate parts (i and i+1...j)
            # We initialize with the worst case: removing s[i] then removing the rest
            dp[i][j] = 1 + dp[i + 1][j]

            # If the first two characters match, they can be removed together
            # as part of a palindrome (e.g., "aa"), effectively costing the same
            # as removing the rest of the string starting from index i+2
            if s[i] == s[i + 1]:
                dp[i][j] = min(dp[i][j], 1 + dp[i + 2][j] if i + 2 <= j else 1)

            # Try to find a character s[k] that matches s[i] to form a palindrome
            # If s[i] == s[k], the cost to remove s[i] and s[k] is absorbed into 
            # the cost of removing the inner part s[i+1:k]
            for k in range(i + 2, j + 1):
                if s[i] == s[k]:
                    # The cost to remove s[i...k] is the same as removing s[i+1...k-1]
                    # because s[i] and s[k] can be removed along with the last 
                    # palindrome removed from the inner range.
                    dp[i][j] = min(dp[i][j], dp[i + 1][k - 1] + (dp[k + 1][j] if k + 1 <= j else 0))

    return dp[0][n - 1]
