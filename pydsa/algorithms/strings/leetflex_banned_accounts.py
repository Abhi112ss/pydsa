METADATA = {
    "id": 1747,
    "name": "Leetflex Banned Accounts",
    "slug": "leetflex_banned_accounts",
    "category": "Hash Table",
    "aliases": [],
    "tags": ["hash_set", "string"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(m)",
    "description": "Count accounts that do not contain any banned usernames.",
}


def solve(accounts: list[list[str]], banned: list[str]) -> int:
    """Count the number of accounts that do not contain any banned usernames.

    Args:
        accounts: A list where each element is a list of usernames belonging to one account.
        banned: A list of usernames that are prohibited.

    Returns:
        The count of accounts that have no usernames appearing in the banned list.

    Examples:
        >>> solve([["alice", "bob"], ["charlie"], ["dave", "eve"]], ["bob", "eve"])
        1
        >>> solve([["john"], ["doe", "smith"]], ["alice"])
        2
    """
    # Convert banned list to a hash set for O(1) look‑ups.
    banned_set = set(banned)

    not_banned_count = 0
    for account_usernames in accounts:
        # Assume the account is not banned until a banned username is found.
        account_is_banned = False
        for username in account_usernames:
            if username in banned_set:
                account_is_banned = True
                break  # No need to check remaining usernames in this account.
        if not account_is_banned:
            not_banned_count += 1

    return not_banned_count