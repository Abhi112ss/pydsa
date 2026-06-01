METADATA = {
    "id": 1193,
    "name": "Monthly Transactions I",
    "slug": "monthly-transactions-i",
    "category": "SQL",
    "aliases": [],
    "tags": ["sql", "group_by", "aggregation"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Calculate monthly transaction counts and amounts per country, including approved transaction statistics.",
}

from collections import defaultdict

def solve(transactions: list[dict]) -> list[dict]:
    """
    Processes transaction data to calculate monthly statistics per country.

    Args:
        transactions: A list of dictionaries where each dictionary represents a transaction.
            Each dictionary contains:
            - 'trans_id': int
            - 'country': str
            - 'state': str ('approved' or 'declined')
            - 'amount': int
            - 'trans_date': str (format 'YYYY-MM-DD')

    Returns:
        A list of dictionaries containing aggregated statistics:
        - 'month': str (format 'YYYY-MM')
        - 'country': str
        - 'trans_count': int
        - 'approved_count': int
        - 'trans_total_amount': int
        - 'approved_total_amount': int

    Examples:
        >>> data = [
        ...     {"trans_id": 1, "country": "US", "state": "approved", "amount": 100, "trans_date": "2018-12-01"},
        ...     {"trans_id": 2, "country": "US", "state": "declined", "amount": 50, "trans_date": "2018-12-15"},
        ...     {"trans_id": 3, "country": "US", "state": "approved", "amount": 200, "trans_date": "2019-01-01"}
        ... ]
        >>> solve(data)
        [{'month': '2018-12', 'country': 'US', 'trans_count': 2, 'approved_count': 1, 'trans_total_amount': 150, 'approved_total_amount': 100},
         {'month': '2019-01', 'country': 'US', 'trans_count': 1, 'approved_count': 1, 'trans_total_amount': 200, 'approved_total_amount': 200}]
    """
    # Key: (month_string, country) -> Value: dict of running totals
    # month_string is extracted from trans_date as 'YYYY-MM'
    aggregates = defaultdict(lambda: {
        "trans_count": 0,
        "approved_count": 0,
        "trans_total_amount": 0,
        "approved_total_amount": 0
    })

    for transaction in transactions:
        # Extract YYYY-MM from YYYY-MM-DD
        month = transaction["trans_date"][:7]
        country = transaction["country"]
        state = transaction["state"]
        amount = transaction["amount"]

        group_key = (month, country)
        stats = aggregates[group_key]

        # Update general transaction metrics
        stats["trans_count"] += 1
        stats["trans_total_amount"] += amount

        # Conditional aggregation for approved transactions
        if state == "approved":
            stats["approved_count"] += 1
            stats["approved_total_amount"] += amount

    # Transform the aggregated dictionary into the required list of dictionaries format
    result = []
    for (month, country), stats in aggregates.items():
        result.append({
            "month": month,
            "country": country,
            "trans_count": stats["trans_count"],
            "approved_count": stats["approved_count"],
            "trans_total_amount": stats["trans_total_amount"],
            "approved_total_amount": stats["approved_total_amount"]
        })

    return result
