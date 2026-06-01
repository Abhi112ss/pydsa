METADATA = {
    "id": 1549,
    "name": "The Most Recent Orders for Each Product",
    "slug": "the-most-recent-orders-for-each-product",
    "category": "Database/Algorithm",
    "aliases": [],
    "tags": ["hash_map", "sorting"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Retrieve the most recent order details for each unique product from a list of orders.",
}

def solve(orders: list[dict]) -> list[dict]:
    """
    Finds the most recent order for each unique product.

    Args:
        orders: A list of dictionaries, where each dictionary represents an order
                containing 'order_id', 'product_id', 'customer_id', and 'timestamp'.

    Returns:
        A list of dictionaries containing the most recent order details for each product,
        sorted by product_id in ascending order.

    Examples:
        >>> orders = [
        ...     {"order_id": 1, "product_id": 1, "customer_id": 10, "timestamp": 100},
        ...     {"order_id": 2, "product_id": 1, "customer_id": 11, "timestamp": 200},
        ...     {"order_id": 3, "product_id": 2, "customer_id": 12, "timestamp": 150}
        ... ]
        >>> solve(orders)
        [{'order_id': 2, 'product_id': 1, 'customer_id': 11, 'timestamp': 200}, 
         {'order_id': 3, 'product_id': 2, 'customer_id': 12, 'timestamp': 150}]
    """
    if not orders:
        return []

    # Sort orders by timestamp in descending order.
    # This ensures that the first time we encounter a product_id, 
    # it is the most recent one.
    sorted_orders = sorted(orders, key=lambda x: x["timestamp"], reverse=True)

    # Use a hash map to store the first occurrence of each product_id.
    # Since we sorted by timestamp DESC, the first occurrence is the latest.
    latest_orders_map: dict[int, dict] = {}

    for order in sorted_orders:
        product_id = order["product_id"]
        if product_id not in latest_orders_map:
            latest_orders_map[product_id] = order

    # Extract the values and sort them by product_id ascending as per standard requirements.
    result = list(latest_orders_map.values())
    result.sort(key=lambda x: x["product_id"])

    return result
