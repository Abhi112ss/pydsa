METADATA = {
    "id": 714,
    "name": "Best Time to Buy and Sell Stock with Transaction Fee",
    "slug": "best-time-to-buy-and-sell-stock-with-transaction-fee",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dynamic_programming", "greedy", "stock"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the maximum profit you can achieve by buying and selling stocks with a fixed transaction fee per completed trade.",
}

def solve(prices: list[int], fee: int) -> int:
    """
    Calculates the maximum profit achievable from stock trading with a transaction fee.

    The algorithm uses dynamic programming with two states:
    1. 'hold': The maximum profit if we currently own a share of stock.
    2. 'free': The maximum profit if we currently do not own any stock.

    Args:
        prices: A list of integers representing the stock price on each day.
        fee: An integer representing the transaction fee incurred for each completed trade.

    Returns:
        The maximum total profit possible.

    Examples:
        >>> solve([1, 3, 2, 8, 4, 9], 2)
        8
        >>> solve([1, 3, 2, 8, 4, 9], 3)
        5
    """
    if not prices:
        return 0

    # 'free' represents the max profit if we don't hold a stock at the end of the day.
    # Initially, we have 0 profit and no stock.
    free = 0
    
    # 'hold' represents the max profit if we hold a stock at the end of the day.
    # Initially, we "buy" the stock on day 0, so profit is -prices[0].
    hold = -prices[0]

    for i in range(1, len(prices)):
        # Update 'free' state:
        # Either we stay free (keep previous free profit), 
        # or we sell the stock we were holding (hold + current price - fee).
        new_free = max(free, hold + prices[i] - fee)
        
        # Update 'hold' state:
        # Either we keep holding the stock (keep previous hold profit),
        # or we buy the stock today using the profit we had when we were free.
        new_hold = max(hold, free - prices[i])
        
        free = new_free
        hold = new_hold

    # The maximum profit will always be in the 'free' state (not holding stock).
    return free
