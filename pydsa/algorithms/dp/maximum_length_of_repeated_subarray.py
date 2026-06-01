METADATA = {
    "id": 718,
    "name": "Maximum Length of Repeated Subarray",
    "slug": "maximum-length-of-repeated-subarray",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dynamic_programming", "sliding_window", "array"],
    "difficulty": "medium",
    "time_complexity": "O(m*n)",
    "space_complexity": "O(m*n)",
    "description": "Find the maximum length of a subarray that appears in both given arrays.",
}

def solve(nums1: list[int], nums2: list[int]) -> int:
    """
    Finds the maximum length of a subarray that appears in both nums1 and nums2.

    This problem is equivalent to finding the Longest Common Substring of two arrays.
    We use dynamic programming where dp[i][j] stores the length of the longest 
    common suffix of the prefixes nums1[0...i-1] and nums2[0...j-1].

    Args:
        nums1: The first list of integers.
        nums2: The second list of integers.

    Returns:
        The length of the longest repeated subarray.

    Examples:
        >>> solve([1, 2, 3, 2, 1], [3, 2, 1, 4, 7])
        3
        >>> solve([1, 2, 3, 4], [5, 6, 7, 8])
        0
    """
    m = len(nums1)
    n = len(nums2)
    
    # dp[i][j] will store the length of the longest common subarray 
    # ending at nums1[i-1] and nums2[j-1].
    # We use (m+1) x (n+1) to handle the base case of empty prefixes.
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    max_length = 0

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            # If elements match, extend the length of the common subarray 
            # found at the previous indices.
            if nums1[i - 1] == nums2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                # Update the global maximum length found so far.
                if dp[i][j] > max_length:
                    max_length = dp[i][j]
            else:
                # If elements don't match, the common subarray ending here is 0.
                dp[i][j] = 0
                
    return max_length
