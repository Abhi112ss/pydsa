METADATA = {
    "id": 3647,
    "name": "Maximum Weight in Two Bags",
    "slug": "maximum-weight-in-two-bags",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dp", "knapsack", "subset sum"],
    "difficulty": "medium",
    "time_complexity": "O(n * W)",
    "space_complexity": "O(W^2)",
    "description": "Maximize the total weight of items placed into two separate bags with given capacities.",
}

def solve(weights: list[int], capacity_a: int, capacity_b: int) -> int:
    """
    Finds the maximum total weight that can be distributed into two bags 
    with capacities capacity_a and capacity_b.

    This is a variation of the 2D knapsack problem where each item can be 
    placed in Bag A, Bag B, or neither.

    Args:
        weights: A list of integers representing the weight of each item.
        capacity_a: The maximum weight capacity of the first bag.
        capacity_b: The maximum weight capacity of the second bag.

    Returns:
        The maximum total weight possible in both bags combined.

    Examples:
        >>> solve([1, 2, 3], 3, 3)
        6
        >>> solve([4, 5, 6], 2, 2)
        0
        >>> solve([1, 10, 5], 5, 5)
        6
    """
    # dp[i][j] represents the maximum weight in Bag B given that 
    # Bag A currently contains weight 'i'.
    # However, since we want to maximize the SUM (weight_a + weight_b),
    # and we are constrained by two independent capacities, we can 
    # treat this as a 2D knapsack problem.
    
    # dp[a][b] = True if it is possible to have weight 'a' in Bag A 
    # and weight 'b' in Bag B.
    # To optimize space, we use a 2D array and iterate backwards.
    
    # Using a boolean DP table to track reachable (weight_a, weight_b) states.
    # dp[a][b] is True if weight 'a' in bag A and 'b' in bag B is achievable.
    dp = [[False] * (capacity_b + 1) for _ in range(capacity_a + 1)]
    dp[0][0] = True

    for weight in weights:
        # Iterate backwards through capacities to reuse the same DP table
        # (standard space optimization for knapsack)
        for a in range(capacity_a, -1, -1):
            for b in range(capacity_b, -1, -1):
                if dp[a][b]:
                    # Option 1: Put item in Bag A
                    if a + weight <= capacity_a:
                        dp[a + weight][b] = True
                    
                    # Option 2: Put item in Bag B
                    if b + weight <= capacity_b:
                        dp[a][b + weight] = True
                    
                    # Option 3: Don't include item (already handled by dp[a][b] being True)

    max_total_weight = 0
    # Iterate through all reachable states to find the maximum sum
    for a in range(capacity_a + 1):
        for b in range(capacity_b + 1):
            if dp[a][b]:
                max_total_weight = max(max_total_weight, a + b)

    return max_total_weight
