METADATA = {
    "id": 3338,
    "name": "Second Highest Salary II",
    "slug": "second-highest-salary-ii",
    "category": "SQL",
    "aliases": [],
    "tags": ["sql", "database"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the second highest distinct salary from a table, returning None if it does not exist.",
}

from typing import Optional, List, Dict, Any


def solve(employee_data: List[Dict[str, Any]]) -> Optional[int]:
    """
    Finds the second highest distinct salary from a list of employee records.

    Args:
        employee_data: A list of dictionaries where each dictionary represents 
            an employee and contains a 'salary' key.

    Returns:
        The second highest distinct salary as an integer, or None if no 
        second highest salary exists.

    Examples:
        >>> solve([{"salary": 100}, {"salary": 200}, {"salary": 300}])
        200
        >>> solve([{"salary": 100}, {"salary": 100}])
        None
        >>> solve([{"salary": 100}])
        None
    """
    # Extract all salaries into a set to ensure we only consider distinct values
    distinct_salaries = {record["salary"] for record in employee_data}

    # If there are fewer than 2 distinct salaries, the second highest doesn't exist
    if len(distinct_salaries) < 2:
        return None

    # Convert to a list and sort in descending order to find the second element
    # Sorting takes O(N log N) in Python, but for a single pass O(N) is possible
    # using a two-variable tracking approach.
    
    highest = float('-inf')
    second_highest = float('-inf')

    for salary in distinct_salaries:
        if salary > highest:
            # Current salary is the new highest, old highest becomes second
            second_highest = highest
            highest = salary
        elif salary > second_highest:
            # Current salary is between highest and second highest
            second_highest = salary

    # If second_highest was never updated from its initial value, return None
    return int(second_highest) if second_highest != float('-inf') else None
