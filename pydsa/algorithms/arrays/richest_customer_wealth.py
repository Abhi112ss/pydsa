METADATA = {
    "id": 1672,
    "name": "Richest Customer Wealth",
    "slug": "richest-customer-wealth",
    "category": "Arrays",
    "aliases": [],
    "tags": ["array", "matrix"],
    "difficulty": "easy",
    "time_complexity": "O(m * n)",
    "space_complexity": "O(1)",
    "description": "Find the maximum wealth among all customers where wealth is the sum of their bank accounts.",
}

def solve(accounts: list[list[int]]) -> int:
    """
    Calculates the maximum wealth among all customers.

    Args:
        accounts: A 2D list where accounts[i][j] is the amount of money 
            the i-th customer has in the j-th bank.

    Returns:
        The maximum total wealth found among all customers.

    Examples:
        >>> solve([[1, 2, 3], [3, 2, 1]])
        6
        >>> solve([[1, 1], [1, 1], [1, 1]])
        2
    """
    max_wealth = 0

    for customer_accounts in accounts:
        # Calculate the total wealth for the current customer
        current_customer_wealth = sum(customer_accounts)
        
        # Update max_wealth if the current customer is richer
        if current_customer_wealth > max_wealth:
            max_wealth = current_customer_wealth

    return max_wealth
