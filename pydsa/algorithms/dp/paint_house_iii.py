METADATA = {
    "id": 1473,
    "name": "Paint House III",
    "slug": "paint-house-iii",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dynamic_programming", "dp"],
    "difficulty": "hard",
    "time_complexity": "O(n * m^2)",
    "space_complexity": "O(n * m * k)",
    "description": "Find the minimum cost to paint houses such that they form exactly 'm' contiguous neighborhoods of colors.",
}

def solve(houses: list[list[int]], m: int) -> int:
    """
    Calculates the minimum cost to paint houses such that there are exactly m neighborhoods.

    Args:
        houses: A 2D list where houses[i][j] is the cost to paint house i with color j+1.
        m: The target number of contiguous neighborhoods.

    Returns:
        The minimum cost to achieve exactly m neighborhoods, or -1 if impossible.

    Examples:
        >>> solve([[1,1,1],[1,1,1],[1,1,1]], 3)
        3
        >>> solve([[1,2,3],[1,2,3],[1,2,3]], 3)
        3
    """
    n = len(houses)
    k = len(houses[0])
    inf = float('inf')

    # dp[i][j][c] represents the minimum cost to paint houses up to index i,
    # with exactly j neighborhoods, and the i-th house having color c.
    # Dimensions: [n][m + 1][k]
    dp = [[[inf] * k for _ in range(m + 1)] for _ in range(n)]

    # Base case: First house
    for color in range(k):
        dp[0][1][color] = houses[0][color]

    # Fill DP table
    for i in range(1, n):
        for j in range(1, m + 1):
            for curr_color in range(k):
                cost = houses[i][curr_color]
                
                # Option 1: Current house has the same color as the previous house
                # This does not increase the number of neighborhoods.
                if dp[i-1][j][curr_color] != inf:
                    dp[i][j][curr_color] = min(dp[i][j][curr_color], dp[i-1][j][curr_color] + cost)
                
                # Option 2: Current house has a different color than the previous house
                # This increases the number of neighborhoods by 1.
                if j > 1:
                    for prev_color in range(k):
                        if prev_color == curr_color:
                            continue
                        if dp[i-1][j-1][prev_color] != inf:
                            dp[i][j][curr_color] = min(dp[i][j][curr_color], dp[i-1][j-1][prev_color] + cost)

    # The answer is the minimum cost among all possible colors for the last house with m neighborhoods
    ans = min(dp[n-1][m])
    
    return int(ans) if ans != inf else -1
