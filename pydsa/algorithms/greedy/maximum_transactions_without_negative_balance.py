METADATA = {
    "id": 3711,
    "name": "Maximum Transactions Without Negative Balance",
    "slug": "maximum_transactions_without_negative_balance",
    "category": "Greedy",
    "aliases": [],
    "tags": ["greedy", "sorting", "priority queue"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Find the maximum number of transactions one can perform such that the running balance never drops below zero.",
}

import heapq

def solve(transactions: list[int]) -> int:
    """
    Calculates the maximum number of transactions possible without the balance dropping below zero.
    
    The algorithm uses a greedy approach with a priority queue (min-heap) to perform 
    backtracking. We process transactions one by one. If a transaction causes the 
    balance to become negative, we "undo" the most negative transaction encountered 
    so far to restore the balance.

    Args:
        transactions: A list of integers representing transaction amounts (positive or negative).

    Returns:
        The maximum number of transactions that can be completed.

    Examples:
        >>> solve([10, -5, -10, 5, -2])
        4
        >>> solve([-1, -2, -3])
        0
        >>> solve([5, 5, -10, 5])
        3
    """
    current_balance = 0
    # min_heap stores the negative transactions we have accepted so far.
    # This allows us to identify the "worst" transaction to remove if we hit a deficit.
    negative_transactions_heap = []
    count = 0

    for amount in transactions:
        # If it's a positive transaction, it always helps the balance.
        if amount >= 0:
            current_balance += amount
            count += 1
        else:
            # If it's a negative transaction, tentatively accept it.
            current_balance += amount
            count += 1
            heapq.heappush(negative_transactions_heap, amount)

            # If the balance drops below zero, we must backtrack.
            # We remove the most negative transaction we've accepted to maximize the balance.
            if current_balance < 0:
                if negative_transactions_heap:
                    # Pop the smallest (most negative) value.
                    worst_transaction = heapq.heappop(negative_transactions_heap)
                    current_balance -= worst_transaction
                    count -= 1

    return count
