METADATA = {
    "id": 2915,
    "name": "Length of the Longest Subsequence That Sums to Target",
    "slug": "length-of-the-longest-subsequence-that-sums-to-target",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dynamic_programming", "knapsack"],
    "difficulty": "medium",
    "time_complexity": "O(n * target)",
    "space_complexity": "O(target)",
    "description": "Find the maximum length of a subsequence of a given array that sums up to a specific target value.",
}

def solve(nums: list[int], target: int) -> int:
    """
    Finds the maximum length of a subsequence that sums up to the target.

    This is a variation of the 0/1 Knapsack problem where the 'value' 
    of each item is 1 (representing its count) and the 'weight' is the 
    number itself. We want to maximize the total value for a fixed weight.

    Args:
        nums: A list of positive integers.
        target: The target sum to achieve.

    Returns:
        The maximum length of a subsequence that sums to target. 
        Returns -1 if no such subsequence exists.

    Examples:
        >>> solve([1, 2, 3, 4, 5], 10)
        4
        >>> solve([1, 1, 1], 2)
        2
        >>> solve([1, 2, 3], 7)
        -1
    """
    # Initialize DP array where dp[i] is the max length to reach sum i.
    # We use -1 to represent that a sum is currently unreachable.
    # Using target + 1 to accommodate the 0-th index.
    dp = [-1] * (target + 1)
    
    # Base case: A sum of 0 is achieved with a subsequence of length 0.
    dp[0] = 0

    for num in nums:
        # Iterate backwards through the DP array to ensure each number 
        # from 'nums' is used at most once (0/1 Knapsack property).
        # We stop at 'num' because we cannot form a sum smaller than the number itself.
        for current_sum in range(target, num - 1, -1):
            # If the previous state (current_sum - num) was reachable
            if dp[current_sum - num] != -1:
                # Update the current sum with the maximum length found so far
                dp[current_sum] = max(dp[current_sum], dp[current_sum - num] + 1)

    return dp[target]
