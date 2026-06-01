METADATA = {
    "id": 176,
    "name": "Second Highest Salary",
    "slug": "second_highest_salary",
    "category": "database",
    "aliases": ["second highest"],
    "tags": ["logic", "sorting"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the second highest distinct salary from a list of salaries, returning None if it does not exist.",
}


def solve(salaries: list[int]) -> int | None:
    """Finds the second highest distinct salary from a list.

    Args:
        salaries: A list of integers representing salaries.

    Returns:
        The second highest distinct salary, or None if it doesn't exist.

    Examples:
        >>> solve([100, 200, 300])
        200
        >>> solve([100])
        None
        >>> solve([100, 100])
        None
    """
    if not salaries:
        return None

    first_highest = float('-inf')
    second_highest = float('-inf')

    # Iterate through the salaries to find the top two distinct values
    for salary in salaries:
        if salary > first_highest:
            # Shift current highest to second highest
            second_highest = first_highest
            first_highest = salary
        elif first_highest > salary > second_highest:
            # Update second highest if current is between first and second
            second_highest = salary

    # If second_highest remains -inf, no distinct second highest was found
    if second_highest == float('-inf'):
        return None

    return int(second_highest)

# Note: In a SQL context, this is typically solved using:
# SELECT MAX(Salary) FROM Employee WHERE Salary < (SELECT MAX(Salary) FROM Employee)
# or using OFFSET 1 with LIMIT 1 after sorting distinct values.