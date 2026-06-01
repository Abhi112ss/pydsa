METADATA = {
    "id": 2986,
    "name": "Find Third Transaction",
    "slug": "find_third_transaction",
    "category": "Sorting",
    "aliases": [],
    "tags": ["sorting", "selection"],
    "difficulty": "easy",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Find the third transaction based on a specific metric after sorting.",
}

def solve(transactions: list[dict], metric: str) -> dict | None:
    """
    Finds the third transaction in a list when sorted by a specified metric in descending order.

    Args:
        transactions: A list of dictionaries, where each dictionary represents a transaction.
        metric: The key in the dictionary to sort by.

    Returns:
        The third transaction dictionary if it exists, otherwise None.

    Examples:
        >>> txs = [{"id": 1, "amount": 100}, {"id": 2, "amount": 500}, {"id": 3, "amount": 300}, {"id": 4, "amount": 200}]
        >>> solve(txs, "amount")
        {'id': 3, 'amount': 300}
        >>> solve([{"id": 1, "amount": 100}], "amount")
        None
    """
    # If there are fewer than 3 transactions, we cannot find the third one
    if len(transactions) < 3:
        return None

    # Sort the transactions in descending order based on the provided metric.
    # We use a lambda to access the specific key provided in the metric argument.
    sorted_transactions = sorted(
        transactions, 
        key=lambda x: x[metric], 
        reverse=True
    )

    # Return the third element (index 2) from the sorted list
    return sorted_transactions[2]
