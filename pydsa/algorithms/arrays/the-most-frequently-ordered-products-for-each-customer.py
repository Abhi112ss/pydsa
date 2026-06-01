METADATA = {
    "id": 1596,
    "name": "The Most Frequently Ordered Products for Each Customer",
    "slug": "the_most_frequently_ordered_products_for_each_customer",
    "category": "Database",
    "aliases": [],
    "tags": ["sql", "window function", "group by"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Return each customer's most frequently ordered product(s).",
}


def solve(orders: list[list[int]]) -> list[list[int]]:
    """Return the most frequently ordered product(s) for each customer.

    Args:
        orders: A list of rows, where each row is a list containing
            [customer_id, product_id, order_date]. The order_date value is
            ignored for the computation.

    Returns:
        A list of [customer_id, product_id] rows representing the product(s)
        that each customer ordered the most times. The result is sorted first
        by ``customer_id`` and then by ``product_id`` in ascending order.

    Examples:
        >>> solve([[1, 1, 20200101], [1, 2, 20200102], [1, 1, 20200103],
        ...        [2, 3, 20200101], [2, 3, 20200102], [2, 4, 20200103]])
        [[1, 1], [2, 3]]
        >>> solve([])
        []
    """
    # Count how many times each (customer, product) pair appears.
    customer_product_counts: dict[int, dict[int, int]] = {}
    for row in orders:
        customer_id, product_id = row[0], row[1]
        product_counts = customer_product_counts.setdefault(customer_id, {})
        product_counts[product_id] = product_counts.get(product_id, 0) + 1

    # Determine the maximum frequency for each customer and collect products
    # that reach this frequency.
    result: list[list[int]] = []
    for customer_id, product_counts in customer_product_counts.items():
        max_frequency = max(product_counts.values())
        for product_id, frequency in product_counts.items():
            if frequency == max_frequency:
                result.append([customer_id, product_id])

    # Sort the final output as required by the problem statement.
    result.sort(key=lambda entry: (entry[0], entry[1]))
    return result