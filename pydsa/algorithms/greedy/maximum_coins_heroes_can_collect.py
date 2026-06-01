METADATA = {
    "id": 2838,
    "name": "Maximum Coins Heroes Can Collect",
    "slug": "maximum-coins-heroes-can-collect",
    "category": "Greedy",
    "aliases": [],
    "tags": ["greedy", "sorting"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(1)",
    "description": "Maximize the total coins collected by matching heroes with coins such that each hero's strength is at least the coin's strength.",
}

def solve(heroes: list[int], coins: list[int]) -> int:
    """
    Calculates the maximum number of coins heroes can collect.
    
    A hero can collect a coin if the hero's strength is greater than or equal 
    to the coin's strength. Each hero can collect at most one coin.

    Args:
        heroes: A list of integers representing the strength of each hero.
        coins: A list of integers representing the strength of each coin.

    Returns:
        The maximum number of coins that can be collected.

    Examples:
        >>> solve([4, 2, 5, 9, 6], [1, 3, 4, 10])
        3
        >>> solve([1, 1, 1], [1, 1, 1])
        3
        >>> solve([1, 2, 3], [4, 5, 6])
        0
    """
    # Sort both lists to enable a two-pointer greedy approach.
    # Sorting allows us to match the weakest capable hero with the weakest available coin.
    heroes.sort()
    coins.sort()

    hero_index = 0
    coin_index = 0
    total_collected = 0
    
    num_heroes = len(heroes)
    num_coins = len(coins)

    # Iterate through both lists using two pointers.
    while hero_index < num_heroes and coin_index < num_coins:
        # If the current hero is strong enough for the current coin
        if heroes[hero_index] >= coins[coin_index]:
            # Match found: increment count and move to the next coin
            total_collected += 1
            coin_index += 1
            # Move to the next hero regardless
            hero_index += 1
        else:
            # Current hero is too weak for the current coin; 
            # since coins are sorted, this hero is too weak for all subsequent coins.
            # Move to a stronger hero.
            hero_index += 1

    return total_collected
