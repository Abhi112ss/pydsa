METADATA = {
    "id": 1940,
    "name": "Longest Common Subsequence Between Sorted Arrays",
    "slug": "longest_common_subsequence_between_sorted_arrays",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dp", "arrays", "sequence"],
    "difficulty": "medium",
    "time_complexity": "O(n * m)",
    "space_complexity": "O(n * m)",
    "description": "Find the length of the longest common subsequence between two sorted arrays.",
}

def solve(array_a: list[int], array_b: list[int]) -> int:
    """
    Calculates the length of the longest common subsequence (LCS) between two sorted arrays.

    Args:
        array_a: The first sorted list of integers.
        array_b: The second sorted list of integers.

    Returns:
        The length of the longest common subsequence.

    Examples:
        >>> solve([1, 2, 3], [2, 3, 4])
        2
        >>> solve([1, 5, 10], [1, 10])
        2
        >>> solve([1, 2, 3], [4, 5, 6])
        0
    """
    n = len(array_a)
    m = len(array_b)

    # Initialize a 2D DP table where dp[i][j] represents the LCS length
    # of the prefixes array_a[0...i-1] and array_b[0...j-1].
    # Using (n + 1) x (m + 1) to handle the base case of empty sequences.
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            # If elements match, increment the LCS length from the previous prefixes
            if array_a[i - 1] == array_b[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                # If they don't match, take the maximum possible LCS by skipping 
                # one element from either array_a or array_b.
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[n][m]
