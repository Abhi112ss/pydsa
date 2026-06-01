METADATA = {
    "id": 2988,
    "name": "Manager of the Largest Department",
    "slug": "manager_of_the_largest_department",
    "category": "Hash Table",
    "aliases": [],
    "tags": ["hash_map", "frequency_count", "array"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Find the manager of the department that has the largest number of employees.",
}

def solve(employees: list[list[int]]) -> int:
    """
    Finds the manager of the department with the largest number of employees.

    Args:
        employees: A list of lists where each sub-list represents an employee.
                   Format: [employee_id, manager_id, department_id]
                   Note: manager_id can be -1 if the employee has no manager.

    Returns:
        The manager_id of the largest department. If multiple departments have 
        the same maximum size, the problem context usually implies returning 
        the first one encountered or follows specific tie-breaking rules. 
        Based on the prompt, we return the manager of the largest department.

    Examples:
        >>> solve([[1, -1, 10], [2, 1, 10], [3, 1, 10], [4, 2, 20]])
        1
        >>> solve([[1, -1, 1], [2, 1, 1], [3, 1, 1], [4, -1, 2], [5, 4, 2]])
        1
    """
    if not employees:
        return -1

    # department_counts maps department_id -> number of employees in that department
    department_counts: dict[int, int] = {}
    # dept_to_manager maps department_id -> manager_id of that department
    # We assume the manager is the person with manager_id -1 in that department
    # or we need to identify the manager based on the department structure.
    # In standard LeetCode problems of this type, the manager is often 
    # the one whose ID is used to manage others in that specific department.
    # However, the prompt implies we just need to find the manager of the largest dept.
    # Let's track the manager for each department.
    dept_to_manager: dict[int, int] = {}

    for emp_id, manager_id, dept_id in employees:
        # Increment the count for the current department
        department_counts[dept_id] = department_counts.get(dept_id, 0) + 1
        
        # If this employee is a top-level manager (manager_id == -1), 
        # they are the manager of this department.
        if manager_id == -1:
            dept_to_manager[dept_id] = emp_id

    max_size = 0
    result_manager = -1

    # Iterate through the departments to find the one with the maximum size
    for dept_id, count in department_counts.items():
        if count > max_size:
            max_size = count
            # Retrieve the manager associated with this department
            result_manager = dept_to_manager.get(dept_id, -1)
        elif count == max_size:
            # Tie-breaking logic: if needed, could be handled here.
            # For this implementation, we keep the first one found.
            pass

    return result_manager
