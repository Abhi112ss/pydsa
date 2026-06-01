METADATA = {
    "id": 2224,
    "name": "Minimum Number of Operations to Convert Time",
    "slug": "minimum_number_of_operations_to_convert_time",
    "category": "greedy",
    "aliases": [],
    "tags": ["greedy", "math"],
    "difficulty": "medium",
    "time_complexity": "O(1)",
    "space_complexity": "O(1)",
    "description": "Compute the minimum number of operations to convert one time to another using greedy extraction of hour and minute units.",
}

import sys

def solve() -> None:
    """Read two time strings and output the minimum number of operations.

    Args:
        None (reads from standard input).

    Returns:
        None (writes the result to standard output).

    Examples:
        >>> # Input format: current_time correct_time
        >>> # Example:
        >>> # 02:30
        >>> # 04:35
        >>> # Output: 3
        >>> # Explanation: add 60 minutes (1 hour) -> 03:30,
        >>> # add 60 minutes (1 hour) -> 04:30,
        >>> # add 5 minutes -> 04:35.
    """
    data = [line.strip() for line in sys.stdin if line.strip()]
    if len(data) < 2:
        return
    current_time = data[0]
    correct_time = data[1]

    # Convert HH:MM to total minutes since midnight
    current_hours, current_minutes = map(int, current_time.split(":"))
    correct_hours, correct_minutes = map(int, correct_time.split(":"))
    current_total = current_hours * 60 + current_minutes
    correct_total = correct_hours * 60 + correct_minutes

    # Compute forward difference, wrapping around midnight if needed
    if correct_total >= current_total:
        minute_difference = correct_total - current_total
    else:
        minute_difference = (24 * 60 - current_total) + correct_total

    # Greedy extraction using the largest possible operation units
    operation_counts = 0
    for unit in (60, 15, 5, 1):
        operation_counts += minute_difference // unit
        minute_difference %= unit

    print(operation_counts)
