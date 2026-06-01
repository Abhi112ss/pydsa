METADATA = {
    "id": 416,
    "name": "Partition Equal Subset Sum",
    "slug": "partition_equal_subset_sum",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dynamic_programming", "knapsack", "subset_sum"],
    "difficulty": "medium",
    "time_complexity": "O(n * target)",
    "space_complexity": "O(target)",
    "description": "Determine if a given non-empty array can be partitioned into two subsets such that the sum of elements in both subsets is equal.",
}

def solve(nums: list[int]) -> bool:
    """
    Determines if the input array can be partitioned into two subsets with equal sums.

    This is a variation of the 0/1 Knapsack problem. If the total sum is odd, 
    it's impossible to split it into two equal integer sums. If even, we 
    look for a subset that sums exactly to total_sum / 2.

    Args:
        nums: A list of positive integers.

    Returns:
        True if a partition exists, False otherwise.

    Examples:
        >>> solve([1, 5, 11, 5])
        True
        >>> solve([1, 2, 3, 5])
        False
    """
    total_sum = sum(nums)

    # If the total sum is odd, we cannot split it into two equal integer subsets
    if total_sum % 2 != 0:
        return False

    target = total_sum // 2
    
    # dp[i] will be True if a subset sum of i is possible
    # We use a 1D array to optimize space from O(n * target) to O(target)
    dp = [False] * (target + 1)
    dp[0] = True

    for num in nums:
        # Iterate backwards to ensure each number is used at most once (0/1 Knapsack)
        # If we iterated forwards, we would be solving the Unbounded Knapsack problem
        for current_sum in range(target, num - 1, -1):
            if dp[current_sum - num]:
                dp[current_sum] = True
        
        # Early exit if we already found a way to reach the target
        if dp[target]:
            return True

    return dp[target]
