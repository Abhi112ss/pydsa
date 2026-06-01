METADATA = {
    "id": 1475,
    "name": "Final Prices With a Special Discount in a Shop",
    "slug": "final-prices-with-a-special-discount-in-a-shop",
    "category": "Stack",
    "aliases": [],
    "tags": ["stack", "monotonic_stack"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Calculate the final prices of items after applying a discount equal to the first smaller or equal price to the right.",
}

def solve(prices: list[int]) -> list[int]:
    """
    Calculates the final prices of items after applying a special discount.
    
    The discount for an item at index i is the value of the first item at index j 
    such that j > i and prices[j] <= prices[i]. If no such item exists, 
    no discount is applied.

    Args:
        prices: A list of integers representing the original prices of items.

    Returns:
        A list of integers representing the final prices after discounts.

    Examples:
        >>> solve([8, 4, 6, 2, 3])
        [4, 2, 2, 2, 3]
        >>> solve([2, 1, 2, 1, 1])
        [1, 1, 1, 1, 1]
    """
    n = len(prices)
    final_prices = list(prices)
    # monotonic_stack will store indices of prices for which we haven't found a discount yet
    monotonic_stack: list[int] = []

    for current_index in range(n):
        current_price = prices[current_index]
        
        # While the stack is not empty and the current price is less than or equal 
        # to the price at the index stored at the top of the stack, 
        # the current price acts as the discount for that index.
        while monotonic_stack and prices[monotonic_stack[-1]] >= current_price:
            index_to_discount = monotonic_stack.pop()
            final_prices[index_to_discount] -= current_price
            
        # Push the current index onto the stack to find its discount later
        monotonic_stack.append(current_index)

    return final_prices
