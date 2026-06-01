METADATA = {
    "id": 3100,
    "name": "Water Bottles II",
    "slug": "water-bottles-ii",
    "category": "Math",
    "aliases": [],
    "tags": ["math", "greedy", "simulation"],
    "difficulty": "medium",
    "time_complexity": "O(log n)",
    "space_complexity": "O(1)",
    "description": "Simulate the process of drinking water and exchanging empty bottles for full ones where the exchange requirement increases each time.",
}

def solve(num_bottles: int, num_exchange: int) -> int:
    """
    Calculates the total number of water bottles one can drink given an initial
    amount and an increasing exchange requirement.

    Args:
        num_bottles: The initial number of full water bottles.
        num_exchange: The initial number of empty bottles required for one full bottle.

    Returns:
        The total number of water bottles consumed.

    Examples:
        >>> solve(10, 3)
        13
        >>> solve(10, 4)
        12
        >>> solve(5, 5)
        5
    """
    total_consumed = num_bottles
    empty_bottles = num_bottles

    # Continue as long as we have enough empty bottles to meet the current exchange requirement
    while empty_bottles >= num_exchange:
        # Perform the exchange: get new full bottles
        new_bottles = empty_bottles // num_exchange
        
        # Calculate remaining empty bottles after exchange plus the newly consumed ones
        # Note: The remainder from the exchange is kept
        empty_bottles = (empty_bottles % num_exchange) + new_bottles
        
        # Increment total consumption
        total_consumed += new_bottles
        
        # The exchange requirement increases by 1 for the next round
        num_exchange += 1

    return total_consumed
