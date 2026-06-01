METADATA = {
    "id": 983,
    "name": "Minimum Cost For Tickets",
    "slug": "minimum-cost-for-tickets",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dynamic_programming", "array"],
    "difficulty": "medium",
    "time_complexity": "O(N)",
    "space_complexity": "O(N)",
    "description": "Find the minimum cost to travel on all required travel days using 1-day, 7-day, or 30-day passes.",
}

def solve(days: list[int], costs: list[int]) -> int:
    """
    Calculates the minimum cost to cover all travel days using available ticket options.

    Args:
        days: A sorted list of integers representing the days of travel.
        costs: A list of three integers representing the cost of 1-day, 7-day, and 30-day passes.

    Returns:
        The minimum cost required to cover all travel days.

    Examples:
        >>> solve([1, 4, 6, 7, 8, 20], [2, 7, 15])
        14
        >>> solve([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], [2, 7, 15])
        14
    """
    if not days:
        return 0

    last_day = days[-1]
    # dp[i] represents the minimum cost to cover all travel days up to day i.
    # We use a size of last_day + 1 to map days directly to indices.
    dp = [0] * (last_day + 1)
    
    # Convert days to a set for O(1) lookup to check if a specific day is a travel day.
    travel_days_set = set(days)

    for current_day in range(1, last_day + 1):
        if current_day not in travel_days_set:
            # If it's not a travel day, the cost remains the same as the previous day.
            dp[current_day] = dp[current_day - 1]
            continue

        # Option 1: Buy a 1-day pass for the current day.
        cost_1_day = dp[current_day - 1] + costs[0]

        # Option 2: Buy a 7-day pass that ends on the current day.
        # We look back 7 days, but ensure we don't go below index 0.
        prev_day_7 = max(0, current_day - 7)
        cost_7_day = dp[prev_day_7] + costs[1]

        # Option 3: Buy a 30-day pass that ends on the current day.
        # We look back 30 days, but ensure we don't go below index 0.
        prev_day_30 = max(0, current_day - 30)
        cost_30_day = dp[prev_day_30] + costs[2]

        # The minimum cost for the current day is the minimum of the three options.
        dp[current_day] = min(cost_1_day, cost_7_day, cost_30_day)

    return dp[last_day]
