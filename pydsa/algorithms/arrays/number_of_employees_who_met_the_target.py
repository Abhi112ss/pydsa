METADATA = {
    "id": 2798,
    "name": "Number of Employees Who Met the Target",
    "slug": "number-of-employees-who-met-the-target",
    "category": "Array",
    "aliases": [],
    "tags": ["array", "counting"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Count how many employees have a score greater than or equal to a given target value.",
}

def solve(performance: list[int], target: int) -> int:
    """
    Counts the number of employees whose performance score meets or exceeds the target.

    Args:
        performance: A list of integers representing the performance scores of employees.
        target: An integer representing the minimum score required to meet the target.

    Returns:
        The total count of employees who met the target.

    Examples:
        >>> solve([1, 2, 3, 4, 5], 3)
        3
        >>> solve([10, 10, 10], 10)
        3
        >>> solve([1, 2, 3], 4)
        0
    """
    met_target_count = 0
    
    # Iterate through each score in the performance list
    for score in performance:
        # Check if the current score is greater than or equal to the target
        if score >= target:
            met_target_count += 1
            
    return met_target_count
