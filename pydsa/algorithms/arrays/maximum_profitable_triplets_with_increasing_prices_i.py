METADATA = {
    "id": 2907,
    "name": "Maximum Profitable Triplets With Increasing Prices I",
    "slug": "maximum-profitable-triplets-with-increasing-prices-i",
    "category": "Array",
    "aliases": [],
    "tags": ["array", "brute_force"],
    "difficulty": "easy",
    "time_complexity": "O(n^3)",
    "space_complexity": "O(1)",
    "description": "Find the number of triplets (i, j, k) such that i < j < k and prices[i] < prices[j] < prices[k] and the profit is maximized.",
}

def solve(prices: list[int], max_profit: int) -> int:
    """
    Calculates the number of triplets (i, j, k) that satisfy the conditions:
    i < j < k, prices[i] < prices[j] < prices[k], and the profit 
    (prices[j] - prices[i]) + (prices[k] - prices[j]) equals max_profit.
    
    Note: The profit formula simplifies to (prices[k] - prices[i]).

    Args:
        prices: A list of integers representing prices.
        max_profit: The maximum profit value to match.

    Returns:
        The count of triplets that achieve the max_profit.

    Examples:
        >>> solve([1, 2, 3, 4, 5], 4)
        2
        >>> solve([1, 5, 2, 4, 3], 3)
        1
    """
    n = len(prices)
    count = 0
    
    # Iterate through all possible triplets (i, j, k) where i < j < k
    for i in range(n):
        for j in range(i + 1, n):
            # Optimization: Only proceed if the first part of the condition is met
            if prices[i] < prices[j]:
                for k in range(j + 1, n):
                    # Check if the second part of the condition is met
                    if prices[j] < prices[k]:
                        # Calculate profit: (prices[j] - prices[i]) + (prices[k] - prices[j])
                        # This simplifies mathematically to prices[k] - prices[i]
                        current_profit = prices[k] - prices[i]
                        
                        if current_profit == max_profit:
                            count += 1
                            
    return count
