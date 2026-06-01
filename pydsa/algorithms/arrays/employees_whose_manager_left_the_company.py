METADATA = {
    "id": 1978,
    "name": "Employees Whose Manager Left the Company",
    "slug": "employees-whose-manager-left-the-company",
    "category": "Array",
    "aliases": [],
    "tags": ["hash_map", "arrays"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Find the IDs of employees whose managers are no longer in the employee table.",
}

def solve(employee: list[list[int]]) -> list[int]:
    """
    Identifies employees whose manager is not present in the employee list.

    Args:
        employee: A list of lists where each sub-list contains [employee_id, manager_id].

    Returns:
        A list of employee IDs whose manager_id does not exist in the set of all employee_ids,
        sorted in ascending order.

    Examples:
        >>> solve([[0, 1], [1, 2], [2, 3]])
        [0]
        >>> solve([[0, 1], [1, 2], [2, 0]])
        []
        >>> solve([[0, 1], [1, 3], [2, 3], [3, 0]])
        [1, 2]
    """
    # Create a set of all existing employee IDs for O(1) lookup
    existing_employee_ids = {emp_info[0] for emp_info in employee}
    
    result_ids = []
    
    for emp_id, manager_id in employee:
        # If the manager_id is not in the set of existing employees, 
        # it means the manager has left the company.
        if manager_id not in existing_employee_ids:
            result_ids.append(emp_id)
            
    # The problem requires the result to be sorted in ascending order
    result_ids.sort()
    
    return result_ids
