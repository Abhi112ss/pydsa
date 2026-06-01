METADATA = {
    "id": 322,
    "name": "Coin Change",
    "slug": "coin-change",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dynamic_programming", "breadth_first_search", "greedy"],
    "difficulty": "medium",
    "time_complexity": "O(amount * len(coins))",
    "space_complexity": "O(amount)",
    "description": "Find the fewest number of coins needed to make up a given amount.",
}

def solve(coins: list[int], amount: int) -> int:
    """
    Calculates the minimum number of coins needed to reach the target amount.

    Args:
        coins: A list of integers representing the denominations available.
        amount: The target total amount.

    Returns:
        The minimum number of coins required to make up the amount. 
        Returns -1 if that amount cannot be made up by any combination of the coins.

    Examples:
        >>> solve([1, 2, 5], 11)
        3
        >>> solve([2], 3)
        -1
        >>> solve([1], 0)
        0
    """
    # If amount is 0, no coins are needed.
    if amount == 0:
        return 0

    # Initialize DP array with a value larger than any possible number of coins.
    # amount + 1 is a safe upper bound because the smallest coin is 1.
    max_val = amount + 1
    dp = [max_val] * (amount + 1)
    
    # Base case: 0 coins are needed to make amount 0.
    dp[0] = 0

    # Iterate through every amount from 1 to the target amount.
    for current_amount in range(1, amount + 1):
        for coin in coins:
            # Check if the coin can be part of the solution for the current amount.
            if coin <= current_amount:
                # The recurrence relation: 
                # min coins for current_amount is the minimum of its current value
                # or 1 (the current coin) + the min coins needed for (current_amount - coin).
                dp[current_amount] = min(dp[current_amount], dp[current_amount - coin] + 1)

    # If dp[amount] is still the initial max_val, the amount is unreachable.
    return dp[amount] if dp[amount] != max_val else -1
