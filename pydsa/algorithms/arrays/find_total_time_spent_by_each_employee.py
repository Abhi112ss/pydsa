METADATA = {
    "id": 1741,
    "name": "Find Total Time Spent by Each Employee",
    "slug": "find-total-time-spent-by-each-employee",
    "category": "Array",
    "aliases": [],
    "tags": ["array", "prefix_sum"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(m)",
    "description": "Calculate the total time spent by each employee by summing the durations of their work intervals.",
}

def solve(n: int, intervals: list[list[int]]) -> list[int]:
    """
    Calculates the total time spent by each employee based on their work intervals.

    Args:
        n (int): The number of employees.
        intervals (list[list[int]]): A list of intervals where each interval is [employee_id, start_time, end_time].

    Returns:
        list[int]: A list of size n where the i-th element is the total time spent by employee i.

    Examples:
        >>> solve(3, [[0, 1, 2], [1, 2, 3], [0, 3, 4]])
        [2, 1, 0]
        >>> solve(2, [[0, 0, 5], [1, 5, 10], [0, 10, 15]])
        [10, 5]
    """
    # Initialize a result array of size n with zeros to store accumulated time
    total_time_spent = [0] * n

    for employee_id, start_time, end_time in intervals:
        # Calculate the duration of the current interval
        duration = end_time - start_time
        
        # Accumulate the duration into the corresponding employee's index
        total_time_spent[employee_id] += duration

    return total_time_spent
