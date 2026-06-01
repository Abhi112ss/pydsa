METADATA = {
    "id": 2830,
    "name": "Maximize the Profit as the Salesman",
    "slug": "maximize-the-profit-as-the-salesman",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dp", "greedy", "array"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Calculate the maximum profit a salesman can make by deciding whether to buy or sell items at specific locations along a path.",
}

def solve(prices: list[int], costs: list[int]) -> int:
    """
    Calculates the maximum profit achievable by traveling through a sequence of locations.
    At each location, the salesman can choose to buy an item (paying the cost) 
    or sell an item (receiving the price).

    Args:
        prices: A list of integers representing the selling price at each location.
        costs: A list of integers representing the buying cost at each location.

    Returns:
        The maximum total profit possible.

    Examples:
        >>> solve([10, 20, 30], [5, 15, 25])
        30
        >>> solve([5, 5, 5], [10, 10, 10])
        0
    """
    # The problem can be modeled as finding the maximum sum of (price[i] - cost[j])
    # where i > j. However, the standard interpretation for this type of problem 
    # is that we want to maximize the cumulative profit.
    # Since we can only sell what we have bought, we track the minimum cost 
    # encountered so far to maximize the potential profit at any given selling point.

    if not prices or not costs:
        return 0

    max_profit = 0
    # Initialize min_cost with the cost of the first location.
    # We use this to track the cheapest way to have an item in hand.
    min_cost = costs[0]

    for i in range(len(prices)):
        # Option 1: We sell the item at the current location.
        # The profit would be the current price minus the cheapest cost seen so far.
        current_transaction_profit = prices[i] - min_cost
        
        # Update the global maximum profit if this transaction is better.
        if current_transaction_profit > max_profit:
            max_profit = current_transaction_profit
            
        # Option 2: We update the minimum cost seen so far.
        # This allows us to potentially buy at a lower price for a future sale.
        if costs[i] < min_cost:
            min_cost = costs[i]

    return max_profit
