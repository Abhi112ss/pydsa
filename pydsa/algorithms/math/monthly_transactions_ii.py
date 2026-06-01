METADATA = {
    "id": 1205,
    "name": "Monthly Transactions II",
    "slug": "monthly-transactions-ii",
    "category": "Hash Table",
    "aliases": [],
    "tags": ["hash_map", "math"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Calculate monthly transaction statistics including total amount, approved amount, and chargeback count per country.",
}

def solve(transactions: list[dict]) -> list[list]:
    """
    Aggregates transaction data to find monthly totals per country.

    Args:
        transactions: A list of dictionaries where each dictionary contains:
            'trans_date' (str), 'country' (str), 'state' (str), 'amount' (int).

    Returns:
        A list of lists where each inner list contains:
            [month, country, total_transactions, total_amount, approved_amount, chargeback_count].
            The result is sorted by month and then by country.

    Examples:
        >>> transactions = [
        ...     {"trans_date": "2018-12-01", "country": "US", "state": "declined", "amount": 10},
        ...     {"trans_date": "2018-12-01", "country": "US", "state": "approved", "amount": 20},
        ...     {"trans_date": "2019-01-01", "country": "US", "state": "approved", "amount": 30}
        ... ]
        >>> solve(transactions)
        [['2018-12', 'US', 2, 30, 20, 0], ['2019-01', 'US', 1, 30, 30, 0]]
    """
    # Map key: (month, country) -> value: [total_count, total_amount, approved_amount, chargeback_count]
    stats_map: dict[tuple[str, str], list[int]] = {}

    for txn in transactions:
        # Extract month in YYYY-MM format
        month = txn["trans_date"][:7]
        country = txn["country"]
        amount = txn["amount"]
        state = txn["state"]
        
        key = (month, country)
        
        if key not in stats_map:
            # Initialize: [count, total_amt, approved_amt, chargeback_cnt]
            stats_map[key] = [0, 0, 0, 0]
            
        current_stats = stats_map[key]
        
        # Update base metrics
        current_stats[0] += 1
        current_stats[1] += amount
        
        # Update conditional metrics based on transaction state
        if state == "approved":
            current_stats[2] += amount
        elif state == "chargeback":
            current_stats[3] += 1

    # Transform the map into the required list format
    result = []
    for (month, country), values in stats_map.items():
        result.append([
            month,
            country,
            values[0],  # total_transactions
            values[1],  # total_amount
            values[2],  # approved_amount
            values[3]   # chargeback_count
        ])

    # Sort by month (index 0) and then by country (index 1)
    result.sort(key=lambda x: (x[0], x[1]))
    
    return result
