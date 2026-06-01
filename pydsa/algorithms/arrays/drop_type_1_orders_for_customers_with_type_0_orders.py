METADATA = {
    "id": 2084,
    "name": "Drop Type 1 Orders for Customers With Type 0 Orders",
    "slug": "drop_type_1_orders_for_customers_with_type_0_orders",
    "category": "Array",
    "aliases": [],
    "tags": ["array", "hash_map"],
    "difficulty": "Easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Remove type‑1 orders for customers that have placed a type‑0 order, preserving the original order.",
}

def solve(orders: list[list[int]]) -> list[list[int]]:
    """Return the list of orders after dropping type‑1 orders for customers
    that have at least one type‑0 order.

    Args:
        orders: A list where each element is a two‑element list
                [customer_id, order_type] with order_type being 0 or 1.

    Returns:
        A filtered list of orders preserving the original relative order.

    Examples:
        >>> solve([[1,0],[1,1],[2,1],[2,0],[3,1]])
        [[1,0],[2,0],[3,1]]
        >>> solve([[5,1],[5,1],[5,0]])
        [[5,1],[5,1],[5,0]]
    """
    # First pass: collect all customers that have placed a type‑0 order.
    customers_with_type0: set[int] = set()
    for order in orders:
        customer_id, order_type = order[0], order[1]
        if order_type == 0:
            customers_with_type0.add(customer_id)

    # Second pass: keep orders that are type‑0 or belong to customers without a type‑0 order.
    filtered_orders: list[list[int]] = []
    for order in orders:
        customer_id, order_type = order[0], order[1]
        if order_type == 0 or customer_id not in customers_with_type0:
            filtered_orders.append(order)

    return filtered_orders