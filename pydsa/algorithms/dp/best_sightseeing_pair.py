METADATA = {
    "id": 1014,
    "name": "Best Sightseeing Pair",
    "slug": "best-sightseeing-pair",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dynamic_programming", "arrays", "greedy"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the maximum value of values[i] + values[j] + i - j where i < j.",
}

def solve(values: list[int]) -> int:
    """
    Finds the maximum value of values[i] + values[j] + i - j for all i < j.

    The formula can be rewritten as (values[i] + i) + (values[j] - j).
    To maximize this, as we iterate through the array, we keep track of the 
    maximum (values[i] + i) encountered so far and use it to calculate 
    the potential score with the current index j.

    Args:
        values: A list of integers representing the values at each location.

    Returns:
        The maximum score possible from a sightseeing pair.

    Examples:
        >>> solve([1, 2, 10, 4])
        11
        >>> solve([15, 3, 7, 10, 2])
        17
    """
    max_score = 0
    # max_prev_part tracks the maximum value of (values[i] + i) seen so far
    max_prev_part = values[0] + 0

    for j in range(1, len(values)):
        # Calculate score using current j as the second element in the pair
        # current_score = (values[i] + i) + (values[j] - j)
        current_score = max_prev_part + values[j] - j
        max_score = max(max_score, current_score)

        # Update max_prev_part to include the current index as a potential 'i' for future 'j's
        max_prev_part = max(max_prev_part, values[j] + j)

    return max_score
