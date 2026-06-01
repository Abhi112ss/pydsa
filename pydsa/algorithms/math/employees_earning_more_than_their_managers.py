METADATA = {
    "id": 181,
    "name": "Employees Earning More Than Their Managers",
    "slug": "employees-earning-more-than-their-managers",
    "category": "Database",
    "aliases": [],
    "tags": ["sql", "join"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Find employees who earn more than their direct managers using a self-join approach.",
}

def solve(employee_table: list[dict[str, int]]) -> list[str]:
    """
    Args:
        employee_table: A list of dictionaries where each dictionary represents an employee 
                        with keys 'id', 'name', 'salary', and 'managerId'.

    Returns:
        A list of names of employees who earn more than their managers.
    """
    employee_map = {emp["id"]: emp for emp in employee_table}
    result_names = []

    for emp in employee_table:
        manager_id = emp.get("managerId")
        if manager_id is not None and manager_id in employee_map:
            manager = employee_map[manager_id]
            if emp["salary"] > manager["salary"]:
                result_names.append(emp["name"])

    return result_names