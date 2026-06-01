METADATA = {
    "id": 2933,
    "name": "High-Access Employees",
    "slug": "high-access-employees",
    "category": "Hash Table",
    "aliases": [],
    "tags": ["hash_map", "array", "counting"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Identify employees who accessed the system more than a threshold number of times within a specific time window.",
}

def solve(access_logs: list[list[int]], threshold: int) -> list[list[int]]:
    """
    Finds employees who have accessed the system at least 'threshold' times.

    Args:
        access_logs: A list of lists where each sub-list contains [employee_id, timestamp].
        threshold: The minimum number of accesses required to be considered high-access.

    Returns:
        A list of lists where each sub-list contains [employee_id, access_count], 
        sorted by employee_id in ascending order.

    Examples:
        >>> solve([[1, 10], [2, 15], [1, 20], [1, 25], [2, 30]], 2)
        [[1, 3], [2, 2]]
        >>> solve([[1, 1], [2, 2], [3, 3]], 2)
        []
    """
    # Dictionary to store the frequency of each employee_id
    access_counts: dict[int, int] = {}

    # Iterate through the logs and increment the count for each employee
    for employee_id, timestamp in access_logs:
        access_counts[employee_id] = access_counts.get(employee_id, 0) + 1

    # Filter employees who meet or exceed the threshold
    high_access_employees: list[list[int]] = []
    for employee_id, count in access_counts.items():
        if count >= threshold:
            high_access_employees.append([employee_id, count])

    # Sort the result by employee_id as per problem requirements
    high_access_employees.sort()

    return high_access_employees
