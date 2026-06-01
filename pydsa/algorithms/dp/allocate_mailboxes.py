METADATA = {
    "id": 1478,
    "name": "Allocate Mailboxes",
    "slug": "allocate-mailboxes",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dynamic_programming", "dp", "greedy"],
    "difficulty": "hard",
    "time_complexity": "O(n^3)",
    "space_complexity": "O(n^2)",
    "description": "Find the minimum number of mailboxes needed to cover all houses given a fixed number of mailboxes.",
}

def solve(houses: list[int], k: int) -> int:
    """
    Calculates the minimum number of mailboxes required to cover all houses.

    The problem is solved by first precomputing the cost (distance) to cover 
    any contiguous range of houses [i, j] with a single mailbox. The optimal 
    position for a single mailbox for a range of houses is the median of their positions.
    Then, we use dynamic programming to partition the houses into k groups.

    Args:
        houses: A list of integers representing the positions of houses.
        k: The number of mailboxes available.

    Returns:
        The minimum total distance to cover all houses.

    Examples:
        >>> solve([1, 4, 8, 10], 2)
        9
        >>> solve([1, 1, 1, 1], 1)
        0
    """
    n = len(houses)
    # Sort houses to ensure contiguous ranges represent spatial clusters
    houses.sort()

    # cost[i][j] will store the minimum distance to cover houses from index i to j with 1 mailbox
    cost = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(i, n):
            # The optimal position for one mailbox for houses[i...j] is the median
            median_idx = (i + j) // 2
            median_pos = houses[median_idx]
            dist_sum = 0
            for idx in range(i, j + 1):
                dist_sum += abs(houses[idx] - median_pos)
            cost[i][j] = dist_sum

    # dp[m][i] is the minimum distance to cover first i houses using m mailboxes
    # Initialize with a large value (infinity)
    dp = [[float('inf')] * (n + 1) for _ in range(k + 1)]
    
    # Base case: 0 houses covered with any number of mailboxes costs 0
    for m in range(k + 1):
        dp[m][0] = 0

    # Fill DP table
    for m in range(1, k + 1):
        for i in range(1, n + 1):
            # Try all possible split points 'j' to place the m-th mailbox
            # The m-th mailbox covers houses from index j to i-1
            for j in range(i):
                # dp[m-1][j] is cost of covering first j houses with m-1 mailboxes
                # cost[j][i-1] is cost of covering remaining houses with 1 mailbox
                dp[m][i] = min(dp[m][i], dp[m - 1][j] + cost[j][i - 1])

    return int(dp[k][n])
