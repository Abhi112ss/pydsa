METADATA = {
    "id": 1518,
    "name": "Water Bottles",
    "slug": "water-bottles",
    "category": "Simulation",
    "aliases": [],
    "tags": ["math", "simulation"],
    "difficulty": "easy",
    "time_complexity": "O(log_{num_exchange}(num_bottles))",
    "space_complexity": "O(1)",
    "description": "Calculate the total number of water bottles you can drink by exchanging empty bottles for full ones.",
}

def solve(num_bottles: int, num_exchange: int) -> int:
    """
    Calculates the total number of water bottles consumed.

    Args:
        num_bottles: The initial number of full water bottles.
        num_exchange: The number of empty bottles required to get one full bottle.

    Returns:
        The total number of water bottles drunk.

    Examples:
        >>> solve(9, 3)
        13
        >>> solve(15, 4)
        19
    """
    total_drunk = num_bottles
    empty_bottles = num_bottles

    # Continue the process as long as we have enough empty bottles to exchange
    while empty_bottles >= num_exchange:
        # Calculate how many new full bottles we get from the current empty ones
        new_bottles = empty_bottles // num_exchange
        
        # Calculate how many empty bottles are left over after the exchange
        remaining_empty = empty_bottles % num_exchange
        
        # Add the new bottles to our total consumption
        total_drunk += new_bottles
        
        # Our new empty bottle count is the ones we just drank plus the leftovers
        empty_bottles = new_bottles + remaining_empty

    return total_drunk
