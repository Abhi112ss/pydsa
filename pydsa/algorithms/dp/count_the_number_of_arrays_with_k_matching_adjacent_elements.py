METADATA = {
    "id": 3405,
    "name": "Count the Number of Arrays with K Matching Adjacent Elements",
    "slug": "count-the-number-of-arrays-with-k-matching-adjacent-elements",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dynamic_programming", "combinatorics", "counting"],
    "difficulty": "medium",
    "time_complexity": "O(n * k)",
    "space_complexity": "O(n * k)",
    "description": "Count the number of arrays of length n with elements from 1 to m such that exactly k adjacent elements are equal.",
}

def solve(n: int, m: int, k: int) -> int:
    """
    Calculates the number of arrays of length n with elements in range [1, m]
    where exactly k pairs of adjacent elements are equal.

    Args:
        n: The length of the array.
        m: The range of values available for each element (1 to m).
        k: The exact number of matching adjacent elements required.

    Returns:
        The number of such arrays modulo 10^9 + 7.

    Examples:
        >>> solve(3, 2, 1)
        4
        # Arrays: [1, 1, 2], [1, 2, 2], [2, 2, 1], [2, 1, 1]
    """
    MOD = 10**9 + 7

    if n == 0:
        return 1 if k == 0 else 0
    if k >= n:
        return 0

    # dp[i][j] represents the number of arrays of length i with exactly j matches.
    # i ranges from 1 to n, j ranges from 0 to k.
    dp = [[0] * (k + 1) for _ in range(n + 1)]

    # Base case: array of length 1 has 0 matches.
    # There are m ways to choose the first element.
    dp[1][0] = m

    for i in range(1, n):
        for j in range(k + 1):
            if dp[i][j] == 0:
                continue
            
            # Option 1: The next element (i+1) is the same as the current element (i).
            # This increases the match count by 1.
            if j + 1 <= k:
                dp[i + 1][j + 1] = (dp[i + 1][j + 1] + dp[i][j]) % MOD
            
            # Option 2: The next element (i+1) is different from the current element (i).
            # There are (m - 1) choices for a different element.
            # This does not increase the match count.
            dp[i + 1][j] = (dp[i + 1][j] + dp[i][j] * (m - 1)) % MOD

    return dp[n][k]
