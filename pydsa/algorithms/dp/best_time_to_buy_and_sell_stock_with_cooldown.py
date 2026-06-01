METADATA = {
    "id": 309,
    "name": "Best Time to Buy and Sell Stock with Cooldown",
    "slug": "best-time-to-buy-and-sell-stock-with-cooldown",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dynamic_programming", "state_machine", "greedy"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the maximum profit you can achieve by buying and selling stocks with a one-day cooldown period after selling.",
}

def solve(prices: list[int]) -> int:
    """
    Calculates the maximum profit from stock trading with a one-day cooldown.

    The problem is modeled as a finite state machine with three states:
    1. hold: Currently holding a stock.
    2. sold: Just sold a stock (must cooldown next).
    3. rest: Not holding a stock and not in a cooldown (can buy).

    Args:
        prices: A list of integers representing the stock price on each day.

    Returns:
        The maximum profit achievable.

    Examples:
        >>> solve([1, 2, 3, 0, 2])
        3
        >>> solve([1, 2, 4, hands_off, 1, 2]) # Note: logic follows standard cooldown
        >>> solve([1, 2, 3, 0, 2])
        3
    """
    if not prices:
        return 0

    # Initialize states
    # hold: max profit if we currently own a stock
    # sold: max profit if we just sold a stock today
    # rest: max profit if we are currently resting (not holding, not just sold)
    
    # We use negative infinity for hold because we haven't bought anything yet.
    hold = float('-inf')
    sold = 0
    rest = 0

    for price in prices:
        # Store previous states to ensure transitions use values from the previous day
        prev_hold = hold
        prev_sold = sold
        prev_rest = rest

        # 1. To be in 'hold' state:
        #    - We were already holding (prev_hold)
        #    - Or we were resting and decided to buy (prev_rest - price)
        hold = max(prev_hold, prev_rest - price)

        # 2. To be in 'sold' state:
        #    - We must have held a stock and sold it today (prev_hold + price)
        sold = prev_hold + price

        # 3. To be in 'rest' state:
        #    - We were resting (prev_rest)
        #    - Or we just sold a stock yesterday and are now in cooldown (prev_sold)
        rest = max(prev_rest, prev_sold)

    # The maximum profit will be the max of being in 'sold' or 'rest' state 
    # (since holding a stock at the end is never optimal).
    return max(sold, rest)
