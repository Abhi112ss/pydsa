METADATA = {
    "id": 2432,
    "name": "The Employee That Worked on the Longest Task",
    "slug": "the_employee_that_worked_on_the_longest_task",
    "category": "Hash Table",
    "aliases": [],
    "tags": ["hash_map", "sorting"],
    "difficulty": "easy",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Find the employee with the greatest total task duration.",
}


def solve(tasks: list[list[int]]) -> int:
    """Return the employee ID that worked on the longest total task time.

    Args:
        tasks: A list where each element is a list of three integers
            [employee_id, start_time, end_time].

    Returns:
        The employee ID with the maximum total duration. If multiple employees
        have the same total duration, the smallest employee ID is returned.

    Examples:
        >>> solve([[1, 1, 3], [2, 2, 5], [1, 4, 6]])
        1
        >>> solve([[3, 2, 4], [3, 5, 7], [2, 1, 3]])
        3
    """
    # Aggregate total duration per employee using a hash map.
    total_time_by_employee: dict[int, int] = {}
    for employee_id, start_time, end_time in tasks:
        duration = end_time - start_time
        total_time_by_employee[employee_id] = total_time_by_employee.get(employee_id, 0) + duration

    # Convert to a list of (employee_id, total_time) pairs and sort:
    #   - primary key: descending total_time
    #   - secondary key: ascending employee_id (to break ties)
    aggregated_list = list(total_time_by_employee.items())
    aggregated_list.sort(key=lambda pair: (-pair[1], pair[0]))

    # The first element after sorting holds the desired employee ID.
    return aggregated_list[0][0] if aggregated_list else -1