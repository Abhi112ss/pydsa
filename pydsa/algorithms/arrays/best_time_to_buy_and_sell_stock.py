METADATA = {
    "id": 121,
    "name": "Best Time to Buy and Sell Stock",
    "slug": "best-time-to-buy-and-sell-stock",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["array", "dynamic_programming", "greedy"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the maximum profit you can achieve by choosing a single day to buy one stock and a different day in the future to sell it.",
}

def solve(prices: list[int]) -> int:
    """
    Calculates the maximum profit possible from a single buy-sell transaction.

    Args:
        prices: A list of integers representing the stock price on each day.

    Returns:
        The maximum profit achievable. Returns 0 if no profit can be made.

    Examples:
        >>> solve([7, 1, 5, 3, 6, 4])
        5
        >>> solve([7, 6, 4, 3, 1])
        0
    """
    if not prices:
        return 0

    min_price_so_far = float('inf')
    max_profit = 0

    for current_price in prices:
        # Update the minimum price encountered so far to ensure we buy at the lowest possible point
        if current_price < min_price_so_far:
            min_price_so_far = current_price
        
        # Calculate potential profit if we sold at the current price
        current_profit = current_price - min_price_so_far
        
        # Update the global maximum profit if the current transaction is better
        if current_profit > max_profit:
            max_profit = current_profit

    return int(max_profit)
