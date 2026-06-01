METADATA = {
    "id": 570,
    "name": "Managers with at Least 5 Direct Reports",
    "slug": "managers-with-at-least-5-direct-reports",
    "category": "Database",
    "aliases": [],
    "tags": ["sql", "math"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Find the names of managers who have at least five direct reports.",
}

from typing import List, Dict


class Employee:
    """Represents an employee record."""
    def __init__(self, id: int, name: str, manager_id: int):
        self.id = id
        self.name = name
        self.manager_id = manager_id


def solve(employees: List[Employee]) -> List[str]:
    """
    Finds the names of managers who have at least five direct reports.

    Args:
        employees: A list of Employee objects containing id, name, and manager_id.

    Returns:
        A list of names (strings) of managers who meet the criteria.

    Examples:
        >>> emp_list = [
        ...     Employee(1, "Joe", None),
        ...     Employee(2, "Henry", 1),
        ...     Employee(3, "Sam", 2),
        ...     Employee(4, "Max", 2),
        ...     Employee(5, "Janet", 2),
        ...     Employee(6, "Randy", 1),
        ...     Employee(7, "Will", 1),
        ...     Employee(8, "Janet", 1),
        ...     Employee(9, "Minerva", 1)
        ... ]
        >>> solve(emp_list)
        ['Joe']
    """
    # Map manager_id to the count of direct reports
    report_counts: Dict[int, int] = {}
    
    # Map employee_id to employee name for quick lookup
    id_to_name: Dict[int, str] = {}

    for emp in employees:
        id_to_name[emp.id] = emp.name
        if emp.manager_id is not None:
            # Increment the count for the manager associated with this employee
            report_counts[emp.manager_id] = report_counts.get(emp.manager_id, 0) + 1

    # Filter managers who have 5 or more reports and retrieve their names
    result_names: List[str] = []
    for manager_id, count in report_counts.items():
        if count >= 5:
            # Ensure the manager_id actually exists in our employee name map
            if manager_id in id_to_name:
                result_names.append(id_to_name[manager_id])

    return result_names
