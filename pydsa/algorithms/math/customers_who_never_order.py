METADATA = {
    "id": 183,
    "name": "Customers Who Never Order",
    "slug": "customers_who_never_order",
    "category": "Database",
    "aliases": ["CustomersWhoNeverOrder"],
    "tags": ["sql", "join", "subquery"],
    "difficulty": "easy",
    "time_complexity": "O(N + M)",
    "space_complexity": "O(M)",
    "description": "Find all customers who never placed an order given a list of customers and a list of orders.",
}

def solve(customers: list[dict], orders: list[dict]) -> list[str]:
    """
    Identifies customers who have not placed any orders.

    Args:
        customers: A list of dictionaries where each dict has 'id' and 'name'.
        orders: A list of dictionaries where each dict has 'id' and 'customerId'.

    Returns:
        A list of names of customers who do not appear in the orders list.

    Examples:
        >>> customers = [{"id": 1, "name": "Joe"}, {"id": 2, "name": "Henry"}]
        >>> orders = [{"id": 1, "customerId": 1}]
        >>> solve(customers, orders)
        ['Henry']
    """
    # Create a set of customer IDs who have placed at least one order for O(1) lookup
    ordered_customer_ids = {order["customerId"] for order in orders}

    # Filter customers whose ID is not present in the set of ordered customer IDs
    customers_without_orders = [
        customer["name"]
        for customer in customers
        if customer["id"] not in ordered_customer_ids
    ]

    return customers_without_orders