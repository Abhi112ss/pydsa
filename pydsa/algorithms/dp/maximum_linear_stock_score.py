METADATA = {
    "id": 2898,
    "name": "Maximum Linear Stock Score",
    "slug": "maximum-linear-stock-score",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dp", "arrays"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Calculate the maximum score achievable by selecting elements in a linear sequence based on specific transition rules.",
}

def solve(prices: list[int], costs: list[int]) -> int:
    """
    Args:
        prices: A list of integers representing the price of stock at each time step.
        costs: A list of integers representing the cost to hold or trade stock.

    Returns:
        The maximum possible score achievable.
    """
    n = len(prices)
    if n == 0:
        return 0

    dp = [0] * n
    dp[0] = prices[0] - costs[0]

    for i in range(1, n):
        option_stay = dp[i - 1] + prices[i] - costs[i]
        option_reset = prices[i] - costs[i]
        dp[i] = max(option_stay, option_reset)

    return max(dp) if dp else 0