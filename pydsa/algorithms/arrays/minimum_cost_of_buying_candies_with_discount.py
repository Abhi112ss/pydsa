METADATA = {
    "id": 2144,
    "name": "Minimum Cost of Buying Candies With Discount",
    "slug": "minimum-cost-of-buying-candies-with-discount",
    "category": "Greedy",
    "aliases": [],
    "tags": ["greedy", "sorting"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(1)",
    "description": "Calculate the minimum cost to buy all candies given that for every two candies purchased, the third most expensive one is free.",
}

def solve(prices: list[int]) -> int:
    """
    Calculates the minimum cost to buy all candies using a greedy approach.
    
    To minimize the cost, we want to maximize the value of the free candies.
    By sorting the prices in descending order, we can pick the two most 
    expensive candies and get the third most expensive one for free.

    Args:
        prices: A list of integers representing the prices of candies.

    Returns:
        The minimum total cost to purchase all candies.

    Examples:
        >>> solve([1, 2, 3, 4, 5, 6])
        12
        >>> solve([10, 10, 10, 10, 10, 10])
        40
    """
    # Sort prices in descending order to ensure we pick the highest 
    # possible values for the 'free' slots.
    prices.sort(reverse=True)
    
    total_cost = 0
    n = len(prices)
    
    # Iterate through the sorted list. 
    # We pay for index 0, 1, then skip 2.
    # We pay for index 3, 4, then skip 5, and so on.
    for i in range(n):
        # The rule is: for every two candies bought, the third is free.
        # In a 0-indexed sorted list, the free candies are at indices 2, 5, 8...
        # These are indices where (i + 1) % 3 == 0.
        if (i + 1) % 3 != 0:
            total_cost += prices[i]
            
    return total_cost
