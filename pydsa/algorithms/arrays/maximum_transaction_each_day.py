METADATA = {
    "id": 1831,
    "name": "Maximum Transaction Each Day",
    "slug": "maximum-transaction-each-day",
    "category": "Hash Table",
    "aliases": [],
    "tags": ["hash_map", "arrays", "sorting"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Find the maximum transaction amount for each day given a list of transactions containing amounts and timestamps.",
}

def solve(transactions: list[list[int]]) -> list[int]:
    """
    Finds the maximum transaction amount for each unique day.

    Args:
        transactions: A list of transactions where each transaction is [amount, timestamp].
            The timestamp is in seconds. A day is defined as 86400 seconds.
            The day index is calculated as floor(timestamp / 86400).

    Returns:
        A list of integers representing the maximum transaction amount for each day,
        sorted by day index.

    Examples:
        >>> solve([[100, 0], [200, 10], [50, 86400], [300, 90000]])
        [200, 300]
        >>> solve([[10, 0], [20, 86400], [30, 172800]])
        [10, 20, 30]
    """
    # Constants
    SECONDS_IN_A_DAY = 86400
    
    # Dictionary to store the maximum amount found for each day index
    # Key: day_index (timestamp // 86400), Value: max_amount
    max_amounts_by_day: dict[int, int] = {}

    for amount, timestamp in transactions:
        # Calculate the day index based on the timestamp
        day_index = timestamp // SECONDS_IN_A_DAY
        
        # Update the maximum amount for the current day
        if day_index not in max_amounts_by_day or amount > max_amounts_by_day[day_index]:
            max_amounts_by_day[day_index] = amount

    # Extract the day indices and sort them to ensure the result is in chronological order
    sorted_days = sorted(max_amounts_by_day.keys())
    
    # Construct the result list using the sorted day indices
    result = [max_amounts_by_day[day] for day in sorted_days]
    
    return result
