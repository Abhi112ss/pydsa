METADATA = {
    "id": 2853,
    "name": "Highest Salaries Difference",
    "slug": "highest-salaries-difference",
    "category": "Arrays",
    "aliases": [],
    "tags": ["arrays", "sorting"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the difference between the maximum and minimum values in an array of salaries.",
}

def solve(salaries: list[int]) -> int:
    """
    Calculates the difference between the highest and lowest salaries in the list.

    Args:
        salaries: A list of integers representing individual salaries.

    Returns:
        The difference between the maximum and minimum salary. 
        Returns 0 if the list is empty or contains one element.

    Examples:
        >>> solve([100, 200, 50, 400])
        350
        >>> solve([500])
        0
        >>> solve([])
        0
    """
    if not salaries:
        return 0

    # Initialize min and max with the first element to handle single-pass comparison
    min_salary = salaries[0]
    max_salary = salaries[0]

    # Iterate through the list once to find both extremes in O(n) time
    for salary in salaries:
        if salary < min_salary:
            min_salary = salary
        elif salary > max_salary:
            max_salary = salary

    return max_salary - min_salary
