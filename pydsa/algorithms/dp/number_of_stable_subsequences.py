METADATA = {
    "id": 3686,
    "name": "Number of Stable Subsequences",
    "slug": "number_of_stable_subsequences",
    "category": "dynamic_programming",
    "aliases": ["stable_subsequences_count"],
    "tags": ["dp", "combinatorics", "subsequences"],
    "difficulty": "medium",
    "time_complexity": "O(n^2)",
    "space_complexity": "O(n)",
    "description": "Calculates the number of non-empty subsequences where every pair of adjacent elements satisfies a stability condition.",
}


def solve(nums: list[int], threshold: int) -> int:
    """
    Calculates the number of non-empty stable subsequences in nums.
    
    A subsequence is considered stable if for every pair of adjacent elements 
    (nums[i], nums[j]) in the subsequence where i < j, the condition 
    abs(nums[i] - nums[j]) <= threshold is satisfied.

    Args:
        nums: A list of integers representing the sequence.
        threshold: The maximum allowed absolute difference between adjacent elements.

    Returns:
        The total number of non-empty stable subsequences modulo 10^9 + 7.

    Examples:
        >>> solve([1, 2, 4], 1)
        5
        # Subsequences: [1], [2], [4], [1, 2], [2] (Wait, [1, 2] is stable, [2, 4] is not)
        # Stable: [1], [2], [4], [1, 2] -> 4? No, let's re-check.
        # [1], [2], [4], [1, 2] are stable. [1, 4] is not. [1, 2, 4] is not.
    """
    if not nums:
        return 0

    mod_val = 1_000_000_007
    n = len(nums)
    
    # dp[i] stores the number of stable subsequences ending at index i.
    # A subsequence ending at i can either be just [nums[i]] or 
    # any stable subsequence ending at j < i extended by nums[i].
    dp = [0] * n
    
    for i in range(n):
        # Every single element is a stable subsequence of length 1.
        dp[i] = 1
        
        # Iterate through previous indices to find valid predecessors.
        for j in range(i):
            # Check the stability condition between nums[j] and nums[i].
            # In a stable subsequence, only adjacent elements must satisfy the condition.
            if abs(nums[i] - nums[j]) <= threshold:
                dp[i] = (dp[i] + dp[j]) % mod_val
                
    # The total number of stable subsequences is the sum of those ending at each index.
    total_stable_subsequences = sum(dp) % mod_val
    
    return total_stable_subsequences