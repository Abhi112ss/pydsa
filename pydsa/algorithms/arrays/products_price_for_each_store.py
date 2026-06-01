METADATA = {
    "id": 1777,
    "name": "Product's Price for Each Store",
    "slug": "products_price_for_each_store",
    "category": "Array",
    "aliases": [],
    "tags": ["monotonic_stack", "array", "stack"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Calculate the price of each product in each store, applying the most recent discount if available.",
}

def solve(price: list[int], discount: list[int]) -> list[list[int]]:
    """
    Calculates the price of each product in each store considering discounts.
    
    A discount at index i applies to the next product that has the same price 
    as price[i]. If no such product exists, the discount is ignored.

    Args:
        price: A list of integers representing the initial prices of products.
        discount: A list of integers representing the discount amounts.

    Returns:
        A list of lists where each inner list contains the final prices for that store.

    Examples:
        >>> solve([10, 2, 4, 5, 3], [2, 1, 3, 4, 5])
        [[10, 2, 4, 5, 3]]
        >>> solve([10, 2, 4, 5, 3], [2, 1, 3, 4, 5]) # Example with discount application
        # If price[0]=10 and discount[0]=2, and price[3]=10, then price[3] becomes 8.
    """
    n = len(price)
    # final_prices will store the price of each product after applying the latest discount
    final_prices = list(price)
    
    # monotonic_stack stores indices of prices for which we are looking for a matching price
    # to apply the discount. The stack helps us find the "nearest previous" occurrence.
    # We use a dictionary to map price values to their most recent discount index.
    # However, a monotonic stack approach for "nearest previous" usually involves 
    # tracking indices of prices seen so far.
    
    # last_seen_discount_index maps a price value to the index of the discount 
    # that applies to it.
    last_seen_discount_index: dict[int, int] = {}
    
    # To handle the "nearest previous" logic efficiently:
    # We iterate through the prices. For each price, we check if it was 
    # previously marked as a "discount trigger".
    
    # We need to track which index is currently "waiting" for a matching price.
    # Since a discount at index i applies to the NEXT occurrence of price[i]:
    # We can use a dictionary to store the index of the discount.
    
    active_discounts: dict[int, int] = {}
    
    for i in range(n):
        current_price = price[i]
        
        # If the current price matches a price that had a discount previously applied
        if current_price in active_discounts:
            discount_idx = active_discounts[current_price]
            final_prices[i] = current_price - discount[discount_idx]
            # Once a discount is applied, it is consumed (per problem logic: 
            # "the discount applies to the next product with the same price")
            # Actually, the problem implies the discount is applied to the NEXT 
            # occurrence. If there are multiple, the most recent one applies.
            # Let's refine: the discount at i applies to the next j > i where price[j] == price[i].
            # We remove it from active_discounts so it doesn't apply to the one after that.
            del active_discounts[current_price]
        
        # Now, this current price could also be a discount trigger for a future product
        # We store the index of the discount available for this price value.
        # If a new discount for the same price comes, it overwrites the old one 
        # because the problem asks for the "nearest previous" discount.
        active_discounts[current_price] = i

    # The problem asks for a list of lists (one for each store). 
    # In LeetCode 1777, the input structure is usually a single list of prices 
    # and a single list of discounts, but the output is a list of lists 
    # representing stores. However, the standard version of this problem 
    # (often seen in similar formats) treats the input as a single sequence.
    # Given the prompt's signature, we return the processed prices as a single-store list.
    
    return [final_prices]
