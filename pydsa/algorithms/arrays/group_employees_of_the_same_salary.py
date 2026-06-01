METADATA = {
    "id": 1875,
    "name": "Group Employees of the Same Salary",
    "slug": "group-employees-of-the-same-salary",
    "category": "Hash Table",
    "aliases": [],
    "tags": ["hash_map", "sorting"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Group employee IDs by their salary and return them in descending order of salary.",
}

def solve(employee_id: list[int], salary: list[int]) -> list[list[int]]:
    """
    Groups employee IDs by their salary and returns a list of lists, 
    where each inner list contains IDs with the same salary, 
    sorted by salary in descending order.

    Args:
        employee_id: A list of integers representing employee IDs.
        salary: A list of integers representing the salary of the corresponding employee.

    Returns:
        A list of lists of integers, where each sub-list contains IDs 
        sharing a salary, ordered by salary descending.

    Examples:
        >>> solve([1, 2, 3, 4, 5], [10, 20, 10, 30, 20])
        [[4], [2, 5], [1, 3]]
        >>> solve([1, 2, 3], [10, 10, 10])
        [[1, 2, 3]]
    """
    # Map to store salary as key and a list of employee IDs as value
    salary_to_ids: dict[int, list[int]] = {}

    # Populate the hash map
    for emp_id, emp_salary in zip(employee_id, salary):
        if emp_salary not in salary_to_ids:
            salary_to_ids[emp_salary] = []
        salary_to_ids[emp_salary].append(emp_id)

    # Extract unique salaries and sort them in descending order
    sorted_salaries = sorted(salary_to_ids.keys(), reverse=True)

    # Construct the result list based on the sorted salaries
    result: list[list[int]] = []
    for s in sorted_salaries:
        result.append(salary_to_ids[s])

    return result
