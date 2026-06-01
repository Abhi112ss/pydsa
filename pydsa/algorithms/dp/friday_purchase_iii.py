METADATA = {
    "id": 3118,
    "name": "Friday Purchase III",
    "slug": "friday-purchase-iii",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dp", "greedy"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Find the maximum total value of items purchased given specific constraints on purchase sequences.",
}

def solve(prices: list[int], discounts: list[int]) -> int:
    """
    Calculates the maximum total value of items purchased.
    
    The problem can be modeled as a dynamic programming problem where at each 
    step 'i', we decide whether to buy the item at index 'i' or skip it. 
    If we buy item 'i', we gain 'prices[i]' and the next available item 
    we can buy is at index 'i + discounts[i] + 1'.

    Args:
        prices: A list of integers representing the price of each item.
        discounts: A list of integers representing the discount period for each item.

    Returns:
        The maximum total value of items purchased.

    Examples:
        >>> solve([10, 20, 30], [1, 1, 1])
        40
        >>> solve([1, 2, 3, 4, 5], [0, 1, 0, 1, 0])
        9
    """
    n = len(prices)
    # dp[i] stores the maximum value we can get starting from index i to the end.
    # We use n + 1 to handle the base case (out of bounds) easily.
    dp = [0] * (n + 1)

    # Iterate backwards from the last item to the first.
    for i in range(n - 1, -1, -1):
        # Option 1: Skip the current item.
        # The value is the same as the maximum value starting from the next item.
        skip_item = dp[i + 1]

        # Option 2: Buy the current item.
        # The value is the current price plus the max value from the next available index.
        # The next available index is i + discount + 1 (since discount is the number of items to skip).
        next_available_index = i + discounts[i] + 1
        
        # Ensure we don't index out of bounds.
        if next_available_index < n:
            buy_item = prices[i] + dp[next_available_index]
        else:
            buy_item = prices[i]

        # The optimal choice at index i is the maximum of these two options.
        dp[i] = max(skip_item, buy_item)

    return dp[0]
