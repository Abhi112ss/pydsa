METADATA = {
    "id": 2678,
    "name": "Number of Senior Citizens",
    "slug": "number-of-senior-citizens",
    "category": "Array",
    "aliases": [],
    "tags": ["array", "counting"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Count the number of elements in an array that are greater than or equal to 60.",
}

def solve(ages: list[int]) -> int:
    """
    Counts how many people in the given list are senior citizens (age >= 60).

    Args:
        ages: A list of integers representing the ages of people.

    Returns:
        The total count of people whose age is 60 or greater.

    Examples:
        >>> solve([2, 9, 51, 86, 100])
        2
        >>> solve([18, 25, 30])
        0
        >>> solve([60, 60, 60])
        3
    """
    senior_citizen_count = 0
    
    # Iterate through each age in the provided list
    for age in ages:
        # Check if the current age meets the senior citizen threshold
        if age >= 60:
            senior_citizen_count += 1
            
    return senior_citizen_count
