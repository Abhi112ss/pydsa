METADATA = {
    "id": 2806,
    "name": "Account Balance After Rounded Purchase",
    "slug": "account-balance-after-rounded-purchase",
    "category": "Math",
    "aliases": [],
    "tags": ["math", "simulation"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Calculate the final account balance after applying specific rounding rules to each transaction.",
}

def solve(initial_balance: int, transactions: list[int]) -> int:
    """
    Calculates the final account balance after applying rounding rules to each transaction.

    The rounding rules for each transaction amount are:
    - If the amount is divisible by 10, it remains unchanged.
    - If the amount is not divisible by 10, it is rounded to the nearest 10.
    - If the amount ends in 5, it is rounded up to the next 10.

    Args:
        initial_balance: The starting amount of money in the account.
        transactions: A list of integers representing the purchase amounts.

    Returns:
        The final balance after all transactions are processed.

    Examples:
        >>> solve(10, [11, 15, 20])
        -30
        >>> solve(100, [10, 25, 30])
        40
    """
    current_balance = initial_balance

    for amount in transactions:
        # Calculate the remainder when divided by 10 to determine rounding
        remainder = amount % 10
        
        if remainder == 0:
            # Already a multiple of 10, no change needed
            rounded_amount = amount
        else:
            # Rounding logic: 
            # If remainder is 5 or more, round up.
            # Otherwise, round down.
            # This can be simplified by adding 5 and then performing integer division by 10.
            rounded_amount = ((amount + 5) // 10) * 10
            
        current_balance -= rounded_amount

    return current_balance
