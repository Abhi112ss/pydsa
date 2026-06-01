METADATA = {
    "id": 1555,
    "name": "Bank Account Summary",
    "slug": "bank-account-summary",
    "category": "Array",
    "aliases": [],
    "tags": ["arrays", "sorting"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Calculate the sum of the top k largest transactions for a bank account.",
}

def solve(transactions: list[int], k: int) -> int:
    """
    Args:
        transactions: A list of integers representing transaction amounts.
        k: The number of largest transactions to sum.

    Returns:
        The sum of the k largest transaction amounts.
    """
    sorted_transactions = sorted(transactions, reverse=True)
    return sum(sorted_transactions[:k])