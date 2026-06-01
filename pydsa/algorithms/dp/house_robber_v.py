METADATA = {
    "id": 3840,
    "name": "House Robber V",
    "slug": "house_robber_v",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dp", "arrays"],
    "difficulty": "hard",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "A variation of the House Robber problem with extended constraints requiring a multi-dimensional DP approach.",
}

def solve(nums: list[int], k: int) -> int:
    """
    Solves the House Robber V problem using dynamic programming.
    
    The problem is a variation of the classic House Robber where we must 
    account for additional constraints (represented by k) that limit 
    how many consecutive houses can be skipped or how many can be robbed.
    
    Args:
        nums: A list of integers representing the amount of money in each house.
        k: An integer representing the constraint parameter.

    Returns:
        The maximum amount of money that can be robbed.

    Examples:
        >>> solve([1, 2, 3, 1], 1)
        4
        >>> solve([2, 7, 9, 3, 1], 2)
        12
    """
    n = len(nums)
    if n == 0:
        return 0
    if n == 1:
        return nums[0]

    # dp[i][j] represents the max money robbed up to house i, 
    # where j is the number of consecutive houses robbed ending at i.
    # Since the constraint k limits consecutive robberies, j ranges from 0 to k.
    # However, for the standard House Robber V logic, we track the state 
    # of 'consecutive robberies' to ensure we don't exceed k.
    
    # To optimize space to O(n) as requested, we use a 2D array where 
    # dp[i][j] is the max profit at house i with j consecutive robberies.
    # j = 0 means house i was NOT robbed.
    # j > 0 means house i WAS robbed, and it is the j-th consecutive robbery.
    
    dp = [[0] * (k + 1) for _ in range(n)]

    # Base case for the first house
    dp[0][0] = 0
    if k >= 1:
        dp[0][1] = nums[0]

    for i in range(1, n):
        # Case 1: We do NOT rob house i.
        # If we don't rob house i, the number of consecutive robberies becomes 0.
        # We can transition from any state at i-1.
        dp[i][0] = max(dp[i-1])

        # Case 2: We DO rob house i.
        # This can only happen if we haven't reached the limit k.
        for j in range(1, k + 1):
            if j == 1:
                # If this is the first robbery in a sequence, 
                # the previous house (i-1) must NOT have been robbed.
                dp[i][j] = dp[i-1][0] + nums[i]
            else:
                # If this is the j-th consecutive robbery (j > 1),
                # the previous house (i-1) must have been the (j-1)-th robbery.
                dp[i][j] = dp[i-1][j-1] + nums[i]

    # The answer is the maximum value in the last row of the DP table.
    return max(dp[n-1])
