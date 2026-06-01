METADATA = {
    "id": 1270,
    "name": "All People Report to the Given Manager",
    "slug": "all-people-report-to-the-given-manager",
    "category": "Database/Logic",
    "aliases": [],
    "tags": ["recursion", "logic", "graph"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Find all employees who report to a specific manager, including indirect reports through a hierarchy.",
}

def solve(manager_id: int, reports: list[tuple[int, int]]) -> list[int]:
    """
    Finds all employees who report to a given manager, including indirect reports.

    Args:
        manager_id: The ID of the manager to start the search from.
        reports: A list of tuples where each tuple is (employee_id, manager_id).

    Returns:
        A sorted list of employee IDs who report to the given manager.

    Examples:
        >>> solve(1, [(1, 3), (2, 3), (3, 1)])
        [1, 2, 3]
        >>> solve(3, [(1, 3), (2, 3), (3, 1)])
        [1, 2]
    """
    # Build an adjacency list representing the management hierarchy
    # Key: Manager ID, Value: List of direct reports
    hierarchy: dict[int, list[int]] = {}
    for emp_id, mgr_id in reports:
        if mgr_id not in hierarchy:
            hierarchy[mgr_id] = []
        hierarchy[mgr_id].append(emp_id)

    result_set: set[int] = set()
    # We use a stack for an iterative Depth First Search (DFS) to find all descendants
    # We start with the manager_id itself because the problem implies the manager 
    # is part of the reporting chain if they are in the hierarchy.
    stack: list[int] = [manager_id]

    while stack:
        current_manager = stack.pop()
        
        # If the current person manages anyone, add them to the result and 
        # add their direct reports to the stack to explore further down the tree
        if current_manager in hierarchy:
            for report_id in hierarchy[current_manager]:
                if report_id not in result_set:
                    result_set.add(report_id)
                    stack.append(report_id)

    # The problem asks for all people who report to the manager.
    # In the context of LeetCode 1270 (SQL version), it usually implies 
    # finding all employees in the hierarchy tree rooted at manager_id.
    # We return the sorted list of IDs found.
    return sorted(list(result_set))
