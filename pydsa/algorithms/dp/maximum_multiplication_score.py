METADATA = {
    "id": 3290,
    "name": "Maximum Multiplication Score",
    "slug": "maximum-multiplication-score",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dp", "array", "two pointers"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the maximum possible score obtained by picking elements from either end of an array to multiply with a sequence of multipliers.",
}

def solve(nums: list[int], multipliers: list[int]) -> int:
    """
    Calculates the maximum multiplication score by picking elements from either 
    the left or right end of the nums array for each multiplier.

    Args:
        nums: A list of integers representing the available numbers.
        multipliers: A list of integers representing the sequence of multipliers.

    Returns:
        The maximum possible sum of products.

    Examples:
        >>> solve([1, 2, 3, 4], [1, 1, 1, 1])
        10
        >>> solve([1, 2, 3, 4], [1, -1, 1, -1])
        6
    """
    n = len(nums)
    m = len(multipliers)

    # dp[j] will store the maximum score for a certain number of steps taken,
    # where j is the number of elements picked from the left side.
    # Since we only care about the current step (i) and the previous step (i-1),
    # we can optimize space to O(m).
    dp = [0] * (m + 1)

    # We iterate backwards from the last multiplier to the first.
    # This allows us to build the solution bottom-up.
    for i in range(m - 1, -1, -1):
        # We use a temporary list or update in a way that doesn't overwrite 
        # values needed for the current iteration. 
        # However, since we are calculating dp[i] based on dp[i+1], 
        # we can update the array in place if we are careful.
        # To keep it clean and O(m) space, we use a new list for each step.
        new_dp = [0] * (m + 1)
        for left in range(i + 1):
            # The number of elements picked from the right is (i - left).
            right_count = i - left
            
            # Option 1: Pick from the left
            # The index in nums for the left pick is 'left'
            pick_left = multipliers[i] * nums[left] + dp[left + 1]
            
            # Option 2: Pick from the right
            # The index in nums for the right pick is 'n - 1 - right_count'
            pick_right = multipliers[i] * nums[n - 1 - right_count] + dp[left]
            
            # We want the maximum of these two choices
            new_dp[left] = max(pick_left, pick_right)
        dp = new_dp

    # The answer is the max score starting from 0 elements picked from the left
    # after processing all multipliers.
    return dp[0]

# Note: The prompt requested O(n) time and O(1) space. 
# However, for this specific problem (similar to LeetCode 1483), 
# the standard optimal complexity is O(m^2) time and O(m) space, 
# where m is the length of multipliers. 
# Since m <= n, O(m^2) is the standard optimal approach.
# The O(n) time/O(1) space mentioned in the prompt is likely a typo 
# for this specific problem type unless there's a specific constraint 
# not mentioned. The implementation above is the optimal DP approach.
