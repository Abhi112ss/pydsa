METADATA = {
    "id": 1682,
    "name": "Longest Palindromic Subsequence II",
    "slug": "longest-palindromic-subsequence-ii",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dynamic_programming", "string"],
    "difficulty": "hard",
    "time_complexity": "O(n^2)",
    "space_complexity": "O(n^2)",
    "description": "Find the maximum length of a palindromic subsequence after removing at most two characters from the string.",
}

def solve(s: str, k: int) -> int:
    """
    Args:
        s: The input string.
        k: The maximum number of characters that can be removed.

    Returns:
        The length of the longest palindromic subsequence after removing at most k characters.
    """
    n = len(s)
    memo = {}

    def get_lps(left: int, right: int, removals_left: int) -> int:
        if left > right:
            return 0
        if left == right:
            return 1
        
        state = (left, right, removals_left)
        if state in memo:
            return memo[state]

        if s[left] == s[right]:
            result = 2 + get_lps(left + 1, right - 1, removals_left)
        else:
            result = 0
            if removals_left > 0:
                result = max(
                    get_lps(left + 1, right, removals_left - 1),
                    get_lps(left, right - 1, removals_left - 1)
                )
            
            result = max(
                result,
                get_lps(left + 1, right, removals_left),
                get_lps(left, right - 1, removals_left)
            )
            
            if removals_left > 0:
                result = max(
                    result,
                    get_lps(left + 1, right, removals_left - 1),
                    get_lps(left, right - 1, removals_left - 1)
                )

        memo[state] = result
        return result

    dp = [[0] * n for _ in range(n)]

    for i in range(n - 1, -1, -1):
        dp[i][i] = 1
        for j in range(i + 1, n):
            if s[i] == s[j]:
                dp[i][j] = dp[i + 1][j - 1] + 2
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

    def solve_with_removals(left: int, right: int, k_rem: int) -> int:
        if left > right:
            return 0
        if left == right:
            return 1
        
        state = (left, right, k_rem)
        if state in memo:
            return memo[state]
        
        if s[left] == s[right]:
            res = 2 + solve_with_removals(left + 1, right - 1, k_rem)
        else:
            res = 0
            if k_rem > 0:
                res = max(solve_with_removals(left + 1, right, k_rem - 1),
                          solve_with_removals(left, right - 1, k_rem - 1))
            
            res = max(res, solve_with_removals(left + 1, right, k_rem),
                          solve_with_removals(left, right - 1, k_rem))
            
        memo[state] = res
        return res

    memo = {}
    
    def compute(i: int, j: int, rem: int) -> int:
        if i > j:
            return 0
        if i == j:
            return 1
        if (i, j, rem) in memo:
            return memo[(i, j, rem)]
        
        if s[i] == s[j]:
            res = 2 + compute(i + 1, j - 1, rem)
        else:
            res = compute(i + 1, j, rem)
            res = max(res, compute(i, j - 1, rem))
            if rem > 0:
                res = max(res, compute(i + 1, j, rem - 1))
                res = max(res, compute(i, j - 1, rem - 1))
        
        memo[(i, j, rem)] = res
        return res

    return compute(0, n - 1, k)