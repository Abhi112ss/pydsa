METADATA = {
    "id": 2110,
    "name": "Number of Smooth Descent Periods of a Stock",
    "slug": "number-of-smooth-descent-periods-of-a-stock",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dp", "arrays", "greedy"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Count the number of contiguous subarrays where the ratio of consecutive elements is at most 2.",
}

def solve(prices: list[int]) -> int:
    """
    Calculates the total number of smooth descent periods in a stock price list.
    
    A smooth descent period is a contiguous subarray where the ratio of 
    each pair of consecutive elements is at most 2.0.

    Args:
        prices: A list of integers representing stock prices.

    Returns:
        The total number of smooth descent periods.

    Examples:
        >>> solve([3, 5, 4, 2, 1])
        9
        >>> solve([10, 1, 1, 1])
        6
    """
    if not prices:
        return 0

    total_periods = 0
    current_streak_length = 0

    for i in range(len(prices)):
        # If it's the first element or the smooth descent condition is met
        # (price[i-1] / price[i] <= 2), increment the current streak.
        # Using multiplication to avoid floating point division issues: 
        # prices[i-1] <= 2 * prices[i]
        if i > 0 and prices[i-1] <= 2 * prices[i]:
            current_streak_length += 1
        else:
            # Reset streak to 1 if the condition is broken
            current_streak_length = 1
        
        # Every time we extend or start a streak, the number of new 
        # valid subarrays ending at index i is equal to the current streak length.
        # e.g., if streak is [5, 4, 2], new subarrays are [2], [4, 2], [5, 4, 2].
        total_periods += current_streak_length

    return total_periods
