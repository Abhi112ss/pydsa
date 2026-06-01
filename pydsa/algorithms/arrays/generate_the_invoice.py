METADATA = {
    "id": 2362,
    "name": "Generate the Invoice",
    "slug": "generate-the-invoice",
    "category": "Simulation",
    "aliases": [],
    "tags": ["array", "simulation"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Calculate the total invoice amount by aggregating item prices and applying specific tax or discount rules.",
}

def solve(items: list[float], tax_rate: float, discount_threshold: float, discount_rate: float) -> float:
    """
    Calculates the final invoice amount based on item prices, a tax rate, 
    and a conditional discount.

    The algorithm iterates through the items to find the subtotal, 
    applies a discount if the subtotal exceeds a threshold, 
    and finally applies the tax rate.

    Args:
        items: A list of prices for each item.
        tax_rate: The tax rate to be applied (e.g., 0.05 for 5%).
        discount_threshold: The subtotal amount above which a discount is applied.
        discount_rate: The discount rate to be applied (e.g., 0.1 for 10%).

    Returns:
        The final total amount of the invoice after discount and tax.

    Examples:
        >>> solve([10.0, 20.0, 30.0], 0.1, 50.0, 0.2)
        44.0
        >>> solve([10.0, 10.0], 0.05, 50.0, 0.1)
        21.0
    """
    subtotal = 0.0
    
    # Aggregate the total price of all items
    for price in items:
        subtotal += price
        
    # Apply discount if the subtotal meets or exceeds the threshold
    if subtotal >= discount_threshold:
        subtotal -= (subtotal * discount_rate)
        
    # Apply the tax rate to the (potentially discounted) subtotal
    total_amount = subtotal * (1.0 + tax_rate)
    
    return round(total_amount, 2)
