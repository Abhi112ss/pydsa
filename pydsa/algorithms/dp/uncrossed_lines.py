METADATA = {
    "id": 1035,
    "name": "Uncrossed Lines",
    "slug": "uncrossed-lines",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dynamic_programming", "array", "sequence"],
    "difficulty": "medium",
    "time_complexity": "O(n * m)",
    "space_complexity": "O(n * m)",
    "description": "Find the maximum number of non-crossing lines that can be drawn between two arrays of integers.",
}

def solve(nums1: list[int], nums2: list[int]) -> int:
    """
    Calculates the maximum number of non-crossing lines between two arrays.
    
    The problem is equivalent to finding the Longest Common Subsequence (LCS) 
    between nums1 and nums2. A line can be drawn between nums1[i] and nums2[j] 
    if nums1[i] == nums2[j], and the non-crossing constraint ensures we are 
    looking for a subsequence of matches.

    Args:
        nums1: The first list of integers.
        nums2: The second list of integers.

    Returns:
        The maximum number of non-crossing lines.

    Examples:
        >>> solve([1, 3, 5, 3], [1, 3, 5, 1])
        3
        >>> solve([1, 2, 3], [2, 1, 3])
        2
    """
    n = len(nums1)
    m = len(nums2)

    # Initialize a 2D DP table where dp[i][j] represents the LCS 
    # of nums1[0...i-1] and nums2[0...j-1].
    # We use (n+1) x (m+1) to handle the base case of empty sequences.
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            # If the elements match, we can draw a line.
            # This increases the count from the previous subproblem (i-1, j-1).
            if nums1[i - 1] == nums2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                # If they don't match, the best we can do is the maximum 
                # obtained by skipping an element from either nums1 or nums2.
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[n][m]
