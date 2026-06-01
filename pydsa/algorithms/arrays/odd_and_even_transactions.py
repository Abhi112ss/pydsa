METADATA = {
    "id": 3220,
    "name": "Odd and Even Transactions",
    "slug": "odd-and-even-transactions",
    "category": "Arrays",
    "aliases": [],
    "tags": ["arrays", "math"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Categorize transaction amounts into odd and even sums.",
}

def solve(transactions: list[int]) -> list[int]:
    """
    Calculates the sum of odd transactions and the sum of even transactions.

    Args:
        transactions: A list of integers representing transaction amounts.

    Returns:
        A list of two integers where the first element is the sum of odd 
        transactions and the second element is the sum of even transactions.

    Examples:
        >>> solve([1, 2, 3, 4, 5])
        [9, 6]
        >>> solve([10, 20, 30])
        [0, 60]
        >>> solve([1, 3, 5])
        [9, 0]
    """
    odd_sum = 0
    even_sum = 0

    for amount in transactions:
        # Check if the amount is even using the modulo operator
        if amount % 2 == 0:
            even_sum += amount
        else:
            # Otherwise, it is an odd transaction
            odd_sum += amount

    return [odd_sum, even_sum]
