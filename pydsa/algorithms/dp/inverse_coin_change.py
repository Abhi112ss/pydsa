METADATA = {
    "id": 3592,
    "name": "Inverse Coin Change",
    "slug": "inverse_coin_change",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dp", "math", "backtracking"],
    "difficulty": "medium",
    "time_complexity": "O(target * len(coins))",
    "space_complexity": "O(target)",
    "description": "Given a target sum and a set of coin denominations, find a subset of coins that could have produced the target sum using the standard coin change DP approach.",
}

from typing import Optional


def solve(target: int, coins: list[int]) -> Optional[list[int]]:
    """
    Finds a subset of coins that sums up to the target value.
    
    This is an inverse problem where we reconstruct the path taken by a 
    standard dynamic programming coin change algorithm.

    Args:
        target: The target sum to reach.
        coins: A list of available coin denominations.

    Returns:
        A list of coins that sum up to the target, or None if no such combination exists.

    Examples:
        >>> solve(11, [1, 2, 5])
        [5, 5, 1]
        >>> solve(3, [2])
        None
    """
    # dp[i] stores whether it is possible to reach sum i
    # We use a boolean array to represent reachability
    dp = [False] * (target + 1)
    dp[0] = True

    # parent[i] stores the coin used to reach sum i to allow reconstruction
    parent = [-1] * (target + 1)

    # Standard Unbounded Knapsack / Coin Change DP approach
    for coin in coins:
        for current_sum in range(coin, target + 1):
            # If the previous state was reachable and current state isn't yet
            if dp[current_sum - coin] and not dp[current_sum]:
                dp[current_sum] = True
                parent[current_sum] = coin

    # If the target is not reachable, return None
    if not dp[target]:
        return None

    # Reconstruct the path from target back to 0 using the parent pointers
    result_coins = []
    current_remaining = target
    while current_remaining > 0:
        coin_used = parent[current_remaining]
        if coin_used == -1:
            # This case should theoretically not be reached if dp[target] is True
            return None
        result_coins.append(coin_used)
        current_remaining -= coin_used

    return result_coins
