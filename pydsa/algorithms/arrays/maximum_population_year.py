METADATA = {
    "id": 1854,
    "name": "Maximum Population Year",
    "slug": "maximum-population-year",
    "category": "Array",
    "aliases": [],
    "tags": ["difference_array", "array", "prefix_sum"],
    "difficulty": "easy",
    "time_complexity": "O(N)",
    "space_complexity": "O(N)",
    "description": "Find the earliest year with the maximum population using a difference array approach.",
}

def solve(birth: list[int], death: list[int]) -> int:
    """
    Finds the earliest year with the maximum population.

    Args:
        birth: A list of integers representing the birth year of each person.
        death: A list of integers representing the death year of each person.

    Returns:
        The earliest year with the maximum population.

    Examples:
        >>> solve([1950, 1961, 1970, 1940], [1961, 1970, 1980, 1950])
        1950
        >>> solve([1950, 1960, 1970], [1960, 1970, 1980])
        1950
    """
    # The problem constraints state years are between 1950 and 2050.
    # We use a difference array to track population changes.
    # Size 101 covers the range [1950, 2050] inclusive.
    OFFSET = 1950
    MAX_YEAR_RANGE = 2050 - 1950 + 1
    diff_array = [0] * (MAX_YEAR_RANGE + 1)

    # Mark the birth and death events.
    # A person is counted in the population from birth year up to (but not including) death year.
    for b, d in zip(birth, death):
        diff_array[b - OFFSET] += 1
        diff_array[d - OFFSET] -= 1

    max_pop = 0
    current_pop = 0
    earliest_year = 1950

    # Calculate prefix sums to find the population at each year.
    for year_idx in range(MAX_YEAR_RANGE):
        current_pop += diff_array[year_idx]
        
        # If we find a new maximum population, update the result.
        # Since we iterate chronologically, we naturally find the earliest year.
        if current_pop > max_pop:
            max_pop = current_pop
            earliest_year = year_idx + OFFSET

    return earliest_year
