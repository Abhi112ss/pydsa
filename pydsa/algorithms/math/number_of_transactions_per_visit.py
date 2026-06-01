METADATA = {
    "id": 1336,
    "name": "Number of Transactions per Visit",
    "slug": "number-of-transactions-per-visit",
    "category": "SQL/Math",
    "aliases": [],
    "tags": ["math", "aggregation", "sequence"],
    "difficulty": "medium",
    "time_complexity": "O(N)",
    "space_complexity": "O(N)",
    "description": "Calculate the number of transactions for each visit, ensuring visits with zero transactions are included.",
}

def solve(visits: list[dict], transactions: list[dict]) -> list[dict]:
    """
    Calculates the number of transactions for each visit.

    Args:
        visits: A list of dictionaries where each dict represents a visit 
                with 'visit_id' and 'customer_id'.
        transactions: A list of dictionaries where each dict represents a 
                      transaction with 'transaction_id', 'visit_id', and 'amount'.

    Returns:
        A list of dictionaries containing 'visit_id' and 'count_of_transactions'.
        The list is sorted by 'visit_id' in ascending order.

    Examples:
        >>> visits = [{'visit_id': 1, 'customer_id': 1}, {'visit_id': 2, 'customer_id': 1}]
        >>> transactions = [{'transaction_id': 1, 'visit_id': 1, 'amount': 10}]
        >>> solve(visits, transactions)
        [{'visit_id': 1, 'count_of_transactions': 1}, {'visit_id': 2, 'count_of_transactions': 0}]
    """
    # Map visit_id to the count of transactions using a hash map for O(1) lookup
    transaction_counts = {}
    for transaction in transactions:
        v_id = transaction['visit_id']
        transaction_counts[v_id] = transaction_counts.get(v_id, 0) + 1

    result = []
    
    # Iterate through all visits to ensure we include those with zero transactions (Left Join logic)
    for visit in visits:
        v_id = visit['visit_id']
        # If the visit_id is not in our transaction map, the count is 0
        count = transaction_counts.get(v_id, 0)
        result.append({
            "visit_id": v_id,
            "count_of_transactions": count
        })

    # Sort the result by visit_id as per standard SQL output expectations for this problem
    result.sort(key=lambda x: x["visit_id"])
    
    return result
