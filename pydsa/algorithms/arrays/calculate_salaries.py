METADATA = {
    "id": 1468,
    "name": "Calculate Salaries",
    "slug": "calculate-salaries",
    "category": "Array",
    "aliases": [],
    "tags": ["array", "hash_map"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Calculate new salaries based on employee ratings using specific multiplier rules.",
}

def solve(salary: list[int], rating: list[int]) -> list[int]:
    """
    Calculates the new salaries for employees based on their ratings.

    Rules:
    - Rating 3: salary * 2
    - Rating 2: salary * 1
    - Rating 1: salary * 0.5 (integer division)
    - Rating 4: salary + 1
    - Rating 5: salary + 2

    Args:
        salary: A list of integers representing current salaries.
        rating: A list of integers representing employee ratings.

    Returns:
        A list of integers representing the updated salaries.

    Examples:
        >>> solve([10, 20, 30, 40, 50], [1, 2, 3, 4, 5])
        [5, 20, 60, 41, 52]
        >>> solve([1, 2, 3, 4, 5], [5, 4, 3, 2, 1])
        [7, 5, 6, 2, 0]
    """
    n = len(salary)
    new_salaries = [0] * n

    for i in range(n):
        current_rating = rating[i]
        current_salary = salary[i]

        # Apply multiplier rules based on the rating value
        if current_rating == 3:
            new_salaries[i] = current_salary * 2
        elif current_rating == 2:
            new_salaries[i] = current_salary
        elif current_rating == 1:
            # Use integer division for rating 1 as per problem requirements
            new_salaries[i] = current_salary // 2
        elif current_rating == 4:
            new_salaries[i] = current_salary + 1
        elif current_rating == 5:
            new_salaries[i] = current_salary + 2
        else:
            # This case should not be reached based on problem constraints
            new_salaries[i] = current_salary

    return new_salaries
