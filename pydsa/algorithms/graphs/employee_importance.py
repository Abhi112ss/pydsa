METADATA = {
    "id": 690,
    "name": "Employee Importance",
    "slug": "employee-importance",
    "category": "Graph",
    "aliases": [],
    "tags": ["dfs", "bfs", "hash_map"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Calculate the total importance of an employee by summing their importance and the importance of all their direct and indirect subordinates.",
}

class Employee:
    def __init__(self, id: int, name: str, importance: int, directReports: list[int]):
        self.id = id
        self.name = name
        self.importance = importance
        self.directReports = directReports

def solve(employees: list[Employee], id: int) -> int:
    """
    Calculates the total importance of an employee and all their subordinates.

    Args:
        employees: A list of Employee objects.
        id: The ID of the employee to start the calculation from.

    Returns:
        The sum of importance values for the given employee and all subordinates.

    Examples:
        >>> employees = [
        ...     Employee(1, "Miss", 150, [2, 3]),
        ...     Employee(2, "John", 90, [4]),
        ...     Employee(3, "Alice", 80, []),
        ...     Employee(4, "Bob", 60, [])
        ... ]
        >>> solve(employees, 1)
        380
    """
    # Map employee ID to the Employee object for O(1) lookup
    employee_map: dict[int, Employee] = {emp.id: emp for emp in employees}
    
    if id not in employee_map:
        return 0

    total_importance = 0
    # Use a stack for iterative Depth First Search (DFS)
    stack: list[int] = [id]

    while stack:
        current_id = stack.pop()
        current_employee = employee_map[current_id]
        
        # Add current employee's importance to the running total
        total_importance += current_employee.importance
        
        # Add all direct reports to the stack to traverse the hierarchy
        for report_id in current_employee.directReports:
            stack.append(report_id)

    return total_importance
