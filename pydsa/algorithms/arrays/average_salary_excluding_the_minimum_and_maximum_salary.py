METADATA = {
    "id": 1491,
    "name": "Average Salary Excluding the Minimum and Maximum Salary",
    "slug": "average-salary-excluding-the-minimum-and-maximum-salary",
    "category": "Array",
    "aliases": [],
    "tags": ["array", "math"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Calculate the average salary after removing the minimum and maximum values from the list.",
}

def solve(salary: list[float]) -> float:
    """
    Calculates the average salary excluding the minimum and maximum values.

    Args:
        salary: A list of floating point numbers representing salaries.

    Returns:
        The average of the salaries after removing one instance of the 
        minimum and one instance of the maximum value.

    Examples:
        >>> solve([10, 20, 30, 40, 50])
        30.0
        >>> solve([1, 1, 1, 1])
        1.0
    """
    # Initialize tracking variables for a single-pass approach
    # We need the sum, the minimum value, and the maximum value
    total_sum = 0.0
    min_salary = float('inf')
    max_salary = float('-inf')

    for s in salary:
        total_sum += s
        if s < min_salary:
            min_salary = s
        if s > max_salary:
            max_salary = s

    # Subtract exactly one instance of min and max from the total sum
    # The problem guarantees len(salary) >= 3
    adjusted_sum = total_sum - min_salary - max_salary
    
    # The number of elements remaining is the original length minus 2
    remaining_count = len(salary) - 2

    return adjusted_sum / remaining_count
