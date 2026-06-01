METADATA = {
    "id": 2979,
    "name": "Most Expensive Item That Can Not Be Bought",
    "slug": "most-expensive-item-that-can-not-be-bought",
    "category": "Array",
    "aliases": [],
    "tags": ["arrays", "sorting"],
    "difficulty": "easy",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(1)",
    "description": "Find the maximum price of an item that is either more expensive than the budget or is unavailable.",
}

def solve(prices: list[int], budget: int, availability: list[bool]) -> int:
    """
    Finds the most expensive item that cannot be bought based on budget and availability.

    An item cannot be bought if its price is strictly greater than the budget 
    OR if its availability status is False.

    Args:
        prices: A list of integers representing the prices of items.
        budget: An integer representing the maximum amount of money available.
        availability: A list of booleans representing whether each item is available.

    Returns:
        The maximum price among all items that cannot be bought. 
        If no such item exists, returns -1.

    Examples:
        >>> solve([10, 20, 30], 25, [True, True, True])
        30
        >>> solve([10, 20, 30], 25, [True, False, True])
        30
        >>> solve([5, 5, 5], 10, [True, False, True])
        5
        >>> solve([10, 20], 30, [True, True])
        -1
    """
    max_unaffordable_price = -1

    # Iterate through all items to check the two conditions for being 'unaffordable'
    for price, is_available in zip(prices, availability):
        # Condition 1: Price exceeds budget
        # Condition 2: Item is not available
        if price > budget or not is_available:
            if price > max_unaffordable_price:
                max_unaffordable_price = price

    return max_unaffordable_price
