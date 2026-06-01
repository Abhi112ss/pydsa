METADATA = {
    "id": 2291,
    "name": "Maximum Profit From Trading Stocks",
    "slug": "maximum-profit-from-trading-stocks",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dp", "greedy", "array"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Calculate the maximum profit possible by trading stocks given price changes and transaction constraints.",
}

def solve(prices: list[int], transaction_fee: int) -> int:
    """
    Calculates the maximum profit from trading stocks with a transaction fee.

    Args:
        prices: A list of integers representing the stock price on each day.
        transaction_fee: An integer representing the fee incurred for each completed transaction.

    Returns:
        The maximum profit achievable.

    Examples:
        >>> solve([1, 3, 2, 8, 4, 9], 2)
        8
        >>> solve([1, 3, 7, 5, 10, 3], 3)
        4
    """
    if not prices:
        return 0

    # hold represents the maximum profit we can have if we currently own a stock.
    # We initialize it to -prices[0] because we "bought" the stock on day 0.
    hold = -prices[0]
    
    # cash represents the maximum profit we can have if we do not currently own a stock.
    # We initialize it to 0 because we start with no stock and no profit.
    cash = 0

    for i in range(1, len(prices)):
        # Update cash: Either we stay in cash, or we sell the stock we were holding.
        # Selling incurs the transaction fee.
        cash = max(cash, hold + prices[i] - transaction_fee)
        
        # Update hold: Either we keep holding the stock, or we buy a new stock using our cash.
        hold = max(hold, cash - prices[i])

    # The maximum profit will always be in the 'cash' state (not holding any stock).
    return cash
