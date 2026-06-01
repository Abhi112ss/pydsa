METADATA = {
    "id": 185,
    "name": "Department Top Three Salaries",
    "slug": "department_top_three_salaries",
    "category": "Database",
    "aliases": ["Top 3 Salaries"],
    "tags": ["sql", "window_function", "sorting"],
    "difficulty": "hard",
    "time_complexity": "O(N log N)",
    "space_complexity": "O(N)",
    "description": "Find employees who earn one of the top three unique salaries in each department.",
}


def solve(employees: list[dict], departments: list[dict]) -> list[dict]:
    """
    Finds employees who earn one of the top three unique salaries in each department.

    Args:
        employees: A list of dictionaries containing 'id', 'name', 'salary', and 'departmentId'.
        departments: A list of dictionaries containing 'id' and 'name'.

    Returns:
        A list of dictionaries containing 'Department', 'Employee', and 'Salary'.

    Examples:
        >>> employees = [
        ...     {'id': 1, 'name': 'Joe', 'salary': 85000, 'departmentId': 1},
        ...     {'id': 2, 'name': 'Henry', 'salary': 80000, 'departmentId': 2},
        ...     {'id': 3, 'name': 'Sam', 'salary': 60000, 'departmentId': 2},
        ...     {'id': 4, 'name': 'Max', 'salary': 90000, 'departmentId': 1},
        ...     {'id': 5, 'name': 'Janet', 'salary': 69000, 'departmentId': 1},
        ...     {'id': 6, 'name': 'Randy', 'salary': 85000, 'departmentId': 1},
        ...     {'id': 7, 'name': 'Will', 'salary': 70000, 'departmentId': 1}
        ... ]
        >>> departments = [{'id': 1, 'name': 'IT'}, {'id': 2, 'name': 'Sales'}]
        >>> solve(employees, departments)
        [{'Department': 'IT', 'Employee': 'Max', 'Salary': 90000}, ...]
    """
    # Map department IDs to their names for quick lookup
    dept_map = {dept['id']: dept['name'] for dept in departments}

    # Group employees by their department ID
    dept_groups = {}
    for emp in employees:
        dept_id = emp['departmentId']
        if dept_id not in dept_groups:
            dept_groups[dept_id] = []
        dept_groups[dept_id].append(emp)

    result = []

    for dept_id, group in dept_groups.items():
        if dept_id not in dept_map:
            continue
        
        dept_name = dept_map[dept_id]
        
        # Identify unique salaries in the department and sort them descending
        unique_salaries = sorted(list(set(emp['salary'] for emp in group)), reverse=True)
        
        # Determine the threshold for the top 3 unique salaries
        # If there are fewer than 3 unique salaries, all are included
        top_three_threshold = unique_salaries[:3]
        salary_set = set(top_three_threshold)

        # Filter employees whose salary is within the top three unique salaries
        for emp in group:
            if emp['salary'] in salary_set:
                result.append({
                    "Department": dept_name,
                    "Employee": emp['name'],
                    "Salary": emp['salary']
                })

    return result