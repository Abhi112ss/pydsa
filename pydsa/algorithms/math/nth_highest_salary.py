METADATA = {
    "id": 177,
    "name": "Nth Highest Salary",
    "slug": "nth_highest_salary",
    "category": "algorithms",
    "aliases": ["nth highest salary"],
    "tags": ["logic", "sorting"],
    "difficulty": "medium",
    "time_complexity": "O(N log N)",
    "space_complexity": "O(N)",
    "description": "Find the nth highest salary from a list of salaries, returning None if it does not exist.",
}

from typing import Optional

def solve(salaries: list[int], n: int) -> Optional[int]:
    """Finds the nth highest salary from a list of integers.

    Args:
        salaries: A list of integer salaries.
        n: The rank of the salary to retrieve (1-indexed).

    Returns:
        The nth highest unique salary, or None if it doesn't exist.

    Examples:
        >>> solve([100, 200, 300], 2)
        200
        >>> solve([100], 2)
        None
    """
    # Remove duplicates to ensure we are looking for the nth distinct value
    unique_salaries = list(set(salaries))
    
    # Sort salaries in descending order to easily access the nth highest
    unique_salaries.sort(reverse=True)
    
    # Check if n is valid (within the range of unique salaries available)
    # Note: n is 1-indexed as per typical SQL/problem definitions
    if 1 <= n <= len(unique_salaries):
        return unique_salaries[n - 1]
    
    return None