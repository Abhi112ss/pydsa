METADATA = {
    "id": 1511,
    "name": "Customer Order Frequency",
    "slug": "customer_order_frequency",
    "category": "Array",
    "aliases": [],
    "tags": ["hash_map", "arrays"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Return the number of customers that placed exactly one order.",
}


def solve(customer_ids: list[int]) -> int:
    """Count customers with exactly one order.

    Args:
        customer_ids: List of integers where each integer represents a customer ID
            that placed an order.

    Returns:
        The number of distinct customer IDs that appear exactly once in the list.

    Examples:
        >>> solve([1, 2, 2, 3, 3, 3])
        1
        >>> solve([4, 5, 6, 7])
        4
    """
    # Build frequency map for each customer ID
    frequency: dict[int, int] = {}
    for cid in customer_ids:
        frequency[cid] = frequency.get(cid, 0) + 1

    # Count how many IDs have a frequency of exactly one
    unique_order_count: int = sum(1 for count in frequency.values() if count == 1)
    return unique_order_count