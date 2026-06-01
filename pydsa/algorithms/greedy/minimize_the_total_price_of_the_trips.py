METADATA = {
    "id": 2646,
    "name": "Minimize the Total Price of the Trips",
    "slug": "minimize-the-total-price-of-the-trips",
    "category": "Greedy",
    "aliases": [],
    "tags": ["greedy", "hash_map", "sorting"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Minimize the total cost of trips by applying discounts to the most expensive items available.",
}

def solve(prices: list[list[int]], discounts: list[int]) -> int:
    """
    Calculates the minimum total price of all trips by applying discounts 
    to the highest available prices across all trips.

    Args:
        prices: A list of lists, where each sublist represents the prices 
                of items in a single trip.
        discounts: A list of integers representing the discount values 
                   available to be applied.

    Returns:
        The minimum total price after applying all possible discounts.

    Examples:
        >>> solve([[1, 2, 3], [4, 5, 6]], [1, 2])
        18
        >>> solve([[1, 1, 1], [1, 1, 1]], [1, 1, 1, 1])
        2
    """
    MOD = 10**9 + 7
    
    # Flatten all prices into a single list to treat all items globally
    all_prices = []
    for trip in prices:
        all_prices.extend(trip)
    
    # Sort all prices in descending order to apply discounts to the largest values
    all_prices.sort(reverse=True)
    
    # Sort discounts in descending order to ensure we subtract the largest 
    # possible values from the largest possible prices
    discounts.sort(reverse=True)
    
    # Apply discounts to the top N prices where N is the number of available discounts
    # We only apply a discount if it actually reduces the price (discount > 0)
    # and if we have more items than discounts.
    num_discounts = len(discounts)
    for i in range(min(num_discounts, len(all_prices))):
        # The problem implies we subtract the discount value from the price.
        # However, the discount is applied to the item, so we subtract it.
        # Note: The problem states "the discount is applied to the item", 
        # meaning price = price - discount.
        all_prices[i] -= discounts[i]
        
    # Sum the remaining prices and return modulo 10^9 + 7
    return sum(all_prices) % MOD
