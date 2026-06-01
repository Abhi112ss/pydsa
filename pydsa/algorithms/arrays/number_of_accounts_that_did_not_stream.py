METADATA = {
    "id": 2020,
    "name": "Number of Accounts That Did Not Stream",
    "slug": "number-of-accounts-that-did-not-stream",
    "category": "Hash Table",
    "aliases": [],
    "tags": ["hash_map", "arrays"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Find the number of accounts that have not appeared in the stream of account IDs.",
}

def solve(accounts: list[int], stream: list[int]) -> int:
    """
    Calculates the number of accounts that did not appear in the stream.

    Args:
        accounts: A list of all unique account IDs.
        stream: A list of account IDs that appeared in the stream.

    Returns:
        The count of accounts from the 'accounts' list that are not present in 'stream'.

    Examples:
        >>> solve([1, 2, 3, 4, 5], [2, 4, 5])
        2
        >>> solve([10, 20, 30], [10, 20, 30])
        0
        >>> solve([1, 2], [])
        2
    """
    # Convert the stream to a set for O(1) average time complexity lookups
    stream_set = set(stream)
    
    # Track how many accounts from the original list are found in the stream set
    active_accounts_count = 0
    
    for account_id in accounts:
        if account_id in stream_set:
            active_accounts_count += 1
            
    # The result is the total number of accounts minus those that were active
    return len(accounts) - active_accounts_count
