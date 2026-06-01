METADATA = {
    "id": 1565,
    "name": "Unique Orders and Customers Per Month",
    "slug": "unique-orders-and-customers-per-month",
    "category": "SQL",
    "aliases": [],
    "tags": ["sql", "grouping", "aggregation"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Calculate the number of unique orders and unique customers for each month.",
}

from dataclasses import dataclass
from datetime import datetime
from collections import defaultdict


@dataclass(frozen=True)
class OrderRecord:
    order_id: int
    customer_id: int
    order_date: datetime


def solve(orders: list[OrderRecord]) -> list[dict[str, any]]:
    """
    Calculates the number of unique orders and unique customers for each month.

    Args:
        orders: A list of OrderRecord objects containing order details.

    Returns:
        A list of dictionaries where each dictionary contains 'month', 
        'orders' (count of unique order IDs), and 'customers' (count of unique customer IDs).
        The list is sorted by month in descending order.

    Examples:
        >>> orders = [
        ...     OrderRecord(1, 1, datetime(2019, 1, 1)),
        ...     OrderRecord(2, 1, datetime(2019, 1, 2)),
        ...     OrderRecord(3, 2, datetime(2019, 1, 3)),
        ...     OrderRecord(4, 3, datetime(2019, 2, 1))
        ... ]
        >>> solve(orders)
        [{'month': '2019-02', 'orders': 1, 'customers': 1}, {'month': '2019-01', 'orders': 3, 'customers': 2}]
    """
    # month_stats maps "YYYY-MM" string to a set of order_ids and a set of customer_ids
    # Using sets ensures we only count unique occurrences (DISTINCT in SQL)
    month_stats: dict[str, dict[str, set[int]]] = defaultdict(
        lambda: {"order_ids": set(), "customer_ids": set()}
    )

    for record in orders:
        # Format the date to YYYY-MM to group by month
        month_key = record.order_date.strftime("%Y-%m")
        
        # Add the order_id and customer_id to their respective sets for that month
        month_stats[month_key]["order_ids"].add(record.order_id)
        month_stats[month_key]["customer_ids"].add(record.customer_id)

    results: list[dict[str, any]] = []
    for month, data in month_stats.items():
        results.append({
            "month": month,
            "orders": len(data["order_ids"]),
            "customers": len(data["customer_ids"])
        })

    # Sort results by month in descending order as per typical SQL requirement for this problem
    results.sort(key=lambda x: x["month"], reverse=True)
    
    return results
