METADATA = {
    "id": 1581,
    "name": "Customer Who Visited but Did Not Make Any Transactions",
    "slug": "customer_who_visited_but_did_not_make_any_transactions",
    "category": "Database",
    "aliases": [],
    "tags": ["hash_map", "sql"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Find customers who visited but never made a transaction.",
}


def solve(visits: list[list[int | str]], transactions: list[list[int | str]]) -> list[int]:
    """Return the list of customer IDs that have at least one visit record but no transaction record.

    Args:
        visits: A list of records where each record is [customer_id, visit_date].
        transactions: A list of records where each record is [customer_id, transaction_date].

    Returns:
        A sorted list of unique customer IDs that appear in ``visits`` but never in ``transactions``.

    Examples:
        >>> visits = [[1, "2020-01-01"], [2, "2020-01-02"], [3, "2020-01-03"]]
        >>> transactions = [[2, "2020-01-02"]]
        >>> solve(visits, transactions)
        [1, 3]

        >>> visits = [[5, "2021-05-01"]]
        >>> transactions = [[5, "2021-05-01"]]
        >>> solve(visits, transactions)
        []
    """
    # Build a set of all customer IDs that have made at least one transaction.
    transaction_customers: set[int] = {record[0] for record in transactions}

    # Collect IDs that visited but are not in the transaction set; use a set to avoid duplicates.
    visited_without_transaction: set[int] = set()
    for visit_record in visits:
        customer_id = visit_record[0]
        if customer_id not in transaction_customers:
            visited_without_transaction.add(customer_id)

    # Return the result sorted in ascending order as required by the problem statement.
    return sorted(visited_without_transaction)