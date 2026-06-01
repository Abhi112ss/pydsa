METADATA = {
    "id": 1774,
    "name": "Closest Dessert Cost",
    "slug": "closest-dessert-cost",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dp", "binary_search"],
    "difficulty": "medium",
    "time_complexity": "O(n * target)",
    "space_complexity": "O(target)",
    "description": "Find the minimum cost to satisfy a customer's craving by choosing a combination of desserts such that the total cost is as close to the target as possible.",
}

def solve(desserts: list[int], target: int) -> int:
    """
    Finds the dessert cost closest to the target using a variation of the knapsack problem.

    Args:
        desserts: A list of integers representing the costs of available desserts.
        target: The target cost the customer wants to reach.

    Returns:
        The integer cost that is closest to the target.

    Examples:
        >>> solve([1, 10, 100], 5)
        1
        >>> solve([1, 10, 100], 15)
        11
    """
    # The maximum possible cost we might care about is target + (smallest dessert cost).
    # However, a safe upper bound for the DP array is target + max(desserts) or 
    # simply target + the smallest dessert to check the next possible step.
    # To simplify, we can cap the search at target + min(desserts).
    
    min_dessert = min(desserts)
    # We only need to track possible sums up to target + min_dessert.
    # Any sum larger than target + min_dessert will definitely be further from target
    # than the sum 'target' itself or the smallest sum greater than target.
    limit = target + min_dessert
    
    # dp[i] will be True if a total cost of 'i' is achievable.
    dp = [False] * (limit + 1)
    dp[0] = True
    
    # Standard 0/1 Knapsack-style DP (but we can use each dessert multiple times? 
    # Wait, the problem says "a combination of desserts", implying we can use 
    # each dessert as many times as we want? 
    # Re-reading: "You can choose any number of desserts... each dessert can be used multiple times."
    # This is actually the Unbounded Knapsack problem.
    
    for dessert in desserts:
        for cost in range(dessert, limit + 1):
            if dp[cost - dessert]:
                dp[cost] = True
                
    # Find the closest achievable cost to the target.
    closest_cost = float('inf')
    
    for cost in range(limit + 1):
        if dp[cost]:
            # Check if this achievable cost is closer to target than our current best.
            if abs(cost - target) < abs(closest_cost - target):
                closest_cost = cost
            # If distances are equal, the problem implies we return the smaller cost?
            # Actually, the problem says "If there are multiple, return the smallest."
            elif abs(cost - target) == abs(closest_cost - target):
                closest_cost = min(closest_cost, cost)
                
    return int(closest_cost)
