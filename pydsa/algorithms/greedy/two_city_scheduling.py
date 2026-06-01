METADATA = {
    "id": 1029,
    "name": "Two City Scheduling",
    "slug": "two-city-scheduling",
    "category": "Greedy",
    "aliases": [],
    "tags": ["greedy", "sorting"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Minimize the total cost of sending n people to city A and n people to city B given specific costs for each person.",
}

def solve(costs: list[list[int]]) -> int:
    """
    Calculates the minimum cost to send exactly half of the people to city A 
    and the other half to city B.

    The strategy is to calculate the relative 'profit' or 'loss' of sending 
    a person to city A instead of city B. By sorting people based on the 
    difference (cost_A - cost_B), we can greedily pick the people who are 
    cheapest to send to city A relative to city B.

    Args:
        costs: A list of lists where costs[i] = [cost_i_A, cost_i_B].

    Returns:
        The minimum total cost.

    Examples:
        >>> solve([[10, 20], [30, 20], [40, 30], [50, 40]])
        130
        >>> solve([[10, 100], [100, 10], [10, 10], [100, 100]])
        130
    """
    # Sort people by the difference between cost A and cost B.
    # A negative difference means city A is much cheaper than city B.
    # A positive difference means city B is much cheaper than city A.
    costs.sort(key=lambda person: person[0] - person[1])

    total_cost = 0
    n = len(costs) // 2

    # The first n people in the sorted list have the smallest (most negative) 
    # difference, meaning they are the most optimal to send to city A.
    for i in range(n):
        total_cost += costs[i][0]

    # The remaining n people are the most optimal to send to city B.
    for i in range(n, 2 * n):
        total_cost += costs[i][1]

    return total_cost
