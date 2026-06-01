METADATA = {
    "id": 1049,
    "name": "Last Stone Weight II",
    "slug": "last-stone-weight-ii",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dynamic_programming", "knapsack", "subset_sum"],
    "difficulty": "medium",
    "time_complexity": "O(n * sum)",
    "space_complexity": "O(sum)",
    "description": "Find the smallest possible weight of the last remaining stone by partitioning stones into two groups with minimum weight difference.",
}

def solve(stones: list[int]) -> int:
    """
    Calculates the minimum weight of the last remaining stone.
    
    The problem is equivalent to finding a subset of stones whose sum is 
    as close to half of the total sum as possible. This is a variation 
    of the 0/1 Knapsack problem (specifically the Subset Sum problem).
    
    Args:
        stones: A list of integers representing the weights of the stones.
        
    Returns:
        The minimum possible weight of the last stone.
        
    Examples:
        >>> solve([2, 7, 4, 1, 8, 1])
        1
        >>> solve([2, 4, 1, 1, 2])
        0
    """
    total_sum = sum(stones)
    # We want to find a subset sum that is as close to target as possible
    target = total_sum // 2
    
    # dp[i] will be True if a subset with sum 'i' can be formed
    # Using a bitset-like approach with a boolean array for space efficiency
    dp = [False] * (target + 1)
    dp[0] = True
    
    for weight in stones:
        # Iterate backwards to ensure each stone is used at most once (0/1 Knapsack)
        for current_sum in range(target, weight - 1, -1):
            if dp[current_sum - weight]:
                dp[current_sum] = True
                
    # Find the largest sum 's' such that s <= total_sum / 2
    # The two groups will have sums 's' and 'total_sum - s'
    # The difference is (total_sum - s) - s = total_sum - 2*s
    max_possible_subset_sum = 0
    for s in range(target, -1, -1):
        if dp[s]:
            max_possible_subset_sum = s
            break
            
    return total_sum - 2 * max_possible_subset_sum
