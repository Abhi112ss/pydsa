METADATA = {
    "id": 1262,
    "name": "Greatest Sum Divisible by Three",
    "slug": "greatest-sum-divisible-by-three",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dynamic_programming", "math", "greedy"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the maximum sum of elements in an array such that the sum is divisible by three.",
}

def solve(nums: list[int]) -> int:
    """
    Finds the maximum sum of elements in the input list that is divisible by three.

    The algorithm uses dynamic programming to maintain the maximum sum achieved 
    for each possible remainder when divided by 3 (0, 1, and 2).

    Args:
        nums: A list of positive integers.

    Returns:
        The largest sum of a subset of nums that is divisible by 3.

    Examples:
        >>> solve([3, 6, 5, 1, 8])
        18
        >>> solve([3, 6, 5, 1, 8, 2])
        18
        >>> solve([1, 2, 3, 4, 5, 6, 7, 8])
        36
    """
    # dp[i] stores the maximum sum found so far that has a remainder of i when divided by 3.
    # Initialize with 0 for remainder 0, and negative infinity for others to represent unreachable states.
    dp = [0, float('-inf'), float('-inf')]

    for num in nums:
        # We create a copy of the current dp state to calculate the next state.
        # This prevents using the same number multiple times within the same iteration.
        current_dp = dp[:]
        
        for current_sum in dp:
            # If the current_sum is valid (not -inf), calculate the new sum and its remainder.
            if current_sum != float('-inf'):
                new_sum = current_sum + num
                remainder = new_sum % 3
                
                # Update the dp table if the new sum is greater than the existing sum for that remainder.
                if new_sum > current_dp[remainder]:
                    current_dp[remainder] = new_sum
        
        dp = current_dp

    # The answer is the maximum sum with remainder 0.
    return int(dp[0])
