METADATA = {
    "id": 474,
    "name": "Ones and Zeroes",
    "slug": "ones-and-zeroes",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dynamic_programming", "knapsack", "two-dimensional-knapsack"],
    "difficulty": "medium",
    "time_complexity": "O(len(strs) * m * n)",
    "space_complexity": "O(m * n)",
    "description": "Find the maximum number of strings in an array that can be formed using a limited number of zeros and ones.",
}

def solve(strs: list[str], m: int, n: int) -> int:
    """
    Finds the maximum number of strings that can be formed given limits on zeros and ones.

    This is a variation of the 0/1 Knapsack problem extended to two dimensions.
    Each string is an item with two weights: the count of '0's and the count of '1's.

    Args:
        strs: A list of binary strings.
        m: The maximum number of '0's allowed.
        n: The maximum number of '1's allowed.

    Returns:
        The maximum number of strings that can be formed.

    Examples:
        >>> solve(["10", "0001", "111001", "1", "0"], 5, 3)
        4
        >>> solve(["10", "0", "1"], 1, 1)
        2
    """
    # dp[i][j] represents the maximum number of strings we can form 
    # using at most i zeros and j ones.
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for s in strs:
        # Count zeros and ones in the current string
        zeros_count = s.count('0')
        ones_count = s.count('1')

        # Iterate backwards through the DP table to ensure each string 
        # is used at most once (standard 0/1 knapsack optimization).
        # We stop when the remaining capacity is less than the current string's requirements.
        for i in range(m, zeros_count - 1, -1):
            for j in range(n, ones_count - 1, -1):
                # Transition: either we don't take the current string, 
                # or we take it and add 1 to the result of the remaining capacity.
                dp[i][j] = max(dp[i][j], dp[i - zeros_count][j - ones_count] + 1)

    return dp[m][n]
