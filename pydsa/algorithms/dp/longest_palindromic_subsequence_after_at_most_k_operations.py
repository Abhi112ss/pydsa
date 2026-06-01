METADATA = {
    "id": 3472,
    "name": "Longest Palindromic Subsequence After at Most K Operations",
    "slug": "longest_palindromic_subsequence_after_at_most_k_operations",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dynamic_programming", "strings"],
    "difficulty": "hard",
    "time_complexity": "O(n^2 * k)",
    "space_complexity": "O(n^2 * k)",
    "description": "Find the length of the longest palindromic subsequence possible by changing at most k characters in the string.",
}

def solve(s: str, k: int) -> int:
    """
    Calculates the length of the longest palindromic subsequence possible 
    by performing at most k character changes.

    Args:
        s: The input string.
        k: The maximum number of character changes allowed.

    Returns:
        The length of the longest palindromic subsequence.

    Examples:
        >>> solve("abcde", 1)
        3
        >>> solve("aba", 0)
        3
        >>> solve("abacaba", 2)
        7
    """
    n = len(s)
    if n == 0:
        return 0

    # dp[i][j][ops] represents the length of the longest palindromic 
    # subsequence in the substring s[i...j] using at most 'ops' operations.
    # We use a 3D array for clarity, though space could be optimized.
    dp = [[[0] * (k + 1) for _ in range(n)] for _ in range(n)]

    # Base case: single characters are palindromes of length 1
    for i in range(n):
        for ops in range(k + 1):
            dp[i][i][ops] = 1

    # Fill the DP table for substrings of length 2 up to n
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            
            for ops in range(k + 1):
                # Option 1: Characters at i and j match
                if s[i] == s[j]:
                    # If they match, we don't use any operations
                    # If length is 2, the result is 2, otherwise 2 + inner LPS
                    inner_val = dp[i + 1][j - 1][ops] if i + 1 <= j - 1 else 0
                    dp[i][j][ops] = 2 + inner_val
                else:
                    # Option 2: Characters at i and j do not match
                    # Sub-option A: Don't use an operation to force them to match
                    # We take the max of excluding either the left or right character
                    res = max(dp[i + 1][j][ops], dp[i][j - 1][ops])
                    
                    # Sub-option B: Use 1 operation to make s[i] == s[j]
                    # This is only possible if we have at least 1 operation left
                    if ops > 0:
                        inner_val = dp[i + 1][j - 1][ops - 1] if i + 1 <= j - 1 else 0
                        res = max(res, 2 + inner_val)
                    
                    dp[i][j][ops] = res

    # The answer is the LPS of the full string using at most k operations
    return dp[0][n - 1][k]
