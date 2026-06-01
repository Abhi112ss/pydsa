METADATA = {
    "id": 465,
    "name": "Optimal Account Balancing",
    "slug": "optimal-account-balancing",
    "category": "Backtracking",
    "aliases": [],
    "tags": ["backtracking", "recursion", "greedy"],
    "difficulty": "hard",
    "time_complexity": "O(2^n)",
    "space_complexity": "O(n)",
    "description": "Find the minimum number of transactions required to settle all debts among a group of people.",
}

def solve(transactions: list[list[int]]) -> int:
    """
    Calculates the minimum number of transactions needed to settle all debts.

    Args:
        transactions: A list of transactions where each transaction is [from, to, amount].

    Returns:
        The minimum number of transactions required to zero out all balances.

    Examples:
        >>> solve([[0, 1, 10], [2, 0, 5]])
        2
        >>> solve([[0, 1, 10], [1, 2, 10], [2, 0, 10]])
        2
    """
    # Step 1: Calculate the net balance for each person.
    # A positive balance means the person is owed money.
    # A negative balance means the person owes money.
    net_balances_map: dict[int, int] = {}
    for sender, receiver, amount in transactions:
        net_balances_map[sender] = net_balances_map.get(sender, 0) - amount
        net_balances_map[receiver] = net_balances_map.get(receiver, 0) + amount

    # Step 2: Filter out people who already have a zero balance.
    # We only care about people with non-zero net balances.
    balances: list[int] = [val for val in net_balances_map.values() if val != 0]

    def backtrack(index: int) -> int:
        """
        Uses backtracking to find the minimum transfers needed starting from index.
        """
        # Base case: If we have processed all people, no more transfers needed.
        if index == len(balances):
            return 0

        # Skip people who have been zeroed out by previous transactions in the recursion.
        if balances[index] == 0:
            return backtrack(index + 1)

        min_transfers = float('inf')

        # Try to settle the current person's balance with every subsequent person.
        for next_person in range(index + 1, len(balances)):
            # Optimization: Only attempt to settle if the next person has an opposite sign.
            # This helps in finding a zero-sum match faster.
            if balances[next_person] * balances[index] < 0:
                # Perform the transaction: transfer the amount needed to zero out balances[index].
                balances[next_person] += balances[index]
                
                # Recurse to find the minimum transfers for the remaining people.
                res = 1 + backtrack(index + 1)
                min_transfers = min(min_transfers, res)
                
                # Backtrack: restore the balance for the next iteration.
                balances[next_person] -= balances[index]

        return int(min_transfers)

    return backtrack(0)
