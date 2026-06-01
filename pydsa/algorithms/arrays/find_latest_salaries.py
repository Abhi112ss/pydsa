METADATA = {
    "id": 2668,
    "name": "Find Latest Salaries",
    "slug": "find_latest_salaries",
    "category": "Database",
    "aliases": [],
    "tags": ["hash_map", "sql"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Return each employee's most recent salary based on timestamp records.",
}


def solve(records: list[list[int]]) -> list[list[int]]:
    """Return the latest salary for each employee.

    Args:
        records: A list where each element is a list of three integers
            [employee_id, salary, changed_at]. `changed_at` represents the
            timestamp when the salary was recorded.

    Returns:
        A list of lists, each containing [employee_id, latest_salary].
        The result is sorted by `employee_id` in ascending order.

    Examples:
        >>> solve([[1, 100, 10], [2, 200, 5], [1, 150, 20]])
        [[1, 150], [2, 200]]
        >>> solve([[3, 300, 1], [3, 350, 2], [2, 400, 3]])
        [[2, 400], [3, 350]]
    """
    # Map each employee_id to a tuple (latest_timestamp, salary_at_that_timestamp)
    latest_by_employee: dict[int, tuple[int, int]] = {}

    for employee_id, salary, changed_at in records:
        # If we have not seen this employee or found a newer timestamp, update the map
        if (employee_id not in latest_by_employee) or (changed_at > latest_by_employee[employee_id][0]):
            latest_by_employee[employee_id] = (changed_at, salary)

    # Build the result list and sort by employee_id for deterministic output
    result: list[list[int]] = [
        [employee_id, salary] for employee_id, ( _, salary) in latest_by_employee.items()
    ]
    result.sort(key=lambda pair: pair[0])
    return result