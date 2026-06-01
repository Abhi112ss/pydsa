METADATA = {
    "id": 1587,
    "name": "Bank Account Summary II",
    "slug": "bank_account_summary_ii",
    "category": "Database",
    "aliases": [],
    "tags": ["SQL", "Join", "Not In"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Return each non‑deleted account with the total amount of its transactions.",
}


def solve() -> str:
    """Generate the SQL query for LeetCode 1587 – Bank Account Summary II.

    Returns:
        str: A SQL statement that lists each account (excluding deleted ones)
            together with the sum of its transaction amounts. Accounts with no
            transactions appear with a total of 0.

    Example:
        >>> query = solve()
        >>> isinstance(query, str)
        True
    """
    # Use LEFT JOIN to keep accounts without transactions and filter out deleted accounts.
    query = (
        "SELECT a.account_id, "
        "a.account_name, "
        "COALESCE(SUM(t.amount), 0) AS total_amount "
        "FROM Accounts AS a "
        "LEFT JOIN Transactions AS t ON a.account_id = t.account_id "
        "WHERE a.deleted = 0 "
        "GROUP BY a.account_id, a.account_name "
        "ORDER BY a.account_id"
    )
    return query