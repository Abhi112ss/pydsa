METADATA = {
    "id": 188,
    "name": "Best Time to Buy and Sell Stock IV",
    "slug": "best-time-to-buy-and-sell-stock-iv",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dynamic_programming", "array"],
    "difficulty": "hard",
    "time_complexity": "O(k * n)",
    "space_complexity": "O(k * n)",
    "description": "Find the maximum profit you can achieve by making at most k transactions.",
}

def solve(k: int, prices: list[int]) -> int:
    """
    Args:
        k: The maximum number of transactions allowed.
        prices: A list of stock prices where prices[i] is the price on day i.

    Returns:
        The maximum profit achievable with at most k transactions.
    """
    n = len(prices)
    if n == 0 or k == 0:
        return 0

    if k >= n // 2:
        max_profit = 0
        for i in range(1, n):
            if prices[i] > prices[i - 1]:
                max_profit += prices[i] - prices[i - 1]
        return max_profit

    dp = [[0] * n for _ in range(k + 1)]

    for t in range(1, k + 1):
        max_diff = -prices[0]
        for d in range(1, n):
            dp[t][d] = max(dp[t][d - 1], prices[d] + max_diff)
            max_diff = max(max_diff, dp[t - 1][d] - prices[d])

    return dp[k][n - 1]