METADATA = {
    "id": 2082,
    "name": "The Number of Rich Customers",
    "slug": "the-number-of-rich-customers",
    "category": "Array",
    "aliases": [],
    "tags": ["array", "counting"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Count how many customers have a balance greater than or equal to a given threshold.",
}

def solve(customers: list[int], threshold: int) -> int:
    """
    Counts the number of customers whose balance is at least the threshold.

    Args:
        customers: A list of integers representing the balances of customers.
        threshold: An integer representing the minimum balance required to be 'rich'.

    Returns:
        The total count of customers with a balance >= threshold.

    Examples:
        >>> solve([1, 5, 10, 15], 10)
        2
        >>> solve([1, 2, 3], 5)
        0
        >>> solve([10, 10, 10], 10)
        3
    """
    rich_customer_count = 0
    
    # Iterate through each customer's balance in the list
    for balance in customers:
        # Check if the current balance meets or exceeds the threshold
        if balance >= threshold:
            rich_customer_count += 1
            
    return rich_customer_count
