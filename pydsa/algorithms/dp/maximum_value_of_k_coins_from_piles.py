METADATA = {
    "id": 2218,
    "name": "Maximum Value of K Coins From Piles",
    "slug": "maximum-value-of-k-coins-from-piles",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dp", "greedy", "knapsack"],
    "difficulty": "medium",
    "time_complexity": "O(n * k * m) where m is max pile size, effectively O(k * sum(pile_lengths))",
    "space_complexity": "O(k)",
    "description": "Find the maximum value of k coins chosen from the tops of several piles.",
}

def solve(piles: list[list[int]], k: int) -> int:
    """
    Calculates the maximum value of k coins that can be taken from the tops of piles.
    
    This is a variation of the Multiple Choice Knapsack Problem. For each pile, 
    we can choose to take 0, 1, 2, ..., or all coins from that pile.
    
    Args:
        piles: A list of lists where each sub-list represents a pile of coins.
        k: The total number of coins to be picked.
        
    Returns:
        The maximum sum of k coins.
        
    Examples:
        >>> solve([[1, 15, 7, 2, 2], [10, 10, 1, 0, 0], [7, 1, 1, 1, 1]], 7)
        54
        >>> solve([[1, 2, 3], [2, 1]], 3)
        6
    """
    # dp[i] stores the maximum value obtained by picking exactly i coins
    # We use a 1D array to optimize space from O(n*k) to O(k)
    dp = [0] * (k + 1)

    for pile in piles:
        # Precompute prefix sums for the current pile to quickly get 
        # the value of taking 'j' coins from this pile.
        # current_pile_sums[j] = sum of first j coins in the pile.
        current_pile_sums = [0]
        running_sum = 0
        for coin in pile:
            running_sum += coin
            current_pile_sums.append(running_sum)
        
        # Iterate backwards through dp to ensure each pile is used at most once
        # (standard 0/1 knapsack optimization for space).
        for current_k in range(k, -1, -1):
            # Try taking 'take' number of coins from the current pile
            # 'take' can range from 1 up to the size of the pile or the remaining k
            for take in range(1, len(current_pile_sums)):
                if current_k >= take:
                    # Update dp[current_k] by comparing its current value 
                    # with the value of taking 'take' coins from this pile 
                    # plus the best value of (current_k - take) coins from previous piles.
                    dp[current_k] = max(dp[current_k], dp[current_k - take] + current_pile_sums[take])
                else:
                    # If we can't even take 'take' coins, we can't take more than that
                    break
                    
    return dp[k]
