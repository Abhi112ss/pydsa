METADATA = {
    "id": 2952,
    "name": "Minimum Number of Coins to be Added",
    "slug": "minimum-number-of-coins-to-be-added",
    "category": "Greedy",
    "aliases": [],
    "tags": ["greedy", "math"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the minimum number of coins to add to a set to ensure any value up to a target can be formed.",
}

def solve(coins: list[int], target: int) -> int:
    """
    Calculates the minimum number of coins to add to a given set of coins 
    to be able to represent every integer value from 1 to target.

    The algorithm uses a greedy approach. We maintain the current maximum 
    reachable value 'max_reachable'. If the next available coin is greater 
    than 'max_reachable + 1', we must add coins to bridge the gap.

    Args:
        coins: A list of existing coin denominations.
        target: The maximum value we want to be able to represent.

    Returns:
        The minimum number of coins that need to be added.

    Examples:
        >>> solve([1, 2, 5], 10)
        1
        >>> solve([1, 1, 1], 10)
        3
        >>> solve([1, 2, 4, 8], 15)
        0
    """
    # Sort coins to process them in increasing order
    coins.sort()
    
    max_reachable = 0
    added_count = 0
    coin_idx = 0
    n = len(coins)

    # We need to be able to reach 'target'
    while max_reachable < target:
        # Check if the next available coin can extend our range without leaving a gap
        if coin_idx < n and coins[coin_idx] <= max_reachable + 1:
            # Use the existing coin to extend the range
            max_reachable += coins[coin_idx]
            coin_idx += 1
        else:
            # There is a gap between max_reachable and the next coin (or no coins left)
            # To bridge the gap greedily, we add a coin equal to (max_reachable + 1)
            # This is the most efficient way to increase the reachable range.
            max_reachable += (max_reachable + 1)
            added_count += 1
            
    return added_count
