METADATA = {
    "id": 3429,
    "name": "Paint House IV",
    "slug": "paint-house-iv",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dp", "dynamic_programming"],
    "difficulty": "hard",
    "time_complexity": "O(n * k)",
    "space_complexity": "O(k)",
    "description": "Find the maximum total score by painting houses with colors such that no two adjacent houses have the same color.",
}

def solve(colors: list[list[int]], k: int) -> int:
    """
    Calculates the maximum total score for painting houses with k colors.

    Args:
        colors: A list of lists where colors[i][j] is the score for painting 
                house i with color j.
        k: The number of available colors.

    Returns:
        The maximum possible total score.

    Examples:
        >>> solve([[1, 2, 3], [3, 2, 1]], 3)
        6
        >>> solve([[1, 1, 1], [1, 1, 1]], 3)
        2
    """
    if not colors:
        return 0

    # dp[j] stores the maximum score ending at the current house with color j.
    # We only need the previous house's results, so we use O(k) space.
    dp = [0] * k

    # Initialize dp with the first house's scores.
    for j in range(k):
        dp[j] = colors[0][j]

    for i in range(1, len(colors)):
        # To optimize the transition, we don't iterate through all previous colors for every current color.
        # Instead, we find the top two maximum scores from the previous house.
        # This allows us to pick the best color for the current house in O(1) after O(k) preprocessing.
        
        max1_val, max1_idx = -1, -1
        max2_val, max2_idx = -1, -1

        for idx in range(k):
            if dp[idx] > max1_val:
                max2_val = max1_val
                max2_idx = max1_idx
                max1_val = dp[idx]
                max1_idx = idx
            elif dp[idx] > max2_val:
                max2_val = dp[idx]
                max2_idx = idx

        new_dp = [0] * k
        for j in range(k):
            # If the current color j is the same as the best color from the previous house,
            # we must use the second best color to satisfy the adjacency constraint.
            if j == max1_idx:
                new_dp[j] = colors[i][j] + max2_val
            else:
                new_dp[j] = colors[i][j] + max1_val
        
        dp = new_dp

    return max(dp)
