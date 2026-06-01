METADATA = {
    "id": 1843,
    "name": "Suspicious Bank Accounts",
    "slug": "suspicious_bank_accounts",
    "category": "Hash Table",
    "aliases": [],
    "tags": ["hash_map", "array", "counting"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Identify bank accounts that have a transaction frequency higher than the average transaction frequency across all accounts.",
}

def solve(transactions: list[int], account_ids: list[int]) -> list[int]:
    """
    Identifies suspicious bank accounts based on transaction frequency.
    
    A bank account is considered suspicious if its number of transactions 
    is strictly greater than the average number of transactions per account.

    Args:
        transactions: A list of transaction amounts (not used for frequency calculation, 
                      but represents the sequence of events).
        account_ids: A list of account IDs corresponding to each transaction.

    Returns:
        A list of account IDs that are suspicious, sorted in ascending order.

    Examples:
        >>> solve([10, 20, 30, 40, 50], [1, 2, 1, 3, 2])
        [1, 2]
        # Account 1: 2 tx, Account 2: 2 tx, Account 3: 1 tx. 
        # Avg = (2+2+1)/3 = 1.66. 1 and 2 are > 1.66.
    """
    if not account_ids:
        return []

    # Step 1: Count transactions per account using a hash map
    transaction_counts: dict[int, int] = {}
    for account_id in account_ids:
        transaction_counts[account_id] = transaction_counts.get(account_id, 0) + 1

    # Step 2: Calculate the average number of transactions per account
    total_transactions = len(account_ids)
    unique_accounts_count = len(transaction_counts)
    average_frequency = total_transactions / unique_accounts_count

    # Step 3: Identify accounts with frequency strictly greater than average
    suspicious_accounts: list[int] = []
    for account_id, count in transaction_counts.items():
        if count > average_frequency:
            suspicious_accounts.append(account_id)

    # Return sorted list as per standard LeetCode requirements for such problems
    return sorted(suspicious_accounts)
