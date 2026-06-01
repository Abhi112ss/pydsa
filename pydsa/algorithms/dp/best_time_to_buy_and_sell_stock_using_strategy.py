METADATA = {
    "id": 3652,
    "name": "Best Time to Buy and Sell Stock using Strategy",
    "slug": "best-time-to-buy-and-sell-stock-using-strategy",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dp", "greedy", "stock"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the maximum profit possible by buying and selling a stock given an array of daily prices.",
}

def solve(prices: list[int]) -> int:
    """
    Calculates the maximum profit achievable from buying and selling a stock.
    
    This implementation uses a state-based dynamic programming approach (greedy)
    to track the maximum profit possible when currently holding a stock versus
    not holding a stock.

    Args:
        prices: A list of integers representing the stock price on each day.

    Returns:
        The maximum profit that can be obtained.

    Examples:
        >>> solve([7, 1, 5, 3, 6, 4])
        5
        >>> solve([7, 6, 4, 3, 1])
        0
    """
    if not prices:
        return 0

    # hold represents the maximum profit we have if we currently own a stock.
    # We initialize it to -prices[0] because we "bought" the stock on day 0.
    hold = -prices[0]
    
    # free represents the maximum profit we have if we do not own a stock.
    # We initialize it to 0 because we start with no profit and no stock.
    free = 0

    for i in range(1, len(prices)):
        current_price = prices[i]
        
        # To calculate the new 'free' state (not holding stock):
        # Either we were already free, or we just sold the stock we were holding.
        new_free = max(free, hold + current_price)
        
        # To calculate the new 'hold' state (holding stock):
        # Either we were already holding, or we just bought the stock using our 'free' profit.
        new_hold = max(hold, free - current_price)
        
        free = new_free
        hold = new_hold

    # The maximum profit will always be in the 'free' state (not holding any stock at the end).
    return free
