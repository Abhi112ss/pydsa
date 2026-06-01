METADATA = {
    "id": 122,
    "name": "Best Time to Buy and Sell Stock II",
    "slug": "best-time-to-buy-and-sell-stock-ii",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["greedy", "dynamic_programming"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the maximum profit you can achieve by making as many transactions as you like.",
}

def solve(prices: list[int]) -> int:
    """
    Calculates the maximum profit possible from multiple stock transactions.

    The algorithm uses a greedy approach: whenever the price of the stock 
    increases from one day to the next, we capture that profit. This is 
    mathematically equivalent to holding the stock through all upward 
    slopes of the price graph.

    Args:
        prices: A list of integers representing the stock price on each day.

    Returns:
        The maximum total profit achievable.

    Examples:
        >>> solve([7, 1, 5, 3, 6, 4])
        7
        >>> solve([1, 2, 3, 4, 5])
        4
        >>> solve([7, 6, 4, 3, 1])
        0
    """
    max_profit = 0
    
    # Iterate through the prices starting from the second day
    for current_day in range(1, len(prices)):
        # If the price today is higher than yesterday, we "buy" yesterday 
        # and "sell" today to capture the immediate profit.
        price_difference = prices[current_day] - prices[current_day - 1]
        
        if price_difference > 0:
            # Accumulate all positive price increments.
            # This captures every upward trend in the price sequence.
            max_profit += price_difference
            
    return max_profit
