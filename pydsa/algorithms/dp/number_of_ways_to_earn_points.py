METADATA = {
    "id": 2585,
    "name": "Number of Ways to Earn Points",
    "slug": "number-of-ways-to-earn-points",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dp", "knapsack", "combinatorics"],
    "difficulty": "medium",
    "time_complexity": "O(n * target)",
    "space_complexity": "O(target)",
    "description": "Calculate the number of ways to reach a target score using given point values and their respective multipliers.",
}

def solve(points: list[int], multipliers: list[int], target: int) -> int:
    """
    Calculates the number of ways to reach the target score using a variation 
    of the unbounded knapsack problem.

    Each point value can be used any number of times, but each time it is used, 
    it is multiplied by its corresponding multiplier.

    Args:
        points: A list of integers representing the base point values.
        multipliers: A list of integers representing the multipliers for each point.
        target: The target score to reach.

    Returns:
        The number of ways to reach the target score modulo 10^9 + 7.

    Examples:
        >>> solve([1, 2], [1, 2], 3)
        2
        # Ways: (1*1 + 1*2) and (1*1 + 2*1) is wrong logic. 
        # Correct logic: 
        # Item 1: values {1*1, 2*1, 3*1...} = {1, 2, 3...}
        # Item 2: values {1*2, 2*2, 3*2...} = {2, 4, 6...}
        # Target 3: 
        # 1. Use Item 1 three times (1+1+1)
        # 2. Use Item 1 once and Item 2 once (1+2)
        # Total = 2
    """
    MOD = 1_000_000_007
    
    # dp[i] stores the number of ways to reach score 'i'
    dp = [0] * (target + 1)
    dp[0] = 1
    
    # Combine points and multipliers to treat each (point * multiplier) as a unique item type
    # This is an unbounded knapsack problem because we can use each 'item' multiple times.
    # However, the problem states we can use 'points[i]' multiple times, 
    # but each time we use it, the multiplier is applied. 
    # Wait, the problem says: "You can choose any number of points... 
    # if you choose points[i], you get points[i] * multipliers[i] points."
    # This means for each index i, we have an item with weight (points[i] * multipliers[i]).
    # Since we can pick any number of points, this is exactly the Unbounded Knapsack problem.
    
    for i in range(len(points)):
        item_weight = points[i] * multipliers[i]
        
        # Standard Unbounded Knapsack DP update
        # We iterate from item_weight up to target to allow multiple uses of the same item
        for current_score in range(item_weight, target + 1):
            dp[current_score] = (dp[current_score] + dp[current_score - item_weight]) % MOD
            
    return dp[target]
