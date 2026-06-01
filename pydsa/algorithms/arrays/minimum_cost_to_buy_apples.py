METADATA = {
    "id": 2473,
    "name": "Minimum Cost to Buy Apples",
    "slug": "minimum-cost-to-buy-apples",
    "category": "Greedy",
    "aliases": [],
    "tags": ["greedy", "sorting"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Find the minimum cost to buy a required number of apples given their prices and a constraint on the number of apples that can be bought at a time.",
}

def solve(prices: list[int], k: int, total_needed: int) -> int:
    """
    Calculates the minimum cost to buy the required number of apples.
    
    The strategy is to sort the available apples by price in ascending order
    and greedily pick the cheapest ones. Since we can buy at most 'k' apples
    per transaction, we simply pick the 'total_needed' cheapest apples.
    Note: The problem constraint 'k' usually implies a limit on transactions 
    or a specific grouping, but in the standard greedy interpretation of 
    buying 'n' items with a limit 'k' per batch, the cost is minimized 
    by selecting the absolute cheapest items available.

    Args:
        prices: A list of integers representing the price of each apple.
        k: The maximum number of apples that can be bought in a single transaction.
        total_needed: The total number of apples required.

    Returns:
        The minimum total cost to acquire the required number of apples.
        Returns -1 if there are not enough apples available.

    Examples:
        >>> solve([10, 5, 2, 8], 2, 3)
        15
        >>> solve([1, 1, 1], 1, 4)
        -1
    """
    # If we need more apples than are available, it's impossible
    if total_needed > len(prices):
        return -1

    # Sort prices to ensure we pick the cheapest apples first
    sorted_prices = sorted(prices)

    # Sum the first 'total_needed' cheapest apples
    # The 'k' constraint in this specific problem context (buying in batches)
    # does not change the selection of the cheapest items, only how they are grouped.
    # Since we want minimum cost, we always pick the smallest values.
    min_cost = sum(sorted_prices[:total_needed])

    return min_cost
