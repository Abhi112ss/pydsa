METADATA = {
    "id": 2701,
    "name": "Consecutive Transactions with Increasing Amounts",
    "slug": "consecutive-transactions-with-increasing-amounts",
    "category": "Array",
    "aliases": [],
    "tags": ["array", "iteration"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the maximum number of consecutive transactions where each transaction amount is strictly greater than the previous one.",
}

def solve(transactions: list[int]) -> int:
    """
    Finds the maximum length of a subarray where each element is strictly 
    greater than the previous element.

    Args:
        transactions: A list of integers representing transaction amounts.

    Returns:
        The length of the longest consecutive increasing sequence.

    Examples:
        >>> solve([1, 2, 3, 2, 5])
        3
        >>> solve([5, 4, 3, 2, 1])
        1
        >>> solve([1, 1, 1, 1])
        1
    """
    if not transactions:
        return 0

    max_streak = 1
    current_streak = 1

    # Iterate through the list starting from the second element
    for i in range(1, len(transactions)):
        # Check if the current transaction is strictly greater than the previous one
        if transactions[i] > transactions[i - 1]:
            current_streak += 1
        else:
            # Reset the streak if the increasing condition is broken
            current_streak = 1
        
        # Update the global maximum streak found so far
        if current_streak > max_streak:
            max_streak = current_streak

    return max_streak
