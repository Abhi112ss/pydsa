METADATA = {
    "id": 1833,
    "name": "Maximum Ice Cream Bars",
    "slug": "maximum-ice-cream-bars",
    "category": "Greedy",
    "aliases": [],
    "tags": ["greedy", "sorting"],
    "difficulty": "easy",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(1)",
    "description": "Find the maximum number of ice cream bars you can buy given a budget by picking the cheapest ones first.",
}

def solve(costs: list[int], budget: int) -> int:
    """
    Calculates the maximum number of ice cream bars that can be purchased.

    Args:
        costs: A list of integers representing the cost of each ice cream bar.
        budget: An integer representing the total amount of money available.

    Returns:
        The maximum number of ice cream bars that can be bought within the budget.

    Examples:
        >>> solve([1, 1, 2, 3], 10)
        4
        >>> solve([4, 2, 3, 9], 1)
        0
        >>> solve([1, 1, 2, 3], 3)
        2
    """
    # Sort the costs in ascending order to apply the greedy strategy:
    # Always pick the cheapest available bar to maximize the count.
    costs.sort()

    ice_cream_count = 0
    current_spent = 0

    for cost in costs:
        # Check if adding the current cheapest bar exceeds the budget
        if current_spent + cost <= budget:
            current_spent += cost
            ice_cream_count += 1
        else:
            # Since the list is sorted, no subsequent bar will fit if this one doesn't
            break

    return ice_cream_count
