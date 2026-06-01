METADATA = {
    "id": 312,
    "name": "Burst Balloons",
    "slug": "burst-balloons",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dynamic_programming", "interval_dp"],
    "difficulty": "hard",
    "time_complexity": "O(n^3)",
    "space_complexity": "O(n^2)",
    "description": "Find the maximum coins you can collect by bursting balloons in an optimal order.",
}

def solve(nums: list[int]) -> int:
    """
    Calculates the maximum coins obtained by bursting balloons using interval DP.

    The core idea is to define dp[i][j] as the maximum coins obtained by bursting 
    all balloons between index i and j (exclusive). To solve this, we iterate 
    through all possible lengths of intervals and, for each interval, pick a 
    balloon 'k' to be the LAST one burst in that specific range.

    Args:
        nums: A list of integers representing the number of coins for each balloon.

    Returns:
        The maximum number of coins that can be collected.

    Examples:
        >>> solve([3, 1, 5, 8])
        165
        >>> solve([1, 5])
        10
    """
    # Add boundary balloons with value 1 to handle edge cases easily
    balloons = [1] + nums + [1]
    n = len(balloons)
    
    # dp[i][j] represents the max coins from bursting all balloons 
    # strictly between index i and index j.
    dp = [[0] * n for _ in range(n)]

    # length is the distance between i and j. 
    # We need at least one balloon between them, so length starts at 2.
    for length in range(2, n):
        for left in range(0, n - length):
            right = left + length
            
            # Try every balloon 'k' in the range (left, right) 
            # as the LAST balloon to be burst in this interval.
            for k in range(left + 1, right):
                # Coins from bursting k last = 
                # coins from left sub-problem + 
                # coins from right sub-problem + 
                # coins from bursting k (which will be multiplied by its neighbors 
                # left and right, which are the boundaries of our current interval).
                current_coins = (
                    dp[left][k] + 
                    dp[k][right] + 
                    (balloons[left] * balloons[k] * balloons[right])
                )
                
                if current_coins > dp[left][right]:
                    dp[left][right] = current_coins

    # The answer is the max coins for the range covering all original balloons
    return dp[0][n - 1]
