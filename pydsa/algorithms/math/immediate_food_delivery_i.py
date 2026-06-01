METADATA = {
    "id": 1173,
    "name": "Immediate Food Delivery I",
    "slug": "immediate-food-delivery-i",
    "category": "Database",
    "aliases": [],
    "tags": ["basic_math", "sql_logic"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Calculate the percentage of immediate orders (where order date equals delivery date) from the total orders.",
}

def solve(delivery: list[dict]) -> float:
    """
    Calculates the percentage of immediate orders.
    
    An order is considered 'immediate' if the order_date is the same as the 
    delivery_date. The result is rounded to two decimal places.

    Args:
        delivery: A list of dictionaries where each dictionary represents a row 
                  in the Delivery table. Each dict contains 'customer_id', 
                  'order_date', and 'delivery_date'.

    Returns:
        float: The percentage of immediate orders rounded to two decimal places.

    Examples:
        >>> delivery = [
        ...     {"customer_id": 1, "order_date": "2019-08-01", "delivery_date": "2019-08-02"},
        ...     {"customer_id": 2, "order_date": "2019-08-02", "delivery_date": "2019-08-02"},
        ...     {"customer_id": 3, "order_date": "2019-08-11", "delivery_date": "2019-08-11"}
        ... ]
        >>> solve(delivery)
        66.67
    """
    if not delivery:
        return 0.0

    immediate_count = 0
    total_orders = len(delivery)

    for record in delivery:
        # An order is immediate if the order date matches the delivery date
        if record["order_date"] == record["delivery_date"]:
            immediate_count += 1

    # Calculate the percentage: (immediate / total) * 100
    percentage = (immediate_count / total_orders) * 100

    # Return the result rounded to two decimal places
    return round(percentage, 2)
