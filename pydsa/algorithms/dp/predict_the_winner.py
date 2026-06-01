METADATA = {
    "id": 486,
    "name": "Predict the Winner",
    "slug": "predict-the-winner",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dynamic_programming", "recursion", "minimax", "array"],
    "difficulty": "medium",
    "time_complexity": "O(n^2)",
    "space_complexity": "O(n^2)",
    "description": "Determine if the first player can win a game where players take turns picking numbers from either end of an array.",
}

def solve(nums: list[int]) -> bool:
    """
    Determines if the first player can win the game given the array of numbers.
    
    The game follows minimax logic: each player plays optimally to maximize 
    their own score relative to the opponent. We use dynamic programming to 
    calculate the maximum relative score difference (Player1_score - Player2_score) 
    possible for any subarray [i, j].

    Args:
        nums: A list of integers representing the numbers available in the game.

    Returns:
        True if the first player can win (or tie), False otherwise.

    Examples:
        >>> solve([1, 5, 2])
        True
        >>> solve([1, 5, 2, 10])
        False
    """
    n = len(nums)
    if n == 0:
        return True

    # dp[i][j] represents the maximum relative score difference 
    # (current player's score minus opponent's score) for the subarray nums[i...j].
    dp = [[0.0] * n for _ in range(n)]

    # Base case: when there is only one number, the player takes it.
    for i in range(n):
        dp[i][i] = float(nums[i])

    # Build the DP table for subarrays of length 2 up to n.
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            
            # The current player chooses either the left end (nums[i]) or the right end (nums[j]).
            # After choosing, the opponent will play optimally on the remaining subarray,
            # so we subtract the opponent's optimal relative score from our choice.
            pick_left = nums[i] - dp[i + 1][j]
            pick_right = nums[j] - dp[i][j - 1]
            
            dp[i][j] = max(pick_left, pick_right)

    # If the maximum relative score difference for the full array is non-negative,
    # the first player wins or ties.
    return dp[0][n - 1] >= 0
