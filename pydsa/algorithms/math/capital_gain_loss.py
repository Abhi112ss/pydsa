METADATA = {
    "id": 1393,
    "name": "Capital Gain/Loss",
    "slug": "capital-gain-loss",
    "category": "Math",
    "aliases": [],
    "tags": ["math", "logic", "hash-table"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Calculate the total capital gain or loss for each stock based on a list of transactions.",
}

def solve(transactions: list[list[str]]) -> list[list[str]]:
    """
    Calculates the total capital gain or loss for each stock.

    Args:
        transactions: A list of transactions where each transaction is 
            [stock_name, operation, price].

    Returns:
        A list of lists where each inner list contains [stock_name, total_gain_loss].
        The result is sorted by stock_name in ascending order.

    Examples:
        >>> solve([["Foo", "Buy", "10"], ["Bar", "Buy", "7"], ["Foo", "Sell", "15"]])
        [['Bar', '0'], ['Foo', '5']]
        >>> solve([["Foo", "Buy", "10"], ["Bar", "Buy", "7"], ["Foo", "Sell", "15"], ["Bar", "Sell", "10"]])
        [['Bar', '3'], ['Foo', '5']]
    """
    # Dictionary to store the running sum of gains/losses for each stock
    # Key: stock name (str), Value: cumulative gain/loss (int)
    stock_balances: dict[str, int] = {}

    for transaction in transactions:
        stock_name = transaction[0]
        operation = transaction[1]
        price = int(transaction[2])

        # Initialize stock in dictionary if not present
        if stock_name not in stock_balances:
            stock_balances[stock_name] = 0

        # If 'Buy', it's an outflow of money (negative)
        # If 'Sell', it's an inflow of money (positive)
        if operation == "Buy":
            stock_balances[stock_name] -= price
        else:
            stock_balances[stock_name] += price

    # Convert the dictionary to a list of [name, total_gain_loss]
    # We convert the integer back to a string to match the expected output format
    result: list[list[str]] = []
    for stock, balance in stock_balances.items():
        result.append([stock, str(balance)])

    # Sort the result alphabetically by stock name as required
    result.sort(key=lambda x: x[0])

    return result
