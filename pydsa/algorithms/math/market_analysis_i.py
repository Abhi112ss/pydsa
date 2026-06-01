METADATA = {
    "id": 1158,
    "name": "Market Analysis I",
    "slug": "market_analysis_i",
    "category": "Database",
    "aliases": [],
    "tags": ["hash_map", "date_processing"],
    "difficulty": "medium",
    "time_complexity": "O(N + M)",
    "space_complexity": "O(N)",
    "description": "Find the number of own orders made by each user in 2019.",
}

from typing import List, Dict


def solve(users: List[Dict], orders: List[Dict]) -> List[Dict]:
    """
    Calculates the number of orders made by each user in the year 2019.

    The function performs a logic equivalent to a LEFT JOIN between the users 
    table and the orders table, filtering orders by the year 2019.

    Args:
        users: A list of dictionaries where each dict represents a user 
               containing 'user_id' and 'join_date'.
        orders: A list of dictionaries where each dict represents an order 
                containing 'order_id', 'order_date', and 'user_id'.

    Returns:
        A list of dictionaries containing 'user_id' and 'orders_in_2019'.

    Examples:
        >>> users = [{'user_id': 1, 'join_date': '2018-01-01'}, {'user_id': 2, 'join_date': '2019-01-01'}]
        >>> orders = [{'order_id': 1, 'order_date': '2019-01-01', 'user_id': 1}, {'order_id': 2, 'order_date': '2019-02-01', 'user_id': 1}]
        >>> solve(users, orders)
        [{'user_id': 1, 'orders_in_2019': 2}, {'user_id': 2, 'orders_in_2019': 0}]
    """
    # Initialize a map to store the count of 2019 orders per user_id
    # This handles the "LEFT JOIN" requirement by ensuring all users are accounted for
    order_counts: Dict[int, int] = {}

    # Iterate through orders to count those occurring in 2019
    for order in orders:
        # Extract year from the date string (format 'YYYY-MM-DD')
        order_year = order["order_date"][:4]
        if order_year == "2019":
            user_id = order["user_id"]
            order_counts[user_id] = order_counts.get(user_id, 0) + 1

    results: List[Dict] = []

    # Iterate through all users to build the final result set
    # This ensures users with 0 orders in 2019 are included
    for user in users:
        user_id = user["user_id"]
        count = order_counts.get(user_id, 0)
        results.append({
            "user_id": user_id,
            "orders_in_2019": count
        })

    return results
