METADATA = {
    "id": 1867,
    "name": "Orders With Maximum Quantity Above Average",
    "slug": "orders-with-maximum-quantity-above-average",
    "category": "Arrays",
    "aliases": [],
    "tags": ["arrays", "math"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Find the number of orders where the quantity is strictly greater than the average quantity of all orders.",
}

def solve(orders: list[list[int]]) -> int:
    """
    Calculates the number of orders with a quantity strictly greater than the average quantity.

    Args:
        orders: A list of lists where each inner list contains [order_id, quantity].

    Returns:
        The count of orders whose quantity is greater than the average quantity.

    Examples:
        >>> solve([[1, 10], [2, 20], [3, 30]])
        1
        >>> solve([[1, 1], [2, 1], [3, 1]])
        0
    """
    if not orders:
        return 0

    total_quantity = 0
    num_orders = len(orders)

    # First pass: Calculate the sum of all quantities to find the average
    for _, quantity in orders:
        total_quantity += quantity

    average_quantity = total_quantity / num_orders

    # Second pass: Count how many orders have a quantity strictly greater than the average
    count_above_average = 0
    for _, quantity in orders:
        if quantity > average_quantity:
            count_above_average += 1

    return count_above_average
