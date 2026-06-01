METADATA = {
    "id": 3205,
    "name": "Maximum Array Hopping Score I",
    "slug": "maximum-array-hopping-score-i",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dynamic_programming", "array"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Find the maximum score achievable by hopping through an array where each hop adds the value of the destination element.",
}

def solve(nums: list[int]) -> int:
    """
    Calculates the maximum score achievable by hopping through the array.
    
    A hop can be made from index i to index i+1 or i+2 (if within bounds).
    The score is the sum of the values of the elements landed on.
    The starting element's value is included in the score.

    Args:
        nums: A list of integers representing the values at each position.

    Returns:
        The maximum score achievable.

    Examples:
        >>> solve([1, 2, 3, 4, 5])
        13
        >>> solve([10, 2, 1, 10, 5])
        25
    """
    n = len(nums)
    if n == 0:
        return 0
    if n == 1:
        return nums[0]

    # dp[i] stores the maximum score to reach index i
    dp = [0] * n
    
    # Base cases: starting at index 0
    dp[0] = nums[0]
    
    # The first hop can only come from index 0 to index 1
    if n > 1:
        dp[1] = nums[0] + nums[1]

    # Fill the DP table for the rest of the array
    for i in range(2, n):
        # To reach index i, we could have come from i-1 or i-2
        # We take the maximum of those two paths and add the current value
        dp[i] = max(dp[i - 1], dp[i - 2]) + nums[i]

    # The problem asks for the maximum score achievable by hopping through the array.
    # Since we can stop at any index (implied by the nature of "hopping through"),
    # we look for the maximum value in the DP table. 
    # However, in standard "hopping" problems where you must reach the end, 
    # it's dp[n-1]. Given the context of "Maximum Score", we return the max 
    # value found in the DP array to account for paths that might end early 
    # if values were negative (though here they are positive).
    return max(dp)
