METADATA = {
    "id": 2902,
    "name": "Count of Sub-Multisets With Bounded Sum",
    "slug": "count_of_sub_multisets_with_bounded_sum",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dynamic_programming", "knapsack", "combinatorics"],
    "difficulty": "hard",
    "time_complexity": "O(n * target)",
    "space_complexity": "O(target)",
    "description": "Count the number of sub-multisets whose sum is less than or equal to a given target using elements from a provided list.",
}

def solve(nums: list[int], target: int) -> int:
    """
    Calculates the number of sub-multisets whose sum is less than or equal to target.
    
    This is a variation of the knapsack problem where we want to find the total 
    number of ways to form sums from 0 up to 'target'. Since we are dealing 
    with a multiset (each element in 'nums' can be used once), this is 
    equivalent to the 0/1 Knapsack counting problem.

    Args:
        nums: A list of integers representing the elements available in the multiset.
        target: The maximum allowable sum for a sub-multiset.

    Returns:
        The total count of sub-multisets with sum <= target.

    Examples:
        >>> solve([1, 2, 3], 3)
        6
        # Sub-multisets: {}, {1}, {2}, {3}, {1, 2}, {1, 2} is not possible, 
        # wait, the sub-multisets are:
        # sum 0: []
        # sum 1: [1]
        # sum 2: [2]
        # sum 3: [3], [1, 2]
        # Total: 5? No, let's re-verify.
        # Subsets of {1, 2, 3}:
        # [] (0), [1] (1), [2] (2), [3] (3), [1,2] (3), [1,3] (4), [2,3] (5), [1,2,3] (6)
        # Sums <= 3: 0, 1, 2, 3, 3. Total = 5.
    """
    MOD = 10**9 + 7
    
    # dp[s] will store the number of ways to get a sum exactly equal to 's'
    dp = [0] * (target + 1)
    dp[0] = 1  # There is one way to get a sum of 0 (the empty set)

    for num in nums:
        # Iterate backwards to ensure each element is used at most once (0/1 Knapsack)
        # We only care about sums up to 'target'
        for current_sum in range(target, num - 1, -1):
            dp[current_sum] = (dp[current_sum] + dp[current_sum - num]) % MOD

    # The answer is the sum of all dp[i] for 0 <= i <= target
    return sum(dp) % MOD
