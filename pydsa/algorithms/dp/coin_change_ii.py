METADATA = {
    "id": 518,
    "name": "Coin Change II",
    "slug": "coin-change-ii",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dynamic_programming", "knapsack", "integer_break"],
    "difficulty": "medium",
    "time_complexity": "O(n * amount)",
    "space_complexity": "O(amount)",
    "description": "Find the number of combinations that make up a given amount using a given set of coins.",
}

def solve(coins: list[int], amount: int) -> int:
    """
    Calculates the total number of ways to make up the given amount using the provided coins.
    This is an implementation of the Unbounded Knapsack problem (specifically, the 
    counting combinations variation).

    Args:
        coins: A list of integers representing the denominations of the coins.
        amount: The target total amount.

    Returns:
        The total number of unique combinations that sum up to the amount.

    Examples:
        >>> solve([1, 2, 5], 5)
        4
        >>> solve([2], 3)
        0
    """
    # dp[i] will store the number of ways to make the amount 'i'
    # We initialize with size amount + 1
    dp = [0] * (amount + 1)

    # Base case: There is exactly one way to make the amount 0 (by choosing no coins)
    dp[0] = 1

    # To ensure we count combinations (order doesn't matter) rather than permutations,
    # we iterate through each coin first, then update the dp table.
    for coin in coins:
        # For each coin, we update all possible amounts from 'coin' up to 'amount'
        for current_amount in range(coin, amount + 1):
            # The number of ways to reach 'current_amount' is increased by 
            # the number of ways we could reach 'current_amount - coin'
            dp[current_amount] += dp[current_amount - coin]

    return dp[amount]
