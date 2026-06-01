METADATA = {
    "id": 3657,
    "name": "Find Loyal Customers",
    "slug": "find_loyal_customers",
    "category": "Hash Table",
    "aliases": [],
    "tags": ["hash_map", "sorting"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Identify customers who meet a specific loyalty threshold based on their transaction frequency or total spend.",
}

def solve(transactions: list[dict], threshold: int) -> list[int]:
    """
    Identifies loyal customers whose transaction count meets or exceeds a given threshold.

    Args:
        transactions: A list of dictionaries where each dictionary represents a transaction.
            Each dictionary contains 'customer_id' (int) and 'amount' (float/int).
        threshold: The minimum number of transactions required to be considered loyal.

    Returns:
        A list of customer IDs that are considered loyal, sorted in ascending order.

    Examples:
        >>> solve([{"customer_id": 1, "amount": 10}, {"customer_id": 2, "amount": 5}, {"customer_id": 1, "amount": 20}], 2)
        [1]
        >>> solve([{"customer_id": 1, "amount": 10}, {"customer_id": 2, "amount": 5}, {"customer_id": 3, "amount": 10}], 1)
        [1, 2, 3]
    """
    # Dictionary to store the frequency of transactions per customer
    customer_transaction_counts: dict[int, int] = {}

    # Iterate through transactions to populate the frequency map
    for transaction in transactions:
        customer_id = transaction["customer_id"]
        customer_transaction_counts[customer_id] = customer_transaction_counts.get(customer_id, 0) + 1

    # Filter customer IDs that meet the loyalty threshold
    loyal_customers: list[int] = []
    for customer_id, count in customer_transaction_counts.items():
        if count >= threshold:
            loyal_customers.append(customer_id)

    # Return the sorted list of loyal customer IDs
    loyal_customers.sort()
    return loyal_customers
