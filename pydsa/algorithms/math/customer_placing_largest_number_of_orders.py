METADATA = {
    "id": 586,
    "name": "Customer Placing the Largest Number of Orders",
    "slug": "customer_placing_the_largest_number_of_orders",
    "category": "Database",
    "aliases": [],
    "tags": ["hash_map", "sorting"],
    "difficulty": "easy",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Find the customer who placed the largest number of orders from the Orders table.",
}


def solve(orders: list[dict[str, int]]) -> list[dict[str, int]]:
    """Find the customer(s) with the largest number of orders.

    Args:
        orders: A list of dictionaries, each containing 'customer_number' and 'order_number'.

    Returns:
        A list of dictionaries with 'customer_number' for customers who placed the most orders.

    Examples:
        >>> solve([
        ...     {"customer_number": 1, "order_number": 101},
        ...     {"customer_number": 2, "order_number": 102},
        ...     {"customer_number": 1, "order_number": 103},
        ...     {"customer_number": 3, "order_number": 104},
        ...     {"customer_number": 1, "order_number": 105},
        ... ])
        [{'customer_number': 1}]

        >>> solve([
        ...     {"customer_number": 1, "order_number": 101},
        ...     {"customer_number": 2, "order_number": 102},
        ...     {"customer_number": 1, "order_number": 103},
        ...     {"customer_number": 2, "order_number": 104},
        ... ])
        [{'customer_number': 1}, {'customer_number': 2}]
    """
    # Step 1: Aggregate order counts per customer using a hash map
    order_counts: dict[int, int] = {}
    for order in orders:
        customer = order["customer_number"]
        order_counts[customer] = order_counts.get(customer, 0) + 1

    # Step 2: Find the maximum order count
    max_count = max(order_counts.values())

    # Step 3: Collect all customers with the maximum count
    result = [{"customer_number": customer} for customer, count in order_counts.items() if count == max_count]

    # Step 4: Sort by customer_number for consistent output
    result.sort(key=lambda x: x["customer_number"])

    return result