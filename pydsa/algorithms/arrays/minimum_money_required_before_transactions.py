METADATA = {
    "id": 2412,
    "name": "Minimum Money Required Before Transactions",
    "slug": "minimum-money-required-before-transactions",
    "category": "Array",
    "aliases": [],
    "tags": ["arrays", "prefix_sum"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the minimum initial amount of money needed to ensure the balance never drops below zero during a series of transactions.",
}

def solve(transactions: list[int]) -> int:
    """
    Calculates the minimum initial amount of money required to cover all transactions.

    The problem asks for the minimum starting balance such that the running balance
    never becomes negative. This is equivalent to finding the most negative point
    reached by the prefix sum of the transactions.

    Args:
        transactions: A list of integers representing money gained (positive) 
            or lost (negative).

    Returns:
        The minimum initial amount of money required.

    Examples:
        >>> solve([1, -3, 4, -5, 2])
        4
        >>> solve([-1, -2, -3])
        6
        >>> solve([1, 2, 3])
        0
    """
    current_balance = 0
    min_balance = 0

    for amount in transactions:
        # Update the running balance with the current transaction
        current_balance += amount
        
        # Track the lowest point the balance reaches during the sequence
        if current_balance < min_balance:
            min_balance = current_balance

    # If the minimum balance is negative (e.g., -4), we need 4 to stay at 0.
    # If the minimum balance is 0 or positive, we need 0 initial money.
    return abs(min_balance)
