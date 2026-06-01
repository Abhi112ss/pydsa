METADATA = {
    "id": 2066,
    "name": "Account Balance",
    "slug": "account-balance",
    "category": "Simulation",
    "aliases": [],
    "tags": ["simulation", "array"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Calculate the final account balance by summing all transaction amounts in a list.",
}

def solve(transactions: list[int]) -> int:
    """
    Calculates the final account balance after a series of transactions.

    Args:
        transactions: A list of integers representing transaction amounts. 
                      Positive values are deposits, negative values are withdrawals.

    Returns:
        The final balance after all transactions have been processed.

    Examples:
        >>> solve([10, -5, 20, -10])
        15
        >>> solve([-5, -5, -5])
        -15
        >>> solve([])
        0
    """
    current_balance = 0
    
    # Iterate through each transaction and update the running total
    for amount in transactions:
        current_balance += amount
        
    return current_balance
