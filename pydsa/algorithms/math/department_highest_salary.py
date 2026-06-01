METADATA = {
    "id": 184,
    "name": "Department Highest Salary",
    "slug": "department_highest_salary",
    "category": "database",
    "aliases": ["Highest Salary in Department"],
    "tags": ["sql", "group_by", "join"],
    "difficulty": "medium",
    "time_complexity": "O(N + M)",
    "space_complexity": "O(N + M)",
    "description": "Find employees who have the highest salary in each of the departments.",
}


def solve(employees: list[dict], departments: list[dict]) -> list[dict]:
    """
    Finds employees who have the highest salary in each department.

    Args:
        employees: A list of dictionaries containing 'id', 'name', 'salary', and 'departmentId'.
        departments: A list of dictionaries containing 'id' and 'name'.

    Returns:
        A list of dictionaries containing 'Department', 'Employee', and 'Salary'.

    Examples:
        >>> employees = [{'id': 1, 'name': 'Joe', 'salary': 70000, 'departmentId': 1},
        ...              {'id': 2, 'name': 'Jim', 'salary': 90000, 'departmentId': 1}]
        >>> departments = [{'id': 1, 'name': 'IT'}]
        >>> solve(employees, departments)
        [{'Department': 'IT', 'Employee': 'Jim', 'Salary': 90000}]
    """
    # Create a mapping from department ID to department name for quick lookup
    department_lookup = {dept['id']: dept['name'] for dept in departments}

    # Find the maximum salary for each department
    # Key: departmentId, Value: max salary found so far
    max_salary_per_dept = {}
    for emp in employees:
        dept_id = emp['departmentId']
        salary = emp['salary']
        if dept_id not in max_salary_per_dept or salary > max_salary_per_dept[dept_id]:
            max_salary_per_dept[dept_id] = salary

    # Filter employees who match the maximum salary in their respective department
    result = []
    for emp in employees:
        dept_id = emp['departmentId']
        # Ensure the department exists in our lookup and the salary matches the max
        if dept_id in max_salary_per_dept and emp['salary'] == max_salary_per_dept[dept_id]:
            result.append({
                "Department": department_lookup.get(dept_id, "Unknown"),
                "Employee": emp['name'],
                "Salary": emp['salary']
            })

    return result