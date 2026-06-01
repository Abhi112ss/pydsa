METADATA = {
    "id": 3293,
    "name": "Calculate Product Final Price in an Array",
    "slug": "calculate-product-final-price-in-an-array",
    "category": "Array",
    "aliases": [],
    "tags": ["monotonic_stack", "array"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Calculate the final price of each item by applying a discount from the next smaller or equal element to its right.",
}

def solve(prices: list[int]) -> list[int]:
    """
    Calculates the final price of each item in the array.
    
    For each index i, the discount is the value at the first index j > i 
    such that prices[j] <= prices[i]. If no such index exists, the discount is 0.

    Args:
        prices: A list of integers representing the initial prices.

    Returns:
        A list of integers representing the final prices after discounts.

    Examples:
        >>> solve([8, 4, 5, 2, 10])
        [4, 2, 2, 2, 10]
        >>> solve([10, 1, 1, 1])
        [1, 1, 1, 1]
    """
    n = len(prices)
    final_prices = list(prices)
    # The stack will store indices of elements for which we haven't found a discount yet.
    # It maintains a monotonic increasing order of values.
    stack: list[int] = []

    for current_index in range(n):
        current_price = prices[current_index]
        
        # While the stack is not empty and the current price is less than or equal 
        # to the price at the index stored at the top of the stack, 
        # the current price is the discount for that index.
        while stack and prices[stack[-1]] >= current_price:
            index_to_discount = stack.pop()
            final_prices[index_to_discount] -= current_price
            
        stack.append(current_index)

    return final_prices
