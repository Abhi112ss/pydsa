METADATA = {
    "id": 377,
    "name": "Combination Sum IV",
    "slug": "combination-sum-iv",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dynamic_programming", "math"],
    "difficulty": "medium",
    "time_complexity": "O(n * target)",
    "space_complexity": "O(target)",
    "description": "Find the number of possible combinations that add up to a target value using elements from a given array, where order matters.",
}

def solve(nums: list[int], target: int) -> int:
    """
    Calculates the number of combinations that sum up to the target value.
    
    This problem is a variation of the unbounded knapsack problem where the 
    order of elements matters (permutations). We use dynamic programming 
    to build up the number of ways to reach every value from 0 to target.

    Args:
        nums: A list of positive integers.
        target: The target sum to reach.

    Returns:
        The total number of combinations that sum up to the target.

    Examples:
        >>> solve([1, 2, 3], 4)
        7
        >>> solve([1], 1)
        1
    """
    # dp[i] will store the number of ways to reach sum 'i'
    # We initialize with size target + 1
    dp = [0] * (target + 1)
    
    # Base case: There is exactly one way to reach sum 0 (by choosing nothing)
    dp[0] = 1
    
    # Iterate through every possible sum from 1 to target
    for current_sum in range(1, target + 1):
        # For each sum, try subtracting every number in the input array
        for num in nums:
            # If the number is less than or equal to the current sum,
            # it means we can form 'current_sum' by adding 'num' to 
            # a previous combination that summed to 'current_sum - num'
            if current_sum >= num:
                dp[current_sum] += dp[current_sum - num]
                
    return dp[target]
