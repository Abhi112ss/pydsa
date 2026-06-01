METADATA = {
    "id": 3007,
    "name": "Maximum Number That Sum of the Prices Is Less Than or Equal to K",
    "slug": "maximum-number-that-sum-of-the-prices-is-less-than-or-equal-to-k",
    "category": "Greedy",
    "aliases": [],
    "tags": ["greedy", "sorting"],
    "difficulty": "easy",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(1)",
    "description": "Find the maximum number of items you can buy given a budget K and a list of prices.",
}

def solve(prices: list[int], k: int) -> int:
    """
    Calculates the maximum number of items that can be purchased without exceeding budget k.

    Args:
        prices: A list of integers representing the price of each item.
        k: An integer representing the total budget available.

    Returns:
        The maximum count of items that can be bought.

    Examples:
        >>> solve([4, 5, 2, 1], 10)
        3
        >>> solve([1, 2, 3, 4, 5], 1)
        1
        >>> solve([10, 20, 30], 5)
        0
    """
    # Sort prices in ascending order to pick the cheapest items first (Greedy approach)
    sorted_prices = sorted(prices)
    
    count = 0
    current_sum = 0
    
    for price in sorted_prices:
        # Check if adding the next cheapest item exceeds the budget
        if current_sum + price <= k:
            current_sum += price
            count += 1
        else:
            # Since the list is sorted, no subsequent items can fit if this one doesn't
            break
            
    return count
