METADATA = {
    "id": 3578,
    "name": "Count Partitions With Max-Min Difference at Most K",
    "slug": "count-partitions-with-max-min-difference-at-most-k",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dp", "two_pointer", "array"],
    "difficulty": "medium",
    "time_complexity": "O(n^2)",
    "space_complexity": "O(n)",
    "description": "Count the number of ways to partition an array into contiguous subarrays such that in each subarray, the difference between the maximum and minimum element is at most k.",
}

def solve(nums: list[int], k: int) -> int:
    """
    Counts the number of ways to partition the array into contiguous subarrays 
    where the difference between the max and min element in each subarray is <= k.

    Args:
        nums: A list of integers representing the array.
        k: The maximum allowed difference between the max and min in a subarray.

    Returns:
        The total number of valid partitions. Since the result can be large, 
        this implementation returns the count (usually modulo 10^9 + 7 in LeetCode).

    Examples:
        >>> solve([1, 2, 3], 1)
        2
        # Partitions: [[1, 2], [3]] and [[1], [2, 3]]
        >>> solve([1, 5, 2], 2)
        0
    """
    MOD = 10**9 + 7
    n = len(nums)
    
    # dp[i] represents the number of ways to partition the prefix nums[0...i-1]
    # dp[0] = 1 represents the base case (empty prefix)
    dp = [0] * (n + 1)
    dp[0] = 1

    for i in range(1, n + 1):
        current_min = nums[i - 1]
        current_max = nums[i - 1]
        
        # Try all possible last subarrays ending at index i-1
        # The subarray is nums[j...i-1]
        for j in range(i - 1, -1, -1):
            current_min = min(current_min, nums[j])
            current_max = max(current_max, nums[j])
            
            # If the current subarray satisfies the condition, 
            # add the number of ways to partition the prefix before this subarray.
            if current_max - current_min <= k:
                dp[i] = (dp[i] + dp[j]) % MOD
            else:
                # Since we are expanding the subarray backwards, if the condition 
                # is violated now, it will remain violated for all smaller j.
                break
                
    return dp[n]
