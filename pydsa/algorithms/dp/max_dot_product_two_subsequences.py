METADATA = {
    "id": 1458,
    "name": "Max Dot Product of Two Subsequences",
    "slug": "max-dot-product-of-two-subsequences",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dynamic_programming", "array"],
    "difficulty": "hard",
    "time_complexity": "O(n * m)",
    "space_complexity": "O(n * m)",
    "description": "Find the maximum dot product of two non-empty subsequences of two given arrays.",
}

def solve(nums1: list[int], nums2: list[int]) -> int:
    """
    Calculates the maximum dot product of two non-empty subsequences.

    Args:
        nums1: The first list of integers.
        nums2: The second list of integers.

    Returns:
        The maximum dot product possible between any two non-empty subsequences.

    Examples:
        >>> solve([2, 1, -2, 5], [-3, 2, 4])
        18
        >>> solve([-1, -1], [1, 1])
        -1
    """
    n = len(nums1)
    m = len(nums2)

    # dp[i][j] represents the maximum dot product using prefixes nums1[:i] and nums2[:j]
    # We initialize with a very small number to handle negative products.
    dp = [[float('-inf')] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            # Current product of the elements at the current indices
            current_product = nums1[i - 1] * nums2[j - 1]
            
            # Option 1: Start a new subsequence with just the current pair
            # Option 2: Add current pair to the best subsequence found in previous prefixes
            # Option 3: Skip current element from nums1 (dp[i-1][j])
            # Option 4: Skip current element from nums2 (dp[i][j-1])
            
            # We use max(0, dp[i-1][j-1]) because if the previous max dot product 
            # was negative, it's better to just start fresh with the current product.
            dp[i][j] = max(
                current_product,
                current_product + dp[i - 1][j - 1],
                dp[i - 1][j],
                dp[i][j - 1]
            )

    return int(dp[n][m])
