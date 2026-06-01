METADATA = {
    "id": 3510,
    "name": "Minimum Pair Removal to Sort Array II",
    "slug": "minimum-pair-removal-to-sort-array-ii",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dynamic_programming", "greedy", "array"],
    "difficulty": "hard",
    "time_complexity": "O(n^2)",
    "space_complexity": "O(n^2)",
    "description": "Find the minimum number of pair removals required to make the remaining elements of an array non-decreasing.",
}

def solve(nums: list[int]) -> int:
    """
    Calculates the minimum number of pair removals to make the array non-decreasing.
    
    A pair removal consists of picking two indices (i, j) and removing them.
    The goal is to find the maximum number of elements we can keep such that 
    they form a non-decreasing subsequence and the number of removed elements 
    is even (since we remove in pairs).

    Args:
        nums: A list of integers.

    Returns:
        The minimum number of elements to remove.

    Examples:
        >>> solve([1, 3, 2, 4])
        2
        >>> solve([1, 2, 3])
        1 (Wait, if we must remove in pairs, we must remove 0 or 2 elements. 
           If the remaining must be non-decreasing, and we remove 2, 1 remains.
           Actually, the problem implies we remove pairs until the rest is sorted.)
    """
    n = len(nums)
    if n == 0:
        return 0

    # dp[i][j] represents the maximum length of a non-decreasing subsequence 
    # that can be formed using elements from the subarray nums[i...j].
    # However, the constraint is that we remove elements in pairs.
    # This means the number of elements removed (n - length_of_subsequence) must be even.
    # Therefore, (n - length_of_subsequence) % 2 == 0.
    
    # Let's redefine: dp[i][j] is the maximum length of a non-decreasing subsequence
    # using a subset of elements from index i to j, such that the number of 
    # elements REMOVED from this range is even.
    
    # Standard LIS approach is O(n log n), but here we have the "pair removal" 
    # constraint which links the parity of the removed elements to the total count.
    
    # Let's use a simpler DP: dp[i][j] = max length of non-decreasing subsequence 
    # in range [i, j].
    # To satisfy the "pair removal" rule:
    # Total removed = n - length_of_subsequence.
    # We need (n - length_of_subsequence) % 2 == 0.
    
    # First, find the Longest Non-Decreasing Subsequence (LNDS).
    # But wait, the problem is "Minimum Pair Removal". 
    # If we remove k pairs, we remove 2k elements.
    # Remaining elements = n - 2k.
    # These remaining elements must be non-decreasing.
    
    # So we need to find the largest k such that there exists a non-decreasing 
    # subsequence of length (n - 2k).
    
    # Let L be the length of the longest non-decreasing subsequence.
    # We want to find the largest length 'len' such that:
    # 1. len <= L
    # 2. (n - len) % 2 == 0
    
    # Step 1: Find the length of the Longest Non-Decreasing Subsequence.
    # We use the O(n log n) tails approach.
    import bisect
    
    tails = []
    for x in nums:
        # bisect_right for non-decreasing (allows duplicates)
        idx = bisect.bisect_right(tails, x)
        if idx < len(tails):
            tails[idx] = x
        else:
            tails.append(x)
    
    max_lnds = len(tails)
    
    # Step 2: Find the largest 'len' <= max_lnds where (n - len) % 2 == 0.
    # If (n - max_lnds) is even, then max_lnds is our target length.
    # If (n - max_lnds) is odd, we must reduce the length by 1 to make the 
    # number of removed elements even.
    
    if (n - max_lnds) % 2 == 0:
        target_len = max_lnds
    else:
        target_len = max_lnds - 1
        
    # The number of elements removed is n - target_len.
    # Since we remove in pairs, the number of pairs is (n - target_len) // 2.
    # The question asks for "Minimum Pair Removal", which usually means 
    # the number of pairs.
    
    return (n - target_len) // 2
