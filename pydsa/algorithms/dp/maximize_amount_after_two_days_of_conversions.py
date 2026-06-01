METADATA = {
    "id": 3387,
    "name": "Maximize Amount After Two Days of Conversions",
    "slug": "maximize-amount-after-two-days-of-conversions",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dp", "greedy"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Maximize the final amount of a target currency after two days of arbitrary currency conversions.",
}

def solve(n: int, conversions: list[list[float]], initial_amounts: list[float], target_currency: int) -> float:
    """
    Calculates the maximum amount of a target currency after two days of conversions.
    
    Each day, we can perform any number of conversions using the provided conversion rates.
    The goal is to maximize the amount of the target currency after exactly two days.
    
    Args:
        n: The number of different currencies.
        conversions: A list of lists where conversions[i] = [u, v, rate] 
                     representing that 1 unit of currency u can be converted to rate units of v.
        initial_amounts: A list of size n where initial_amounts[i] is the amount of currency i.
        target_currency: The index of the currency we want to maximize.

    Returns:
        The maximum amount of the target currency possible after two days.

    Examples:
        >>> solve(3, [[0, 1, 2.0], [1, 2, 3.0]], [10.0, 0.0, 0.0], 2)
        60.0
    """
    # Step 1: Find the maximum possible conversion rate between any two currencies i and j.
    # Since we can perform any number of conversions in one day, this is equivalent 
    # to finding the longest path in a graph where edge weights are multiplicative.
    # We use a variation of the Floyd-Warshall algorithm or multiple BFS/Dijkstra.
    # Given the constraints and the nature of the problem (maximizing product), 
    # we can use a Bellman-Ford style approach to find the max multiplier between all pairs.
    
    # max_rate[i][j] will store the maximum multiplier to go from currency i to j
    max_rate = [[0.0] * n for _ in range(n)]
    for i in range(n):
        max_rate[i][i] = 1.0
        
    for u, v, rate in conversions:
        max_rate[u][v] = max(max_rate[u][v], rate)
        # Assuming conversions are directed as per problem description
        
    # Floyd-Warshall to find all-pairs maximum conversion rates
    for k in range(n):
        for i in range(n):
            if max_rate[i][k] > 0:
                for j in range(n):
                    if max_rate[k][j] > 0:
                        max_rate[i][j] = max(max_rate[i][j], max_rate[i][k] * max_rate[k][j])

    # Step 2: Calculate the maximum amount of each currency after Day 1.
    # amount_day1[i] = max over all j (initial_amounts[j] * max_rate[j][i])
    amount_day1 = [0.0] * n
    for i in range(n):
        for j in range(n):
            if initial_amounts[j] > 0 and max_rate[j][i] > 0:
                amount_day1[i] = max(amount_day1[i], initial_amounts[j] * max_rate[j][i])

    # Step 3: Calculate the maximum amount of the target currency after Day 2.
    # amount_day2[target] = max over all i (amount_day1[i] * max_rate[i][target])
    max_final_amount = 0.0
    for i in range(n):
        if amount_day1[i] > 0 and max_rate[i][target_currency] > 0:
            max_final_amount = max(max_final_amount, amount_day1[i] * max_rate[i][target_currency])
            
    return max_final_amount
