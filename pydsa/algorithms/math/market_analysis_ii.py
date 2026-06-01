METADATA = {
    "id": 1159,
    "name": "Market Analysis II",
    "slug": "market-analysis-ii",
    "category": "Database/Algorithm",
    "aliases": [],
    "tags": ["hash_map", "sorting", "simulation"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Find the number of sellers whose second most recent order was for their favorite brand.",
}

def solve(orders: list[dict], favorites: list[dict]) -> int:
    """
    Determines how many sellers had their second most recent order for their favorite brand.

    Args:
        orders: A list of dictionaries where each dict contains 'seller_id', 'brand', and 'order_date'.
        favorites: A list of dictionaries where each dict contains 'seller_id' and 'favorite_brand'.

    Returns:
        The count of sellers whose second most recent order matches their favorite brand.

    Examples:
        >>> orders = [
        ...     {"seller_id": 1, "brand": "A", "order_date": "2021-01-01"},
        ...     {"seller_id": 1, "brand": "B", "order_date": "2021-01-02"},
        ...     {"seller_id": 1, "brand": "C", "order_date": "2021-01-03"},
        ...     {"seller_id": 2, "brand": "A", "order_date": "2021-01-01"}
        ... ]
        >>> favorites = [
        ...     {"seller_id": 1, "favorite_brand": "B"},
        ...     {"seller_id": 2, "favorite_brand": "A"}
        ... ]
        >>> solve(orders, favorites)
        1
    """
    # Group orders by seller_id
    # seller_orders maps seller_id -> list of (order_date, brand)
    seller_orders: dict[int, list[tuple[str, str]]] = {}
    for order in orders:
        s_id = order["seller_id"]
        if s_id not in seller_orders:
            seller_orders[s_id] = []
        seller_orders[s_id].append((order["order_date"], order["brand"]))

    # Map seller_id to their favorite brand for O(1) lookup
    favorite_map: dict[int, str] = {
        fav["seller_id"]: fav["favorite_brand"] for fav in favorites
    }

    match_count = 0

    # Iterate through each seller that has a favorite brand defined
    for seller_id, fav_brand in favorite_map.items():
        if seller_id not in seller_orders:
            continue
        
        # Sort orders by date in descending order (most recent first)
        # We use the date string directly as ISO format allows lexicographical sorting
        current_seller_history = seller_orders[seller_id]
        current_seller_history.sort(key=lambda x: x[0], reverse=True)

        # Check if the seller has at least two orders
        # The second most recent order is at index 1
        if len(current_seller_history) >= 2:
            second_recent_brand = current_seller_history[1][1]
            if second_recent_brand == fav_brand:
                match_count += 1

    return match_count
