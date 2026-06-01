METADATA = {
    "id": 3572,
    "name": "Maximize Y-Sum by Picking a Triplet of Distinct X-Values",
    "slug": "maximize-y-sum-by-picking-a-triplet-of-distinct-x-values",
    "category": "Greedy",
    "aliases": [],
    "tags": ["sorting", "greedy"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Find the maximum sum of y-values by selecting exactly three elements with distinct x-values.",
}

def solve(points: list[list[int]]) -> int:
    """
    Finds the maximum sum of y-values by picking exactly three elements 
    that have distinct x-values.

    Args:
        points: A list of lists where each sub-list contains [x, y].

    Returns:
        The maximum sum of three y-values with distinct x-values. 
        Returns -1 if it is impossible to pick three distinct x-values.

    Examples:
        >>> solve([[1, 10], [1, 20], [2, 5], [3, 15], [3, 30]])
        55  # Picks (1, 20), (2, 5), (3, 30) -> 20 + 5 + 30 = 55
        >>> solve([[1, 10], [1, 20], [2, 5]])
        -1  # Only two distinct x-values available
    """
    # Group the maximum y-value for each unique x-value
    # Since we want to maximize the sum, for any given x, 
    # we only care about the largest y associated with it.
    max_y_per_x: dict[int, int] = {}
    for x, y in points:
        if x not in max_y_per_x or y > max_y_per_x[x]:
            max_y_per_x[x] = y

    # If we have fewer than 3 unique x-values, we cannot form a triplet
    if len(max_y_per_x) < 3:
        return -1

    # Extract all the maximum y-values found for each unique x
    candidate_y_values: list[int] = list(max_y_per_x.values())

    # Sort the y-values in descending order to pick the largest ones greedily
    candidate_y_values.sort(reverse=True)

    # The sum of the top 3 largest y-values will be the maximum possible sum
    # because each y-value corresponds to a unique x-value by construction.
    return sum(candidate_y_values[:3])
