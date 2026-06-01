METADATA = {
    "id": 1076,
    "name": "Project Employees II",
    "slug": "project_employees_ii",
    "category": "Database",
    "aliases": [],
    "tags": ["math", "arrays"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Return project IDs with the maximum number of employees.",
}


def solve(project_employee: list[list[int]]) -> list[int]:
    """Find project IDs that have the maximum number of employees.

    Args:
        project_employee: A list of [project_id, employee_id] pairs representing
            assignments of employees to projects.

    Returns:
        A sorted list of project IDs that have the highest employee count.

    Examples:
        >>> solve([[1, 1], [1, 2], [2, 3], [2, 4], [2, 5]])
        [2]
        >>> solve([[1, 1], [2, 2], [3, 3]])
        [1, 2, 3]
    """
    # Count employees per project
    employee_counts: dict[int, int] = {}
    for project_id, _ in project_employee:
        employee_counts[project_id] = employee_counts.get(project_id, 0) + 1

    if not employee_counts:
        return []

    # Determine the maximum employee count
    max_count = max(employee_counts.values())

    # Collect all project IDs with the maximum count and sort them
    result = [project_id for project_id, count in employee_counts.items() if count == max_count]
    result.sort()
    return result