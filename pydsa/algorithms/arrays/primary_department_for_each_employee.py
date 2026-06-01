METADATA = {
    "id": 1789,
    "name": "Primary Department for Each Employee",
    "slug": "primary_department_for_each_employee",
    "category": "Database",
    "aliases": [],
    "tags": ["sql", "hash_map"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Return each employee's primary department based on a flag or single assignment.",
}


def solve(employees: list[tuple[int, int, int]]) -> list[tuple[int, int]]:
    """Determine the primary department for each employee.

    Args:
        employees: A list of tuples where each tuple contains
            (employee_id, department_id, primary_flag). `primary_flag` is 1 if the
            department is marked as primary for that employee, otherwise 0.

    Returns:
        A list of tuples (employee_id, department_id) representing the primary
        department for each employee. The result is sorted by `employee_id` in
        ascending order.

    Examples:
        >>> data = [
        ...     (1, 10, 0),
        ...     (1, 20, 1),
        ...     (2, 30, 0),
        ... ]
        >>> solve(data)
        [(1, 20), (2, 30)]

        >>> data = [(3, 40, 0)]
        >>> solve(data)
        [(3, 40)]
    """
    # Map each employee to its candidate primary department.
    primary_by_employee: dict[int, int] = {}

    for employee_id, department_id, primary_flag in employees:
        if primary_flag == 1:
            # Directly store the explicitly marked primary department.
            primary_by_employee[employee_id] = department_id
        else:
            # If we haven't seen a primary yet, store the department as a fallback.
            # This handles the case where the employee belongs to only one department.
            if employee_id not in primary_by_employee:
                primary_by_employee[employee_id] = department_id

    # Produce sorted result list.
    result: list[tuple[int, int]] = sorted(primary_by_employee.items())
    return result