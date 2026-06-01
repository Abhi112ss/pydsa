METADATA = {
    "id": 1327,
    "name": "List the Products Ordered in a Period",
    "slug": "list-the-products-ordered-in-a-period",
    "category": "Database",
    "aliases": [],
    "tags": ["math", "sql-equivalent"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(k) where k is number of unique products",
    "description": "Calculate the total units ordered for each product within a specific month and year.",
}

from collections import defaultdict

def solve(transactions: list[dict], month: int, year: int) -> list[dict]:
    """
    Calculates the total units ordered for each product within a specific month and year.

    Args:
        transactions: A list of dictionaries where each dictionary represents a transaction.
            Each dictionary contains 'product_id', 'unit', 'item_id', 'order_date', 
            'customer_id', and 'user_id'.
            'order_date' is a string in 'YYYY-MM-DD' format.
        month: The target month (1-12).
        year: The target year (e.g., 2021).

    Returns:
        A list of dictionaries, each containing 'product_id' and 'unit'.
        The list is sorted by 'product_id' in ascending order.

    Examples:
        >>> transactions = [
        ...     {"product_id": 1, "unit": 10, "item_id": 1, "order_date": "2021-01-01", "customer_id": 1, "user_id": 1},
        ...     {"product_id": 1, "unit": 5, "item_id": 2, "order_date": "2021-01-05", "customer_id": 2, "user_id": 2},
        ...     {"product_id": 2, "unit": 20, "item_id": 3, "order_date": "2021-01-10", "customer_id": 3, "user_id": 3},
        ...     {"product_id": 1, "unit": 10, "item_id": 4, "order_date": "2021-02-01", "customer_id": 4, "user_id": 4}
        ... ]
        >>> solve(transactions, 1, 2021)
        [{'product_id': 1, 'unit': 15}, {'product_id': 2, 'unit': 20}]
    """
    # Dictionary to aggregate units per product_id
    product_totals = defaultdict(int)

    for record in transactions:
        # Parse the date string 'YYYY-MM-DD'
        date_parts = record["order_date"].split("-")
        record_year = int(date_parts[0])
        record_month = int(date_parts[1])

        # Filter records by the specific month and year provided
        if record_year == year and record_month == month:
            product_id = record["product_id"]
            units = record["unit"]
            product_totals[product_id] += units

    # Transform the aggregated dictionary into the required list of dictionaries format
    result = []
    for product_id in sorted(product_totals.keys()):
        result.append({
            "product_id": product_id,
            "unit": product_totals[product_id]
        })

    return result
