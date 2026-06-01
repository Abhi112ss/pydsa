METADATA = {
    "id": 2706,
    "name": "Buy Two Chocolates",
    "slug": "buy_two_chocolates",
    "category": "Array",
    "aliases": [],
    "tags": ["array", "sorting"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Return the maximum number of chocolates (0, 1, or 2) that can be bought with a given budget.",
}


def solve(prices: list[int], money: int) -> int:
    """Determine the maximum number of chocolates that can be bought.

    Args:
        prices: List of chocolate prices.
        money: Available amount of money.

    Returns:
        The maximum count of chocolates that can be purchased (0, 1, or 2).

    Examples:
        >>> solve([1, 2, 3, 4], 3)
        2
        >>> solve([5, 6, 7], 4)
        0
        >>> solve([10, 20, 30], 15)
        1
    """
    # Find the smallest and second smallest prices in a single pass.
    smallest_price = float('inf')
    second_smallest_price = float('inf')
    for price in prices:
        if price < smallest_price:
            second_smallest_price = smallest_price
            smallest_price = price
        elif price < second_smallest_price:
            second_smallest_price = price

    # If the cheapest chocolate exceeds the budget, none can be bought.
    if smallest_price > money:
        return 0

    # If the sum of the two cheapest chocolates fits the budget, buy two.
    if smallest_price + second_smallest_price <= money:
        return 2

    # Otherwise, only one chocolate can be bought.
    return 1