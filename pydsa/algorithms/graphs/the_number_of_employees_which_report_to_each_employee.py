METADATA = {
    "id": 1731,
    "name": "The Number of Employees Which Report to Each Employee",
    "slug": "the-number-of-employees-which-report-to-each-employee",
    "category": "Hash Table",
    "aliases": [],
    "tags": ["hash_map", "graphs", "tree"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Calculate the total number of reports (direct and indirect) for each manager in a company hierarchy.",
}

def solve(manager_id: list[int], reports: list[list[int]]) -> list[list[int]]:
    """
    Calculates the total number of reports for each manager.

    Args:
        manager_id: A list where manager_id[i] is the manager of employee i.
        reports: A list of pairs [manager_id, employee_id].

    Returns:
        A list of lists where each sublist contains [manager_id, total_reports_count],
        sorted by manager_id in ascending order.

    Examples:
        >>> solve([0, 0, 0, 1, 1, 2, 2], [[0, 1], [0, 2], [0, 3], [1, 4], [1, 5], [2, 6]])
        [[0, 6], [1, 2], [2, 1]]
    """
    from collections import defaultdict

    # adjacency_list maps a manager to their direct reports
    adjacency_list = defaultdict(list)
    # all_managers tracks every ID that acts as a manager at any level
    all_managers = set()

    for manager, employee in reports:
        adjacency_list[manager].append(employee)
        all_managers.add(manager)

    # memoization dictionary to store total reports for each manager
    memo = {}

    def count_reports(current_manager: int) -> int:
        """Helper function to perform DFS and count all descendants."""
        if current_manager in memo:
            return memo[current_manager]
        
        total_count = 0
        # Traverse all direct reports of the current manager
        for report in adjacency_list[current_manager]:
            # 1 for the direct report + all of their own reports
            total_count += 1 + count_reports(report)
        
        memo[current_manager] = total_count
        return total_count

    # Calculate reports for every manager identified in the hierarchy
    results = []
    for manager in sorted(list(all_managers)):
        results.append([manager, count_reports(manager)])

    return results
