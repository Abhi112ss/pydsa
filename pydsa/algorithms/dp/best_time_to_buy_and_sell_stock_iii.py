METADATA = {
    "id": 123,
    "name": "Best Time to Buy and Sell Stock III",
    "slug": "best-time-to-buy-and-sell-stock-iii",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["array", "dynamic programming", "stock"],
    "difficulty": "hard",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the maximum profit you can achieve by completing at most two transactions.",
}

def solve(prices: list[int]) -> int:
    """
    Calculates the maximum profit from at most two stock transactions.

    Args:
        prices: A list of integers representing the stock price on each day.

    Returns:
        The maximum profit achievable.

    Examples:
        >>> solve([3, 3, 5, 0, 0, 3, 1, 4])
        6
        >>> solve([1, 2, 3, 4, 5])
        4
        >>> solve([7, 6, 4, 3, 1])
        0
    """
    if not prices:
        return 0

    # Initialize states:
    # buy1: Max money remaining after the first purchase (negative because it's a cost)
    # sell1: Max profit after the first sale
    # buy2: Max money remaining after the second purchase
    # sell2: Max profit after the second sale
    buy1 = float('-inf')
    sell1 = 0
    buy2 = float('-inf')
    sell2 = 0

    for price in prices:
        # 1. Update first buy: maximize remaining cash after buying at current price
        buy1 = max(buy1, -price)
        
        # 2. Update first sell: maximize profit after selling at current price
        sell1 = max(sell1, buy1 + price)
        
        # 3. Update second buy: maximize remaining cash after buying using profit from first sale
        buy2 = max(buy2, sell1 - price)
        
        # 4. Update second sell: maximize total profit after second sale
        sell2 = max(sell2, buy2 + price)

    return int(sell2)
