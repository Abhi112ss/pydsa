METADATA = {
    "id": 3928,
    "name": "Minimum Cost to Buy Apples II",
    "slug": "minimum-cost-to-buy-apples-ii",
    "category": "Greedy",
    "aliases": [],
    "tags": ["greedy", "sorting"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(1)",
    "description": "Find the minimum cost to purchase a required number of apples given specific pricing constraints and bulk discounts.",
}

def solve(prices: list[int], k: int) -> int:
    """
    Calculates the minimum cost to buy k apples using a greedy approach.
    
    The strategy is to sort the prices in ascending order and pick the 
    cheapest apples first. Since the problem implies we want to minimize 
    the total cost, we always prioritize the lowest available prices.

    Args:
        prices: A list of integers representing the cost of each apple.
        k: The total number of apples required to be purchased.

    Returns:
        The minimum total cost to purchase exactly k apples.

    Examples:
        >>> solve([1, 5, 2, 4, 3], 3)
        6
        >>> solve([10, 2, 5, 1], 2)
        3
    """
    # Sort prices to ensure we always pick the cheapest available apples first
    prices.sort()
    
    total_cost = 0
    # Iterate through the sorted prices and pick the first k elements
    for i in range(k):
        total_cost += prices[i]
        
    return total_cost
