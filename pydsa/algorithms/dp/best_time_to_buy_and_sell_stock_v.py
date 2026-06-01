METADATA = {
    "id": 3573,
    "name": "Best Time to Buy and Sell Stock V",
    "slug": "best-time-to-buy-and-sell-stock-v",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dp", "arrays", "greedy"],
    "difficulty": "hard",
    "time_complexity": "O(n * k)",
    "space_complexity": "O(n * k)",
    "description": "Find the maximum profit from trading stocks with at most k transactions and a one-day cooldown period after selling.",
}

def solve(prices: list[int], k: int) -> int:
    """
    Calculates the maximum profit from trading stocks with at most k transactions
    and a one-day cooldown period after each sale.

    Args:
        prices: A list of integers representing the stock price on each day.
        k: The maximum number of transactions allowed.

    Returns:
        The maximum profit achievable.

    Examples:
        >>> solve([1, 2, 3, 0, 2], 2)
        3
        >>> solve([1, 2, 4, 1, 5], 1)
        4
    """
    if not prices or k == 0:
        return 0

    n = len(prices)
    
    # If k is very large, the problem effectively becomes "unlimited transactions with cooldown"
    # However, to maintain the O(n*k) requirement and handle the specific k constraint,
    # we use a 3D DP table or a structured 2D DP table.
    # dp[i][j][state] where:
    # i: day index
    # j: number of transactions completed
    # state: 0 -> Available to buy (not holding, not in cooldown)
    #        1 -> Holding stock
    #        2 -> In cooldown (just sold)

    # To optimize space from O(n*k) to O(k), we only need the previous day's states.
    # But per requirements, we implement the standard O(n*k) approach.
    
    # dp[day][transactions_remaining][state]
    # Using a dictionary or a 3D array. Given n and k can be large, 
    # we use a 2D array where each element is a list/tuple of 3 states to save overhead.
    
    # dp[i][j] = [max_profit_available, max_profit_holding, max_profit_cooldown]
    # j is number of transactions *started*
    dp = [[[-float('inf')] * 3 for _ in range(k + 1)] for _ in range(n)]

    # Base case: Day 0
    # State 0: Not holding, 0 transactions
    dp[0][0][0] = 0
    # State 1: Holding, 1st transaction started
    if k > 0:
        dp[0][1][1] = -prices[0]

    for i in range(1, n):
        for j in range(k + 1):
            # State 0: Available to buy
            # Can come from:
            # 1. Being available yesterday (dp[i-1][j][0])
            # 2. Coming out of cooldown yesterday (dp[i-1][j][2])
            dp[i][j][0] = max(dp[i-1][j][0], dp[i-1][j][2])

            if j > 0:
                # State 1: Holding stock
                # Can come from:
                # 1. Holding stock yesterday (dp[i-1][j][1])
                # 2. Buying stock today (must have been in state 0 yesterday)
                #    Note: Buying starts a transaction, so we look at dp[i-1][j-1][0]
                #    Wait, if we use j as "transactions completed", logic shifts.
                #    Let's use j as "transactions initiated".
                dp[i][j][1] = max(dp[i-1][j][1], dp[i-1][j-1][0] - prices[i])

                # State 2: Cooldown (Just sold)
                # Can come from:
                # 1. Selling stock today (must have been holding yesterday)
                dp[i][j][2] = dp[i-1][j][1] + prices[i]

    # The answer is the max of being in state 0 or state 2 (not holding) 
    # across all possible transaction counts at the last day.
    max_profit = 0
    for j in range(k + 1):
        max_profit = max(max_profit, dp[n-1][j][0], dp[n-1][j][2])
        
    return int(max_profit)
